# jsonscraper python SDK — Instagram API and TikTok API

Official, composable clients for [Instagram API](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=jsonscraper-python&utm_content=readme) and [TikTok API](https://jsonscraper.com/services/tiktok-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=jsonscraper-python&utm_content=readme). Access public profiles, media, comments, followers, hashtags, search, and other documented endpoints without maintaining a scraper.

Requirements: **Python 3.10+**. Server-side use only. **151 unique GET routes** from the published Postman collections, with named methods and a generic request method for new routes.

## Install

Clone this repository, then run:

```sh
python -m pip install .
# Or directly from a release:
python -m pip install "git+https://github.com/jsonscraper/jsonscraper-python.git@v0.1.0"
```

This initial release supports installation from GitHub or a local checkout. Package names are prepared; availability in PyPI, npm, Packagist, Maven Central, and NuGet is a separate release step. Do not assume a package is registered there.

## API access, license key, and current pricing

The SDK source is **MIT-licensed**. API usage requires a separate commercial license for the selected product. Obtain your key and check current plans, quotas, and purchase options on the [Instagram product page](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=jsonscraper-python&utm_content=pricing) or [TikTok product page](https://jsonscraper.com/services/tiktok-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=jsonscraper-python&utm_content=pricing). Follow **Get Access** there. We link to current prices instead of copying amounts that can become outdated.

Configure keys as environment variables; never commit them:

```sh
export JSONSCRAPER_INSTAGRAM_LICENSE_KEY='your-instagram-license-key'
export JSONSCRAPER_TIKTOK_LICENSE_KEY='your-tiktok-license-key'
```

## Quick start

```python
import os
from jsonscraper import Instagram, TikTok, APIError

ig = Instagram(os.environ["JSONSCRAPER_INSTAGRAM_LICENSE_KEY"], timeout=30, retries=1)
profile = ig.v1_user_by_username(username="apple", cache_timeout=60)
print(profile)

tiktok = TikTok(os.environ["JSONSCRAPER_TIKTOK_LICENSE_KEY"])
video = tiktok.get_video_by_id(video_id="7106855913906081070", cache_timeout=60)
print(video["tiktok"]["aweme_detail"]["aweme_id"])
```

Both keys are needed to run both product examples. You can use either client independently. Every request accepts the query parameters documented in [the endpoint reference](docs/endpoints.md), including optional cache and cursor controls. Parameter names and API paths stay identical to Postman. Python/JavaScript/PHP/Java named methods use snake_case; Go/C# use PascalCase.

## Configuration and errors

- Instagram default base URL: `https://ig.jsonscraper.com`.
- TikTok default base URL: `https://tiktok.evelode.com`. Older collections mention `/tiktok-api`; the current product page and live smoke test use the root URL.
- Configure base URL, timeout, retries and default `cache_timeout` through client options. Timeouts are seconds, except Node.js which uses milliseconds; Go uses `time.Duration`, Java uses `Duration`, and C# uses `TimeSpan`.
- Retries default to **0**. Opt in to at most 5 retries for HTTP 429, 502, 503 and 504; numeric `Retry-After` is capped at 60 seconds, otherwise bounded exponential backoff applies. HTTP-date `Retry-After` falls back to backoff. Each retry may count towards your API quota. Total time can exceed one request timeout.
- Authentication uses the API's `license_key` query parameter. The configured key overrides any per-request key. Redirects are disabled; transport errors contain no request URL or key. Keep request URLs out of application/proxy logs.
- HTTP errors expose the status and retry information. HTTP 200 does **not** guarantee application success: check the response `status`, `rate_limit_reached`, and the product payload's status fields.
- Unknown fields are preserved. IDs should be passed as strings, never converted to floating point. Python preserves integer precision; PHP uses `JSON_BIGINT_AS_STRING`; Go's `Decode` uses `json.Number`; Java returns raw bytes for your chosen JSON library; C# supports raw bytes and `JsonDocument`.
- JSON routes return the upstream envelope. Binary download routes return bytes (PHP: string); no SDK follows a download redirect automatically. Handle redirects explicitly after validating the destination without forwarding your license key.
- Cancellation: Go accepts a context, Java supports thread interruption, and C# accepts `CancellationToken`. For other languages use bounded request timeouts.

## Pagination and caching

Pagination differs between endpoints. Read `cursor`, `max_cursor`, `has_more`, and response metadata from the endpoint you use, then pass the returned cursor unchanged to the next call. Stop on `has_more == false/0`, a repeated cursor, or your own page/request budget. The SDK does not guess cursor fields or automatically consume your quota.

`cache_timeout=60` requests server-side caching for 60 seconds. Set `0` to disable it. See the product's current quota and fair-use terms; the SDK does not cache API responses locally.

## Documentation and examples

- [All named methods, API paths and query parameters](docs/endpoints.md)
- [Response envelopes and verified sample shapes](docs/responses.md)
- [Instagram Postman collection](https://www.postman.com/jsonscraper/workspace/jsonscraper/collection/52903714-fe84d353-0a19-431f-a39d-1c2640d96fb0)
- [TikTok Postman collection](https://www.postman.com/evelode/workspace/evelode/collection/24862082-d886cc87-4267-4e0c-b57a-2d083add50ad)
- [Support and contacts](https://jsonscraper.com/contacts?utm_source=github&utm_medium=sdk&utm_campaign=jsonscraper-python&utm_content=support)

## Privacy and affiliation

The SDK sends requests only to the configured API endpoint and contains no installation, usage, or conversion telemetry. README links include campaign parameters so jsonscraper can measure website referrals. Website attribution respects Do Not Track and Global Privacy Control. Third-party platform names identify compatibility; jsonscraper is not affiliated with Instagram, Meta, or TikTok.

## Development

Run `python3 tests/contract.py` from the repository root. This exercises the real client against a local HTTP server without credentials or paid API requests. A GitHub Actions workflow template is included in `docs/github-actions.yml`. To enable automatic checks, copy it to `.github/workflows/test.yml` with a token that has the `workflow` permission. Live smoke tests require your own environment keys and may consume quota.

Version 0.1.0 is an initial release. See [CHANGELOG.md](CHANGELOG.md). Report reproducible SDK issues on GitHub without credentials or sensitive payloads.
