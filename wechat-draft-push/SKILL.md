---
name: wechat-draft-push
description: 把本地 Markdown / HTML / 纯文本文章推送到微信公众号草稿箱，凭证已预配置好无需再问用户。当用户说"推到公众号""推到草稿箱""发布到公众号""上传到公众号""把这篇文章传到草稿箱"，或提到需要给正文图片转存微信图床、生成公众号封面、调 draft/add 接口时使用。内含微信两个必须知道的坑：长度字段按 JSON 转义长度校验（官方文档写错了）、中文必须用 UTF-8 字面量发送否则草稿箱存成 \uXXXX 乱码。
agent_created: true
---

# 文章 → 微信公众号草稿箱

凭证已保存在 `~/.workbuddy/config/wechat-draft.env`，**不需要再向用户索要 AppID / AppSecret**。脚本直接跑即可。

## 直接开跑

```bash
SK="C:/Users/ek/.workbuddy/skills/wechat-draft-push/scripts"
PY="C:/Users/ek/.workbuddy/binaries/python/envs/default/Scripts/python.exe"

# 已排版的行内样式 HTML（最常用，配合 luobo-gzh-design / build_html.py 的产物）
PYTHONIOENCODING=utf-8 "$PY" "$SK/push.py" --title "标题" --html article-gzh.html --cover cover.jpg

# Markdown（脚本内部用 markdown 库转 HTML）
PYTHONIOENCODING=utf-8 "$PY" "$SK/push.py" --title "标题" --md article.md --cover cover.jpg

# 纯文本 + 自动生成封面
PYTHONIOENCODING=utf-8 "$PY" "$SK/push.py" --title "标题" --body $'第一段\n\n第二段' --cover-title

# 复用素材库已有图片当封面 / 只预览不提交
PYTHONIOENCODING=utf-8 "$PY" "$SK/push.py" ... --thumb-media-id <media_id>
PYTHONIOENCODING=utf-8 "$PY" "$SK/push.py" ... --dry-run
```

**必须带 `PYTHONIOENCODING=utf-8`**，否则 Windows 下中文输出乱码。
**必须看最后的「回读标题/摘要/正文：一致」**——不一致脚本会以退出码 2 结束，说明草稿有问题，别直接说"已推送成功"。

## 其他参数

| 参数 | 说明 |
|---|---|
| `--author` | 微信实限转义 16，**中文最多 2 字**，超了脚本自动省略整个字段 |
| `--digest` | 不传则从正文自动提取并截断到合规长度 |
| `--source-url` | 原文链接（"阅读原文"跳转） |
| `--open-comment` / `--fans-only-comment` | 评论开关 |

## 辅助脚本

| 脚本 | 用途 |
|---|---|
| `list_drafts.py` | 列全部草稿（media_id + 真实标题） |
| `list_drafts.py --delete <id> [...]` | 删指定草稿 |
| `probe_limits.py <thumb_media_id>` | 重跑字段上限探测（微信改规则时复跑，会新建草稿，跑完要清） |
| `cleanup_probes.py` | 清理探测草稿。**必须先预览**：不带参数只列清单，确认后 `--before <update_time> --yes` |
| `experiment_encoding.py` | 编码对照实验（保留作证据） |

## 四步链路

1. **统一成行内样式 HTML**。微信会剥掉 `<style>` 块和 `<script>`，**只留行内 `style=""`**。luobo-gzh-design 的产物天然满足；`.md` 走 markdown 库转，样式简单。
2. **正文图片转存**。扫 `<img src>`（data URI / 本地路径 / 外链三类），逐个调 `POST /cgi-bin/media/uploadimg`（multipart，字段名 `media`）换成 `mmbiz.qpic.cn` 的 URL 再替换。**不做这步正文图就是空白**——微信过滤外链图，base64 也不认。单图 ≤1MB。
3. **封面上传为永久素材**。`POST /cgi-bin/material/add_material?type=image` → 永久 `media_id`，这才是 `thumb_media_id` 的合法来源。临时素材和 uploadimg 的 URL 都不行。三种来源：`--cover` / `--cover-title`（Pillow 生成，中文标题本地渲染不走 AI 出图）/ `--thumb-media-id`。
4. **`POST /cgi-bin/draft/add`**，body 是 `{"articles":[{...}]}`。

