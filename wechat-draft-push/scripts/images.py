#!/usr/bin/env python3
"""把正文 HTML 里的图片统一转存到微信，并替换 <img src>。

微信会过滤 content 里的外链图片，base64 也不认，所以这一步是必须的。
处理三类 src：data URI / 本地路径 / 外链。
"""
import base64
import hashlib
import re
from pathlib import Path

import requests

IMG_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc\s*=\s*)(["\'])(.*?)\2', re.I | re.S)
DATA_URI_RE = re.compile(r"^data:image/([a-zA-Z0-9.+-]+);base64,(.+)$", re.S)
WECHAT_IMAGE_HOSTS = ("mmbiz.qpic.cn", "mmbiz.qlogo.cn", "mmbiz.qpic.cn/")

MIME_EXT = {
    "jpeg": ".jpg", "jpg": ".jpg", "pjpeg": ".jpg",
    "png": ".png", "gif": ".gif", "webp": ".webp", "bmp": ".bmp",
}


def _ext_from_mime(mime):
    mime = (mime or "").lower()
    for key, ext in MIME_EXT.items():
        if key in mime:
            return ext
    return ".png"


def _is_wechat_url(src):
    return any(h in src for h in WECHAT_IMAGE_HOSTS)


def localize_images(html, upload_fn, tmp_dir, base_dir=None, limit_mb=1.0, logger=print):
    """返回 (new_html, stats)。upload_fn(本地文件路径) -> 微信 URL。"""
    tmp_dir = Path(tmp_dir)
    tmp_dir.mkdir(parents=True, exist_ok=True)
    base_dir = Path(base_dir or ".")
    stats = {"found": 0, "uploaded": 0, "skipped": 0, "failed": 0, "oversize": 0}

    def repl(m):
        stats["found"] += 1
        prefix, quote, src = m.group(1), m.group(2), m.group(3).strip()
        try:
            if src.startswith("//"):
                src = "https:" + src
            dm = DATA_URI_RE.match(src)
            if dm:
                ext = _ext_from_mime(dm.group(1))
                raw = base64.b64decode(dm.group(2))
                path = tmp_dir / f"inline-{hashlib.md5(raw).hexdigest()[:12]}{ext}"
                path.write_bytes(raw)
            elif src.startswith(("http://", "https://")):
                if _is_wechat_url(src):
                    stats["skipped"] += 1
                    return m.group(0)
                r = requests.get(src, timeout=60)
                r.raise_for_status()
                ext = _ext_from_mime(r.headers.get("Content-Type", ""))
                path = tmp_dir / f"remote-{hashlib.md5(src.encode()).hexdigest()[:12]}{ext}"
                path.write_bytes(r.content)
            else:
                raw_path = Path(src[8:] if src.startswith("file:///") else src)
                path = raw_path if raw_path.is_absolute() else (base_dir / raw_path)
                if not path.exists():
                    stats["failed"] += 1
                    logger(f"    ! 本地图片不存在，保留原 src: {src}")
                    return m.group(0)

            size_mb = path.stat().st_size / 1024 / 1024
            if size_mb > limit_mb:
                stats["oversize"] += 1
                stats["failed"] += 1
                logger(f"    ! 超过 {limit_mb}MB（{size_mb:.2f}MB），保留原 src: {path.name}")
                return m.group(0)

            url = upload_fn(str(path))
            stats["uploaded"] += 1
            logger(f"    转存 OK  {path.name}  ->  {url[:64]}...")
            return f"{prefix}{quote}{url}{quote}"
        except Exception as e:
            stats["failed"] += 1
            logger(f"    ! 转存失败，保留原 src: {src[:50]}  ({e})")
            return m.group(0)

    return IMG_SRC_RE.sub(repl, html), stats
