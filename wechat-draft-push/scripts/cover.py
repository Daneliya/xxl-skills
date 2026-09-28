#!/usr/bin/env python3
"""用 Pillow 确定性生成封面（文字本地渲染，避免 AI 出图把中文画错）。"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simhei.ttf",
]


def _font(size):
    for p in FONT_CANDIDATES:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def _wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=font) <= max_w:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def make_cover(title, out_path, subtitle=None, size=(900, 383),
               bg="#101820", fg="#F2F5F7", sub_fg="#9FB0BE", accent="#3BA37E"):
    w, h = size
    img = Image.new("RGB", size, bg)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 8, h], fill=accent)

    f_title = _font(52)
    lines = _wrap(d, title, f_title, w - 128)
    line_h = 68
    block_h = len(lines) * line_h + (34 if subtitle else 0)
    y = (h - block_h) / 2
    for line in lines:
        d.text((64, y), line, font=f_title, fill=fg)
        y += line_h
    if subtitle:
        d.text((64, y + 6), subtitle, font=_font(22), fill=sub_fg)

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "JPEG", quality=92)
    return out_path
