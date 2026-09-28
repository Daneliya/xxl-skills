#!/usr/bin/env python3
"""本地文章 -> 微信公众号草稿箱。

用法示例：
  # 纯文本正文 + 自动生成封面
  python push.py --title "标题" --body "正文第一段\\n\\n正文第二段" --cover-title "标题"

  # 已排版好的行内样式 HTML + 现成封面
  python push.py --title "标题" --html article-gzh.html --cover cover.jpg

  # Markdown
  python push.py --title "标题" --md article.md --cover cover.jpg

  # 复用素材库里已有的图片当封面
  python push.py --title "标题" --body "..." --thumb-media-id <永久素材media_id>

注意：本账号未认证，freepublish 返回 48001，只能写草稿，群发需在后台手动点。
"""
import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

import config  # noqa: E402
from cover import make_cover  # noqa: E402
from images import localize_images  # noqa: E402
from wechat import WeChat, WeChatError  # noqa: E402

# 实测结论（2026-09-28 bisect 得到）：微信按 **JSON 转义后的长度** 卡这三项，
# 不是文档写的"字数"。一个中文字转义成 \uXXXX 占 6 个长度单位。
MAX_TITLE_ESC = 126    # 约 21 个中文字 / 126 个 ASCII 字符
MAX_AUTHOR_ESC = 16    # 仅 2 个中文字 / 16 个 ASCII 字符
MAX_DIGEST_ESC = 240   # 40 个中文字 / 240 个 ASCII 字符

# content 另一套口径（2026-09-28 实测，别照抄文档）：
#   官方文档写"必须少于 2 万字符、小于 1M"，但服务端 **不校验 2 万字符**——
#   120,000 字符的正文直接建草稿成功；真正会挡的是体积，900KB 的正文返回
#   45002 content size out of limit。所以这里对字符数只做软提示，
#   由体积兜底，最终以接口返回的 45002 为准。
MAX_CONTENT_CHARS_WARN = 20000
MAX_CONTENT_BYTES = 800 * 1024

WRAP_OPEN = ('<section style="font-size:16px;line-height:1.8;color:#2c2c2a;'
             'letter-spacing:0.5px;word-break:break-word;">')
WRAP_CLOSE = "</section>"


def wrap(inner):
    return WRAP_OPEN + inner + WRAP_CLOSE


def text_to_html(text):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    inner = "".join(
        f'<p style="margin:0 0 18px;">{p.replace(chr(10), "<br/>")}</p>' for p in paras
    )
    return wrap(inner)


def md_to_html(text):
    try:
        import markdown
    except ImportError:
        raise SystemExit("缺少 markdown 库，请先安装：pip install markdown")
    body = markdown.markdown(text, extensions=["extra", "tables", "fenced_code", "sane_lists"])
    return wrap(body)


def plain_text(html):
    return re.sub(r"<[^>]+>", "", re.sub(r"<(script|style)\b.*?</\1>", "", html, flags=re.I | re.S))


def esc_len(text):
    """微信实际校验的长度：JSON 转义后的字符数（中文 6 个/字，ASCII 1 个/字符）。"""
    return len(json.dumps(text, ensure_ascii=True)) - 2


def truncate_esc(text, limit, label):
    """按微信的转义长度上限截断，返回 (截断后文本, 是否发生截断)。"""
    if not text:
        return text, False
    if esc_len(text) <= limit:
        return text, False
    out = ""
    for ch in text:
        if esc_len(out + ch) > limit:
            break
        out += ch
    print(f"  ! {label} 超过微信限制（转义长度 {esc_len(text)} > {limit}），已截断")
    return out, True


