#!/usr/bin/env python3
"""微信公众号接口封装：token 缓存 / 正文图片上传 / 永久素材 / 草稿箱。

接口来源（官方文档已验证）：
  获取 token          GET  /cgi-bin/token
  正文图片转存         POST /cgi-bin/media/uploadimg        （不占永久素材配额）
  上传永久图片素材     POST /cgi-bin/material/add_material  （type=image）
  草稿数              GET  /cgi-bin/draft/count
  新建草稿            POST /cgi-bin/draft/add
  草稿列表            POST /cgi-bin/draft/batchget
"""
import json
import time
from pathlib import Path

import requests

API = "https://api.weixin.qq.com/cgi-bin"
TOKEN_EARLY_REFRESH = 300


class WeChatError(RuntimeError):
    def __init__(self, api, errcode, errmsg):
        super().__init__(f"[{api}] errcode={errcode} errmsg={errmsg}")
        self.api = api
        self.errcode = errcode
        self.errmsg = errmsg


class WeChat:
    def __init__(self, appid, secret, token_cache=".token.json", timeout=60):
        if not appid or not secret:
            raise ValueError("缺少 AppID / AppSecret，请检查 .env")
        self.appid = appid
        self.secret = secret
        self.timeout = timeout
        self.token_cache = Path(token_cache)
        self._token = None

    # ---------- 基础 ----------
    def token(self, force=False):
        now = time.time()
        if not force and self._token and now < self._token[1] - TOKEN_EARLY_REFRESH:
            return self._token[0]
        if not force and self.token_cache.exists():
            try:
                data = json.loads(self.token_cache.read_text(encoding="utf-8"))
                ok = data.get("appid") == self.appid and now < data.get("expires_at", 0) - TOKEN_EARLY_REFRESH
                if ok:
                    self._token = (data["access_token"], data["expires_at"])
                    return self._token[0]
            except Exception:
                pass
        r = requests.get(
            f"{API}/token",
            params={"grant_type": "client_credential", "appid": self.appid, "secret": self.secret},
            timeout=self.timeout,
        )
        data = self._parse(r)
        if "access_token" not in data:
            raise WeChatError("token", data.get("errcode"), data.get("errmsg"))
        expires_at = now + int(data.get("expires_in", 7200)) - 60
        self._token = (data["access_token"], expires_at)
        try:
            self.token_cache.write_text(
                json.dumps(
                    {"appid": self.appid, "access_token": data["access_token"], "expires_at": expires_at},
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
        except Exception:
            pass
        return self._token[0]

    @staticmethod
    def _parse(resp):
        """显式按 UTF-8 解码响应体。

        微信返回的 Content-Type 经常不带 charset，直接 res.json() 会让 requests
        用 apparent_encoding 猜编码，中文会被猜成 latin-1 而显示成乱码。
        """
        try:
            return json.loads(resp.content.decode("utf-8"))
        except Exception:
            return {"errcode": "non_json", "errmsg": f"非 JSON 响应: {resp.content[:200]!r}"}

    @staticmethod
    def _check(api, data):
        if isinstance(data, dict) and data.get("errcode"):
            raise WeChatError(api, data.get("errcode"), data.get("errmsg"))
        return data

    def _request(self, method, path, payload=None, params=None):
        """所有请求走这里。

        关键：**必须用 data=<utf-8 bytes> + ensure_ascii=False 发中文**。
        微信的 draft/material 接口不解 \\uXXXX 转义，用 requests 的 json= 参数
        （默认 ensure_ascii=True）会把中文转义后发出去，微信就当字面量存进草稿箱，
        草稿箱里显示成 \\u516c\\u4f17... 这种乱码。
        """
        params = dict(params or {})
        params["access_token"] = self.token()
        url = f"{API}{path}"
        if method == "GET":
            resp = requests.get(url, params=params, timeout=self.timeout)
        else:
            body, headers = None, {}
            if payload is not None:
                body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
                headers["Content-Type"] = "application/json; charset=utf-8"
            resp = requests.post(url, params=params, data=body, headers=headers, timeout=self.timeout)
        return self._check(path, self._parse(resp))

    def get(self, path, params=None):
        return self._request("GET", path, params=params)

    def post(self, path, json_body=None, params=None):
        return self._request("POST", path, payload=json_body, params=params)

    # ---------- 素材 / 图片 ----------
    def upload_content_image(self, image_path):
        """上传图文消息内的图片，返回可在正文里直接使用的 URL。"""
        p = Path(image_path)
        with p.open("rb") as f:
            files = {"media": (p.name, f)}
            r = requests.post(
                f"{API}/media/uploadimg",
                params={"access_token": self.token()},
                files=files,
                timeout=self.timeout,
            )
        data = self._check("media/uploadimg", self._parse(r))
        if not data.get("url"):
            raise WeChatError("media/uploadimg", "no_url", str(data))
        return data["url"]

    def add_permanent_image(self, image_path):
        """上传图片永久素材，返回 {media_id, url}。封面 thumb_media_id 用这个。"""
        p = Path(image_path)
        with p.open("rb") as f:
            files = {"media": (p.name, f)}
            r = requests.post(
                f"{API}/material/add_material",
                params={"access_token": self.token(), "type": "image"},
                files=files,
                timeout=self.timeout,
            )
        data = self._check("material/add_material", self._parse(r))
        if not data.get("media_id"):
            raise WeChatError("material/add_material", "no_media_id", str(data))
        return data

    def material_count(self):
        return self.get("/material/get_materialcount")

    def list_materials(self, type="image", offset=0, count=1):
        return self.post("/material/batchget_material", {"type": type, "offset": offset, "count": count})

    # ---------- 草稿 ----------
    def draft_count(self):
        return self.get("/draft/count")

    def draft_add(self, articles):
        return self.post("/draft/add", {"articles": articles})

    def draft_batchget(self, offset=0, count=20, no_content=1):
        return self.post("/draft/batchget", {"offset": offset, "count": count, "no_content": no_content})

    def draft_get(self, media_id):
        return self.post("/draft/get", {"media_id": media_id})

    def draft_delete(self, media_id):
        return self.post("/draft/delete", {"media_id": media_id})
