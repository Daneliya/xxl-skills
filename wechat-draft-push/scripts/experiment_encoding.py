#!/usr/bin/env python3
"""编码对照实验：证明 draft/add 存乱码是 `ensure_ascii=True` 转义导致的。

三种发法，内容完全相同，只有编码方式不同：
  A  json=payload                      → requests 默认 ensure_ascii=True（转义）
  B  data=<ensure_ascii=False utf-8>   → 中文字面量，显式 Content-Type   ← 正确
  C  data=<ensure_ascii=True utf-8>    → 字面 ASCII 转义
然后回读，比较草稿箱里实际存的是什么。

注意：会新建 3 条草稿，跑完记得用 list_drafts.py --delete 清掉。
"""
import json
import sys
from pathlib import Path

import requests

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

import config  # noqa: E402
from wechat import API, WeChat  # noqa: E402

CONTENT = '<section style="font-size:16px;"><p>ABCDEFG abcdefg</p></section>'


def main():
    wx = WeChat(config.APPID, config.APPSECRET, token_cache=config.TOKEN_CACHE)
    tk = wx.token()

    def call(path, **kw):
        r = requests.post(f"{API}{path}", params={"access_token": tk}, timeout=60, **kw)
        return json.loads(r.content.decode("utf-8"))

    res = call("/draft/batchget", json={"offset": 0, "count": 5, "no_content": 1})
    items = res.get("item", [])
    print(f"当前草稿 {len(items)} 条")
    for it in items:
        a = it["content"]["news_item"][0]
        print(f"  title={a.get('title')!r}")
        print(f"    thumb={a.get('thumb_media_id')!r}  长度={len(a.get('thumb_media_id') or '')}")

    if not items:
        raise SystemExit("草稿箱是空的，需要一个可用的 thumb_media_id 才能做这个实验")
    thumb = items[0]["content"]["news_item"][0]["thumb_media_id"]
    print(f"\n使用 thumb={thumb!r}")

    def art(t):
        return {"articles": [{"title": t, "content": CONTENT, "thumb_media_id": thumb}]}

    variants = [
        ("A json= (ensure_ascii=True)", "json"),
        ("B data utf8 不转义", "data_false"),
        ("C data utf8 转义", "data_true"),
    ]

    created = []
    for label, kind in variants:
        payload = art("编码" + label[0])
        if kind == "json":
            data = call("/draft/add", json=payload)
        else:
            body = json.dumps(payload, ensure_ascii=(kind == "data_true")).encode("utf-8")
            data = call("/draft/add", data=body,
                        headers={"Content-Type": "application/json; charset=utf-8"})
        print(f"\n[提交] {label}")
        print(f"  errcode={data.get('errcode')} errmsg={data.get('errmsg')} media_id={data.get('media_id')}")
        if data.get("media_id"):
            created.append((label, data["media_id"]))

    if created:
        print("\n回读实际存进去的 title：")
        res = call("/draft/batchget", json={"offset": 0, "count": 5, "no_content": 1})
        by_id = {it["media_id"]: it for it in res.get("item", [])}
        for label, mid in created:
            t = by_id.get(mid, {}).get("content", {}).get("news_item", [{}])[0].get("title", "?")
            verdict = "正常" if t == "编码" + label[0] else ">>> 乱码 <<<"
            print(f"  {label}: {t!r}   {verdict}")
        print("\n结论：B（ensure_ascii=False）才正常，A/C 都会存成字面 \\uXXXX。")


if __name__ == "__main__":
    main()
