# Responses

A live TikTok video request was verified on 2026-10-25. The following is a deliberately shortened structural example, not a complete fixture or a guarantee that all fields always exist:

```json
{"status":"ok","rate_limit_reached":false,"limits_info":{"requests_count":1,"requests_limit":100},"tiktok":{"status_code":0,"aweme_detail":{"aweme_id":"7106855913906081070"}}}
```

The numeric limits above are illustrative. Live user and comment responses were also checked: user data is under `tiktok.user`; comments are under `tiktok.comments`, with `cursor` and `has_more` on `tiktok`. Fields can be null or absent. Preserve the upstream envelope to inspect application errors and quota status.

A live Instagram profile request was also verified on 2026-10-25. Public profile data is in `ig` (not `data`):

```json
{"status":"ok","ig":{"pk":"5821462185","username":"apple","is_private":false,"is_verified":true},"timestamp":1792879723}
```

This is a shortened structural example. The API may return `pk` as a JSON integer; retain IDs as strings in your application. Quota fields may be absent when the response is served from cache.

For downloads, check the content type and handle binary bodies without parsing JSON. If a route responds with a redirect, validate the destination and download separately without forwarding `license_key`.
