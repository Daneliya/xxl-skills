#!/usr/bin/env python3
"""列出所有草稿；带 --delete 时可批量删除指定 media_id。"""
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

import config  # noqa: E402
from wechat import WeChat  # noqa: E402

wx = WeChat(config.APPID, config.APPSECRET, token_cache=config.TOKEN_CACHE)

if "--delete" in sys.argv:
    ids = sys.argv[sys.argv.index("--delete") + 1:]
    for mid in ids:
        try:
            wx.draft_delete(mid)
            print(f"[已删除] {mid}")
        except Exception as e:
            print(f"[删除失败] {mid}  {e}")
    print()

items = []
offset = 0
while True:
    res = wx.draft_batchget(offset, 20, no_content=1)
    batch = res.get("item", [])
    items.extend(batch)
    if len(batch) < 20:
        break
    offset += 20

print(f"草稿总数: {len(items)}")
for i, it in enumerate(items):
    news = it.get("content", {}).get("news_item", [{}])
    title = news[0].get("title") if news else "?"
    print(f"{i:>3}  {it.get('update_time')}  {it.get('media_id')}  {title!r}")
