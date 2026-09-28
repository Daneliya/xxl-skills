#!/usr/bin/env python3
"""读取公众号凭证配置。

查找顺序（先命中先用）：
  1. 环境变量 WECHAT_DRAFT_ENV 指向的文件
  2. ~/.workbuddy/config/wechat-draft.env   <- 推荐放这里
     （故意放在 skill 目录**之外**：skill 可以放心分享/上传，凭证不会跟着走）
  3. 本脚本同目录的 .env

文件格式：每行 KEY=VALUE，`#` 开头为注释。

需要的键：
  WECHAT_APPID=wx................
  WECHAT_APPSECRET=..............
  WECHAT_DEFAULT_AUTHOR=           可选，留空表示不填作者
  WECHAT_TOKEN_CACHE=              可选，access_token 缓存路径
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
USER_CONFIG_DIR = Path.home() / ".workbuddy" / "config"

CANDIDATES = []
if os.environ.get("WECHAT_DRAFT_ENV"):
    CANDIDATES.append(Path(os.environ["WECHAT_DRAFT_ENV"]))
CANDIDATES.append(USER_CONFIG_DIR / "wechat-draft.env")
CANDIDATES.append(HERE / ".env")

ENV_PATH = next((p for p in CANDIDATES if p.exists()), None)


def _load(path):
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


if ENV_PATH:
    _load(ENV_PATH)

APPID = os.environ.get("WECHAT_APPID", "")
APPSECRET = os.environ.get("WECHAT_APPSECRET", "")
DEFAULT_AUTHOR = os.environ.get("WECHAT_DEFAULT_AUTHOR", "")

_cache = os.environ.get("WECHAT_TOKEN_CACHE")
TOKEN_CACHE = Path(_cache) if _cache else (USER_CONFIG_DIR / ".wechat-token.json")

if not APPID or not APPSECRET:
    raise SystemExit(
        "没找到公众号凭证。\n"
        f"请把 AppID / AppSecret 写进：{USER_CONFIG_DIR / 'wechat-draft.env'}\n"
        "内容形如：\n"
        "  WECHAT_APPID=wx................\n"
        "  WECHAT_APPSECRET=..............\n"
        "（或用环境变量 WECHAT_DRAFT_ENV 指向别的文件）"
    )