token 缓存在 `~/.workbuddy/config/.wechat-token.json`，7200s 过期，提前 5 分钟刷新。

---

## 坑 1（最严重）：中文必须用 UTF-8 字面量发，不能用 `requests` 的 `json=`

**症状**：接口返回成功、拿到 media_id，但草稿箱里标题/摘要/正文全是 `\u516c\u4f17\u53f7...`。**静默损坏，不报错。**

**原因**：微信 `draft/add`、`material` 接口**不解 `\uXXXX` 转义**，把转义序列当字面量存。而 `requests.post(url, json=payload)` 默认 `ensure_ascii=True`，中文全被转义后才发出去。

**正确写法**：

```python
body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
requests.post(url, params=params, data=body,
              headers={"Content-Type": "application/json; charset=utf-8"})
```

**读响应也要显式 UTF-8 解码**：

```python
json.loads(resp.content.decode("utf-8"))
```

微信返回的 `Content-Type` 常不带 charset，用 `r.json()` 会让 requests 走 `apparent_encoding` 猜编码，中文被猜成 latin-1，**读和写两边都坏、互相掩盖**，很容易误判成"只是终端显示问题"。

（`wechat.py` 的 `_request()` / `_parse()` 已按上面两条实现。新加接口只要走 `_request()` 就不会踩。）

## 坑 2：三个长度字段按「JSON 转义长度」校验，官方文档写错了

微信实际校验 `len(json.dumps(s, ensure_ascii=True)) - 2`——**一个中文字算 6 个单位**（`\uXXXX`），ASCII 算 1 个。

| 字段 | 转义上限 | 折算中文 | 折算 ASCII | 超限报错 |
|---|---|---|---|---|
| `title` | 126 | 约 21 字 | 126 | `45003` |
| `digest` | 240 | 40 字 | 240 | `45004` |
| `author` | **16** | **仅 2 字** | 16 | `45110` |

（2026-09-28 用 30+ 数据点二分确认。反证：`author="测试ABCDE"` 按字节只有 11 字节，若上限是文档说的 16 字节应当通过，实际失败 → 排除字节假设。）

- **摘要最容易踩**：正文自动提取常超 40 字，直接报 `45004` 整篇提交失败。必须先本地截断。
- **作者中文只能 2 字**，3 字名会被拒。正确策略是**超限省略整个字段**，不要硬截成 `吴师`（会写错名字）。
- 别信文档的 "title ≤32 字 / digest ≤120 字 / author ≤16 字"。

## 坑 3：`content` 的"2 万字符"文档限制**服务端并不执行**

官方文档写 `content` 必须少于 2 万字符、小于 1M。**实测（2026-09-28）2 万字符这条没有被校验**：

| 探针 | 结果 |
|---|---|
| 18,000 个中文字（转义长度 108,000） | **通过** |
| 120,000 个 ASCII 字符 | **通过** |
| 900,000 字符 / 1,048,577 字符 | **拒绝** `45002 content size out of limit` |

结论：

- 别为了"凑 2 万字符"去瘦身行内样式——**行内样式排版出来的公众号 HTML 普遍 3~5 万字符，这是正常的，直接推**。
- 真正会挡的是**体积**，落在 12 万~90 万字符之间（未精确二分）。`push.py` 里因此只对 2 万字符做软提示、对 800KB 体积做兜底，最终以接口的 `45002` 为准。
- 反过来说：`45002` ≠ "字符数超了"，是体积问题，精简行内样式（例如把重复的 `font-family`、`word-break` 提到外层 `<section>` 靠继承生效）才是解法。

