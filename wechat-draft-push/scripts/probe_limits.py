#!/usr/bin/env python3
"""重跑字段上限探测（微信改规则时可复跑校验）。

实测结论（2026-09-28）：
  微信是按 **JSON 转义后的长度** 校验 title / digest / author，不是文档写的"字数"。
  `json.dumps(s, ensure_ascii=True)` 后一个中文字 = `\\uXXXX` = 6 个长度单位。
  实测边界：
    title  转义 ≤126 → 约 21 个中文字 / 126 个 ASCII
    digest 转义 ≤240 → 40 个中文字 / 240 个 ASCII
    author 转义 ≤16  → **仅 2 个中文字** / 16 个 ASCII
  反证：若按"字节"算，author「2中文+5英文」= 11 字节应通过，实际失败 → 排除字节假设。

用法: python probe_limits.py [承接用的thumb_media_id]
注意：每成功一次会新建一条草稿，跑完用 cleanup_probes.py 清理。
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

import config  # noqa: E402
from wechat import WeChat, WeChatError  # noqa: E402

CONTENT = '<section style="font-size:16px;"><p>字段上限探测</p></section>'


def esc(s):
    return len(json.dumps(s, ensure_ascii=True)) - 2


def main():
    thumb = sys.argv[1] if len(sys.argv) > 1 else None
    if not thumb:
        raise SystemExit("请传入一个可用的永久素材 media_id 当封面")
    wx = WeChat(config.APPID, config.APPSECRET, token_cache=config.TOKEN_CACHE)

    cases = [
        # title：转义 126 是边界
        ("title 20中文（转义120）", {"title": "中" * 20}),
        ("title 21中文（转义126）", {"title": "中" * 21}),
        ("title 22中文（转义132）", {"title": "中" * 22}),
        ("title 126英文", {"title": "a" * 126}),
        ("title 127英文", {"title": "a" * 127}),
        # digest：转义 240 是边界
        ("digest 39中文（转义234）", {"digest": "测" * 39}),
        ("digest 40中文（转义240）", {"digest": "测" * 40}),
        ("digest 41中文（转义246）", {"digest": "测" * 41}),
        ("digest 240英文", {"digest": "x" * 240}),
        ("digest 241英文", {"digest": "x" * 241}),
        # author：转义 16 是边界
        ("author 2中文（转义12）", {"author": "测" * 2}),
        ("author 3中文（转义18）", {"author": "测" * 3}),
        ("author 16英文", {"author": "A" * 16}),
        ("author 17英文", {"author": "A" * 17}),
        ("author 2中文+4英文（转义16）", {"author": "测试ABCD"}),
        ("author 2中文+5英文（转义17）", {"author": "测试ABCDE"}),
    ]

    for label, extra in cases:
        art = {"title": "探测", "content": CONTENT, "thumb_media_id": thumb}
        art.update(extra)
        try:
            wx.draft_add([art])
            print(f"[OK ] {label}")
        except WeChatError as e:
            print(f"[ERR] {label}  -> {e.errcode}")

    print()
    print("草稿总数:", wx.draft_count())


if __name__ == "__main__":
    main()