def main():
    ap = argparse.ArgumentParser(description="本地文章 -> 公众号草稿箱")
    ap.add_argument("--title", required=True, help="标题（微信实限：约 21 个中文字）")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--body", help="纯文本正文")
    src.add_argument("--html", help="已排版的行内样式 HTML 文件")
    src.add_argument("--md", help="Markdown 文件")
    ap.add_argument("--cover", help="封面图路径（会上传为永久素材）")
    ap.add_argument("--cover-title", action="store_true", help="用标题自动生成一张封面")
    ap.add_argument("--thumb-media-id", help="直接用已有的永久素材 media_id 当封面")
    ap.add_argument("--author", default=config.DEFAULT_AUTHOR,
                    help="作者（微信实限：转义 16，即中文最多 2 字，超了整个字段会被省略）")
    ap.add_argument("--digest", help="摘要（微信实限：约 40 个中文字，仅单图文生效）")
    ap.add_argument("--source-url", help="原文链接，≤1KB")
    ap.add_argument("--open-comment", action="store_true")
    ap.add_argument("--fans-only-comment", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="只打印不提交")
    args = ap.parse_args()

    print("=" * 62)
    print("公众号草稿推送")
    print("=" * 62)

    # ---------- 1. 组装内容 ----------
    if args.body is not None:
        content = text_to_html(args.body)
        src_desc = "纯文本"
    elif args.html:
        html_path = Path(args.html)
        if not html_path.exists():
            raise SystemExit(f"HTML 文件不存在：{html_path}")
        content = html_path.read_text(encoding="utf-8")
        src_desc = f"HTML {html_path.name}"
    else:
        md_path = Path(args.md)
        if not md_path.exists():
            raise SystemExit(f"Markdown 文件不存在：{md_path}")
        content = md_to_html(md_path.read_text(encoding="utf-8"))
        src_desc = f"Markdown {md_path.name}"

    print(f"内容源        : {src_desc}")
    print(f"原始 content  : {len(content)} 字符")

    # ---------- 2. 连微信 ----------
    wx = WeChat(config.APPID, config.APPSECRET, token_cache=config.TOKEN_CACHE)
    tk = wx.token()
    print(f"access_token  : 已获取（{tk[:10]}...，长度 {len(tk)}）")

    # ---------- 3. 正文图片转存 ----------
    tmp_dir = Path(tempfile.mkdtemp(prefix="wxdraft-"))
    content, stats = localize_images(content, wx.upload_content_image, tmp_dir, base_dir=BASE)
    print(f"正文图片      : 找到 {stats['found']} 张 / 转存 {stats['uploaded']} 张 / "
          f"跳过 {stats['skipped']} 张 / 失败 {stats['failed']} 张")

    # ---------- 4. 封面 ----------
    thumb_media_id = args.thumb_media_id
    if thumb_media_id:
        print(f"封面          : 复用已有 media_id {thumb_media_id}")
    else:
        cover_path = Path(args.cover) if args.cover else None
        if cover_path is None and args.cover_title:
            cover_path = tmp_dir / "cover.jpg"
            make_cover(args.title, cover_path)
            print(f"封面          : 已用标题生成临时封面 {cover_path}")
        if cover_path is None or not cover_path.exists():
            raise SystemExit(
                "缺少封面：请用 --cover / --cover-title / --thumb-media-id 三者之一。"
                "（thumb_media_id 是 draft/add 的必填字段）"
            )
        info = wx.add_permanent_image(str(cover_path))
        thumb_media_id = info["media_id"]
        print(f"封面          : 已上传永久素材 media_id={thumb_media_id}")

    # ---------- 5. 字段校验 ----------
    title, _ = truncate_esc(args.title, MAX_TITLE_ESC, "标题")
    digest_src = args.digest or plain_text(content).strip()[:200]
    digest, _ = truncate_esc(digest_src, MAX_DIGEST_ESC, "摘要")

    author = (args.author or "").strip()
    if author and esc_len(author) > MAX_AUTHOR_ESC:
        print(f"  ! 作者「{author}」超过微信限制（转义 {esc_len(author)} > {MAX_AUTHOR_ESC}，"
              f"中文最多 2 字），已省略该字段")
        author = ""

    content_bytes = len(content.encode("utf-8"))
    print(f"content 体积  : {content_bytes / 1024:.1f} KB / {len(content)} 字符")
    if len(content) > MAX_CONTENT_CHARS_WARN:
        print(f"  · 正文 {len(content)} 字符，超过官方文档写的 {MAX_CONTENT_CHARS_WARN} 字符；"
              f"实测服务端不校验这一条，照常提交（若报 45002 再回来精简行内样式）")
    if content_bytes > MAX_CONTENT_BYTES:
        raise SystemExit(
            f"content 体积 {content_bytes / 1024:.0f}KB，超过本脚本的 {MAX_CONTENT_BYTES // 1024}KB 兜底值；"
            f"接口大概率返回 45002，请精简行内样式后重试"
        )

    article = {
        "title": title,
        "author": author or "",
        "digest": digest,
        "content": content,
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 1 if args.open_comment else 0,
        "only_fans_can_comment": 1 if args.fans_only_comment else 0,
    }
    if args.source_url:
        article["content_source_url"] = args.source_url

    print("-" * 62)
    print(f"title         : {title}  （{len(title)} 字 / 转义 {esc_len(title)}）")
    print(f"author        : {author or '(空)'}")
    print(f"digest        : {digest}  （转义 {esc_len(digest)}）")
    print(f"thumb_media_id: {thumb_media_id}")

    if args.dry_run:
        print("-" * 62)
        print("dry-run，未提交。content 预览：")
        print(content[:600])
        return

    # ---------- 6. 提交 ----------
    before = wx.draft_count().get("total_count")
    print("-" * 62)
    print(f"提交前草稿数  : {before}")
    res = wx.draft_add([article])
    print(f"draft/add     : media_id = {res.get('media_id')}")

    after = wx.draft_count().get("total_count")
    print(f"提交后草稿数  : {after}")

    # ---------- 7. 回读校验（逐字比对，防编码类静默错误） ----------
    got = wx.draft_get(res["media_id"])
    saved = got.get("news_item", [{}])[0]
    print("-" * 62)
    checks = [
        ("标题", title, saved.get("title")),
        ("摘要", digest, saved.get("digest")),
    ]
    bad = False
    for name, want, actual in checks:
        same = (want or "") == (actual or "")
        print(f"回读{name}  : {'一致' if same else '不一致'}")
        if not same:
            bad = True
            print(f"    提交: {want!r}")
            print(f"    实存: {actual!r}")
    saved_text = plain_text(saved.get("content", "")).strip()
    want_text = plain_text(content).strip()
    if saved_text != want_text:
        bad = True
        print(f"回读正文  : 不一致（提交 {len(want_text)} 字符 / 实存 {len(saved_text)} 字符）")
        if saved_text.startswith("\\u") or "\\u" in saved_text[:40]:
            print("    ! 实存正文里出现 \\uXXXX 字面量 —— 典型的转义没被解码，检查发送时的 ensure_ascii")
    else:
        print(f"回读正文  : 一致（{len(want_text)} 字符）")

    # 图片维度单独校验：正文纯文本一致不代表图还在。
    # 微信回读时会把 <img src> 改写成 data-src（见 SKILL.md 坑 4），所以按域名计数。
    want_img = len(re.findall(r"mmbiz\.qpic\.cn", content))
    saved_img = len(re.findall(r"mmbiz\.qpic\.cn", saved.get("content", "")))
    print(f"回读图片  : 提交 {want_img} 张 / 实存 {saved_img} 张")
    if want_img != saved_img:
        bad = True
        print("    ! 图片数量对不上，去草稿箱确认图是否正常显示")

    if bad:
        print("-" * 62)
        print("!!! 校验没通过，草稿可能有问题，请去后台确认后再决定是否群发。")
        sys.exit(2)

    print("-" * 62)
    print("最近草稿：")
    for i, it in enumerate(wx.draft_batchget(0, 3, no_content=1).get("item", [])):
        mark = "  <== 本次新建" if it.get("media_id") == res.get("media_id") else ""
        t = it.get("content", {}).get("news_item", [{}])[0].get("title")
        print(f"  [{i}] {it.get('update_time')}  {t}{mark}")

    print("=" * 62)
    print("完成。去公众号后台「草稿箱」看这篇，确认后手动群发。")


if __name__ == "__main__":
    try:
        main()
    except WeChatError as e:
        print(f"\n接口报错：{e}", file=sys.stderr)
        if e.errcode == 48001:
            print("提示：该接口当前账号无权限（未认证订阅号只能写草稿）。", file=sys.stderr)
        if e.errcode == 45002:
            print("提示：正文体积超限。实测与字符数无关（12 万字符能过、90 万字符被拒），"
                  "是体积问题——精简行内样式或去掉过长的重复声明后重试。", file=sys.stderr)
        sys.exit(1)