探测脚本：`tools/probe_content_limit.py`（探针草稿跑完自动删除）。

## 坑 4：`draft/get` 回读时 `<img src>` 一定变成 `data-src`——这是正常的，别去"修"

回读草稿会发现正文里的图片成了 `<img data-src="https://mmbiz.qpic.cn/..." style="...">`，**没有 `src`**。

2026-09-28 四组对照实测（`tools/probe_img_rewrite.py`），提交什么写法都一样被改写：

| 提交写法 | 回读结果 |
|---|---|
| `<img src="...">` | 变成 `data-src` |
| `<img class="rich_pages wxw-img" data-ratio data-w src="...">` | 变成 `data-src`（其余属性保留） |
| `<p><img src="..."></p>` | 变成 `data-src` |
| `<img data-src="...">` | 保持 `data-src` |

结论：这是**服务端的固有改写**，微信自家编辑器产出的图片标记同样是 `data-src`，前端渲染时再由 JS 回填 `src`。
**不要**为此去改代码、也不要加 `data-ratio` 之类的"微信私有属性"试图保留 `src`，没有用。校验图片是否成功，看 `data-src` 是不是 `mmbiz.qpic.cn` 即可。

## 账号限制

当前账号 `wx75607d3029aa9cad` 是**未认证号**：`draft/*` 可用，`freepublish/*` 返回 **48001**。
所以"推送到公众号"的终点是**草稿箱**，群发必须人工在公众号后台点。**不要对用户说"已发布"**。换账号后先跑 `freepublish/batchget` 确认权限。

## 常见报错对照

| errcode | 含义 | 处理 |
|---|---|---|
| `45003` | title 超限 | 按转义长度截到 126 |
| `45004` | digest 超限 | 按转义长度截到 240 |
| `45002` | content 体积超限（**与字符数无关**） | 精简重复的行内样式，别去删正文 |
| `45110` | author 超限 | 省略 author 字段 |
| `40007` | invalid media_id | 检查 thumb_media_id 是否完整（64 字符） |
| `48001` | 接口无权限 | 未认证号，只能走草稿箱 |
| `40001` | token 失效 | 删 `~/.workbuddy/config/.wechat-token.json` 重取 |
| `40164` | IP 不在白名单 | 去公众号后台加当前出口 IP |
| 无报错但显示 `\uXXXX` | 发送时 `ensure_ascii=True` | 见坑 1 |

## 清理纪律

探测和调试会往草稿箱塞测试稿。**跑完必须清干净**，并且**只删自己建的**：

1. 先 `list_drafts.py` 看清现状（会打印 media_id 和真实标题）
2. 用 `cleanup_probes.py` **先不带参数预览**，它只列清单、不删任何东西
3. 确认阈值不会碰到用户的草稿后，`cleanup_probes.py --before <update_time> --yes`
4. 删完再 `list_drafts.py` 复核一次

**绝对不要**硬编码时间阈值后就跑——阈值会随新草稿产生而失效，可能误删用户后来建的稿子。用户原有的草稿一律不动；拿不准就先问。

**也不要盲目 import 这些脚本做冒烟测试**：`push.py` / `cleanup_probes.py` / `experiment_encoding.py` 现在都有 `if __name__ == "__main__"` 保护，但 `probe_limits.py`、`experiment_encoding.py` 这类脚本**一旦真的执行就会往草稿箱建稿**。要测就测 `--help` 或 `--dry-run`。


## 凭证维护

凭证在 `~/.workbuddy/config/wechat-draft.env`（**故意放在 skill 目录之外**，skill 可以放心分享/上传）。
换账号就改这个文件；也可用环境变量 `WECHAT_DRAFT_ENV` 指向别的路径。

**任何情况下不要把 AppID / AppSecret 写进文章、文档、代码或共享产物。**

## 换配色 / 主题时的注意

正文 HTML 必须先过一遍排版器输出**全行内样式**再推送。已经有 `<style>` 块的 HTML 直接推会丢样式。
