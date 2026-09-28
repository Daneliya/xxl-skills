#!/usr/bin/env python3
"""清理探测/调试产生的草稿。

**故意不做自动判断**：先不带参数跑一遍看清单和 update_time，
确认哪些是自己建的、不会碰到用户原有草稿，再显式指定时间阈值删除。

用法:
  python cleanup_probes.py                            # 只预览：列出全部草稿 + update_time
  python cleanup_probes.py --before 1790562000        # 预览：将删除该时间之后的草稿
  python cleanup_probes.py --before 1790562000 --yes  # 真删
"""
import argparse
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

import config  # noqa: E402
from wechat import WeChat  # noqa: E402


def fetch_all(wx):
    items, offset = [], 0
    while True:
        batch = wx.draft_batchget(offset, 20, no_content=1).get("item", [])
        items.extend(batch)
        if len(batch) < 20:
            break
        offset += 20
    return items


def title_of(it):
    news = it.get("content", {}).get("news_item", [{}])
    return news[0].get("title", "?") if news else "?"


def main():
    ap = argparse.ArgumentParser(description="清理调试草稿（先预览再删）")
    ap.add_argument("--before", type=int,
                    help="删除 update_time 大于该值的草稿。不给则只预览、不删任何东西")
    ap.add_argument("--yes", action="store_true", help="真正执行删除")
    args = ap.parse_args()

    wx = WeChat(config.APPID, config.APPSECRET, token_cache=config.TOKEN_CACHE)
    items = fetch_all(wx)

    print(f"当前草稿 {len(items)} 条：")
    for it in sorted(items, key=lambda x: x.get("update_time", 0)):
        print(f"  update_time={it.get('update_time')}  {title_of(it)!r}")
        print(f"    media_id={it['media_id']}")

    if args.before is None:
        print("\n未指定 --before，没有删除任何东西。")
        print("确认清单后，用 --before <update_time> 指定阈值（只删比它新的），再加 --yes 执行。")
        print("注意：阈值一定要避开用户自己建的草稿。")
        return

    targets = [it for it in items if it.get("update_time", 0) > args.before]
    print(f"\nupdate_time > {args.before} 的共 {len(targets)} 条：")
    for it in targets:
        print(f"  [将删除] {it.get('update_time')}  {title_of(it)!r}")
    print(f"将保留 {len(items) - len(targets)} 条（其余原有草稿不动）")

    if not args.yes:
        print("\n预览模式，未执行。确认无误后加 --yes。")
        return

    ok = 0
    for it in targets:
        try:
            wx.draft_delete(it["media_id"])
            ok += 1
        except Exception as e:
            print(f"  删除失败 {it['media_id']}: {e}")
    print(f"\n已删除 {ok}/{len(targets)} 条")
    print("剩余草稿数:", wx.draft_count())


if __name__ == "__main__":
    main()
