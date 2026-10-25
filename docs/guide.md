# Instagram Scraper API for Python

[![Latest release](https://img.shields.io/github/v/tag/jsonscraper/instagram-api-python?label=release&style=flat-square)](https://github.com/jsonscraper/instagram-api-python/tags)
[![Python requirements](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white&style=flat-square)](#1-install)
[![Last commit](https://img.shields.io/github/last-commit/jsonscraper/instagram-api-python?style=flat-square)](https://github.com/jsonscraper/instagram-api-python/commits)
[![MIT license](https://img.shields.io/github/license/jsonscraper/instagram-api-python?style=flat-square)](../LICENSE)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/jsonscraper/workspace/jsonscraper/collection/52903714-fe84d353-0a19-431f-a39d-1c2640d96fb0)


Official Python client for the [jsonscraper Instagram Scraper API](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=instagram-api-python&utm_content=readme). **97 documented GET routes**, simple installation, configurable requests, working examples, and responses ready for your application.

![From API access to your first JSON response](quickstart.svg)

**[Get an API key](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=instagram-api-python&utm_content=get_access) · [Current pricing](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=instagram-api-python&utm_content=pricing#pricing) · [Endpoint reference](endpoints.md) · [Runnable examples](../examples) · [Postman](https://www.postman.com/jsonscraper/workspace/jsonscraper/collection/52903714-fe84d353-0a19-431f-a39d-1c2640d96fb0)**

## Navigation

- [What you can build](#what-you-can-build)
- [Installation](#1-install)
- [License key and access](#2-get-api-access)
- [First request](#3-make-your-first-request)
- [Available methods](#available-methods)
- [Request examples](#more-request-examples)
- [Complete example catalogue](#complete-request-example-catalogue)
- [Endpoint reference](endpoints.md)
- [Configuration](#configuration)
- [Errors, pagination and caching](#errors-pagination-and-caching)
- [FAQ](#faq)
- [Development and releases](#development-and-releases)
- [Privacy](#privacy)

## What you can build

Read public profiles; retrieve media, reels and comments; explore hashtag/location/search routes; build analytics, monitoring and data integrations.

This repository contains the **Instagram SDK only**. It calls the hosted jsonscraper API; you do not need to maintain browser automation, platform sessions or a scraping server.

## 1. Install

Requirements: **Python 3.10+**.

```sh
python -m pip install "git+https://github.com/jsonscraper/instagram-api-python.git@0.1.0"
```

The GitHub installation above works independently of package registry registration. A public PyPI/npm/Packagist listing is a separate release step; this README does not claim those listings already exist.

To develop from a checkout, clone this repository and install its dependencies using the package manager for this SDK.

## 2. Get API access

The SDK source uses the **MIT license**. Hosted API usage requires a separate **Instagram API license** with its own quota and validity period.

1. Open the [Instagram product page](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=instagram-api-python&utm_content=onboarding).
2. Check the current plans and follow **Get Access** to obtain your license key.
3. Save the key on your server as an environment variable:

```sh
export JSONSCRAPER_INSTAGRAM_LICENSE_KEY='your-license-key'
```

Current prices and limits are linked from the product page rather than copied into this README. That keeps the purchase information current. Do not commit your key or put it in browser/mobile frontend code.

## 3. Make your first request

```python
import os
from jsonscraper_instagram import Instagram, APIError

client = Instagram(os.environ["JSONSCRAPER_INSTAGRAM_LICENSE_KEY"], timeout=30, retries=1)
try:
    response = client.v1_user_by_username(username="apple", cache_timeout=60)
    if response.get("status") != "ok":
        raise RuntimeError("The API returned an application error")
    print(response["ig"])
except APIError as error:
    print(f"HTTP {error.status}; check your key, quota, or parameters")
```

**[Open the runnable version](../examples/quickstart.py)**. The example uses a public account and a short server-side cache. You can replace the account with one relevant to your project. A licensed live request may consume quota.

The profile response follows this shape (shortened; fields can be absent or null):

```json
{
  "status": "ok",
  "ig": {
    "pk": "5821462185",
    "username": "apple",
    "is_private": false,
    "is_verified": true
  }
}
```

**[Response handling guide](responses.md)** explains the envelope, application errors and identifiers. Profile responses were verified against the live API on 2026-10-25.

## Available methods

97 named API methods are available. Start with these commonly used requests, then open the [complete method reference](endpoints.md) for every method and its parameters.

| Use case | SDK method | Query parameters |
| --- | --- | --- |
| Get user info by username (by ID is faster) | `v1_user_by_username()` | `username`, `cache_timeout` |
| Get user info by ID | `v1_user_by_id()` | `id`, `cache_timeout` |
| Get posts (chunked) | `v1_user_medias_chunk()` | `user_id`, `end_cursor`, `cache_timeout` |
| Get user stories by ID | `v1_user_stories()` | `user_id`, `amount`, `force`, `cache_timeout` |
| Get media info by shortcode | `v1_media_by_code()` | `code`, `cache_timeout` |
| Get media comments (chunked) | `v1_media_comments_chunk()` | `id`, `min_id`, `max_id`, `can_support_threading`, `cache_timeout` |
| Search users | `v1_search_users()` | `query`, `cache_timeout` |
| Search hashtags | `v1_search_hashtags()` | `query`, `cache_timeout` |

Each method is documented with a [complete runnable example](../examples/README.md). The transport preserves the full response envelope, including application status, payload and optional quota metadata.

## Find the request you need

The [endpoint reference](endpoints.md) lists every named SDK method, exact API path, query parameter and purpose. The [Postman collection](https://www.postman.com/jsonscraper/workspace/jsonscraper/collection/52903714-fe84d353-0a19-431f-a39d-1c2640d96fb0) contains current descriptions, parameter examples and endpoint groups.

Use the generic request method for newly added routes without waiting for an SDK release. Parameter names remain identical to Postman. For example, cache controls are always `cache_timeout`; platform IDs are passed as strings.

## More request examples

- [Read a media item](../examples/media.py) — `GET /v1/media/by/code`.
- [Search public users](../examples/search.py) — `GET /v1/search/users`.
- [Read a page of user media](../examples/feed.py) — `GET /v1/user/medias/chunk`.

These examples make one request each. They never loop automatically through your quota. For feed pagination, inspect the returned cursor and `has_more`, then pass the cursor back to the same endpoint.

## Complete request example catalogue

Every link opens a full program with parameters, authentication, timeout, errors and output handling. **[Running the examples](../examples/README.md)** explains the commands.

<details>
<summary>User · 33 examples</summary>

- [Get user info by ID](../examples/endpoints/v1_user_by_id.py) — `GET /v1/user/by/id`.
- [Get user info by username (by ID is faster)](../examples/endpoints/v1_user_by_username.py) — `GET /v1/user/by/username`.
- [Get user info by URL (by ID is faster)](../examples/endpoints/v1_user_by_url.py) — `GET /v1/user/by/url`.
- [Get info about user by ID](../examples/endpoints/v1_user_about.py) — `GET /v1/user/about`.
- [Get posts (chunked)](../examples/endpoints/v1_user_medias_chunk.py) — `GET /v1/user/medias/chunk`.
- [Get pinned posts](../examples/endpoints/v1_user_medias_pinned.py) — `GET /v1/user/medias/pinned`.
- [Get reels (chunked)](../examples/endpoints/v1_user_clips_chunk.py) — `GET /v1/user/clips/chunk`.
- [Get tagged (mentions) posts](../examples/endpoints/v1_user_tag_medias_chunk.py) — `GET /v1/user/tag/medias/chunk`.
- [Get user stories by ID](../examples/endpoints/v1_user_stories.py) — `GET /v1/user/stories`.
- [Get user stories by username (by ID is faster)](../examples/endpoints/v1_user_stories_by_username.py) — `GET /v1/user/stories/by/username`.
- [Get user highlights by ID](../examples/endpoints/v1_user_highlights.py) — `GET /v1/user/highlights`.
- [Get user highlights by username (by ID is faster)](../examples/endpoints/v1_user_highlights_by_username.py) — `GET /v1/user/highlights/by/username`.
- [Search in followers list by query (not working for legacy verified accounts)](../examples/endpoints/v1_user_search_followers.py) — `GET /v1/user/search/followers`.
- [Search in followings list by query (not working for legacy verified accounts)](../examples/endpoints/v1_user_search_following.py) — `GET /v1/user/search/following`.
- [Get user following (chunked)](../examples/endpoints/v1_user_following_chunk.py) — `GET /v1/user/following/chunk`.
- [Get user followers (chunked)](../examples/endpoints/v1_user_followers_chunk.py) — `GET /v1/user/followers/chunk`.
- [Get user info by ID](../examples/endpoints/v2_user_by_id.py) — `GET /v2/user/by/id`.
- [Get user info by username](../examples/endpoints/v2_user_by_username.py) — `GET /v2/user/by/username`.
- [Get user stories by ID](../examples/endpoints/v2_user_stories.py) — `GET /v2/user/stories`.
- [Get user stories by username](../examples/endpoints/v2_user_stories_by_username.py) — `GET /v2/user/stories/by/username`.
- [Get user reels by ID](../examples/endpoints/v2_user_clips.py) — `GET /v2/user/clips`.
- [Get user following list](../examples/endpoints/v2_user_following.py) — `GET /v2/user/following`.
- [Get user followers list](../examples/endpoints/v2_user_followers.py) — `GET /v2/user/followers`.
- [Get media where user is tagged](../examples/endpoints/v2_user_tag_medias.py) — `GET /v2/user/tag/medias`.
- [Get user highlights by ID](../examples/endpoints/v2_user_highlights.py) — `GET /v2/user/highlights`.
- [Get user highlights by username (by ID is faster)](../examples/endpoints/v2_user_highlights_by_username.py) — `GET /v2/user/highlights/by/username`.
- [Get business suggestions for user](../examples/endpoints/v2_user_explore_businesses_by_id.py) — `GET /v2/user/explore/businesses/by/id`.
- [Get suggested profiles for user](../examples/endpoints/v2_user_suggested_profiles.py) — `GET /v2/user/suggested/profiles`.
- [Get user followers (chunked)](../examples/endpoints/gql_user_followers_chunk.py) — `GET /gql/user/followers/chunk`.
- [Get user following (chunked)](../examples/endpoints/gql_user_following_chunk.py) — `GET /gql/user/following/chunk`.
- [Get user reposts](../examples/endpoints/gql_user_reposts.py) — `GET /gql/user/reposts`.
- [Get user clips (reels)](../examples/endpoints/gql_user_clips.py) — `GET /gql/user/clips`.
- [Get user profile media (grid)](../examples/endpoints/gql_user_medias.py) — `GET /gql/user/medias`.

</details>

<details>
<summary>Media · 20 examples</summary>

- [Get media info by ID](../examples/endpoints/v1_media_by_id.py) — `GET /v1/media/by/id`.
- [Get media info by shortcode](../examples/endpoints/v1_media_by_code.py) — `GET /v1/media/by/code`.
- [Get media info by URL](../examples/endpoints/v1_media_by_url.py) — `GET /v1/media/by/url`.
- [Get media insights](../examples/endpoints/v1_media_insight.py) — `GET /v1/media/insight`.
- [Get media comments (chunked)](../examples/endpoints/v1_media_comments_chunk.py) — `GET /v1/media/comments/chunk`.
- [Get media likers](../examples/endpoints/v1_media_likers.py) — `GET /v1/media/likers`.
- [Get author of the media](../examples/endpoints/v1_media_user.py) — `GET /v1/media/user`.
- [Get media oEmbed data](../examples/endpoints/v1_media_oembed.py) — `GET /v1/media/oembed`.
- [Get media code from media ID (PK) (unlimited usage)](../examples/endpoints/v1_media_code_from_pk.py) — `GET /v1/media/code/from/pk`.
- [Get media ID (PK) from shortcode (unlimited usage)](../examples/endpoints/v1_media_pk_from_code.py) — `GET /v1/media/pk/from/code`.
- [Get media ID (PK) from URL (unlimited usage)](../examples/endpoints/v1_media_pk_from_url.py) — `GET /v1/media/pk/from/url`.
- [Get media info by ID](../examples/endpoints/v2_media_info_by_id.py) — `GET /v2/media/info/by/id`.
- [Get media info by shortcode](../examples/endpoints/v2_media_info_by_code.py) — `GET /v2/media/info/by/code`.
- [Get media info by URL](../examples/endpoints/v2_media_info_by_url.py) — `GET /v2/media/info/by/url`.
- [Get media comments](../examples/endpoints/v2_media_comments.py) — `GET /v2/media/comments`.
- [Get media likers](../examples/endpoints/v2_media_likers.py) — `GET /v2/media/likers`.
- [Check comment for offensiveness](../examples/endpoints/v2_media_comment_offensive.py) — `GET /v2/media/comment/offensive`.
- [Get comment replies](../examples/endpoints/v2_media_comments_replies.py) — `GET /v2/media/comments/replies`.
- [Get media likers by media ID](../examples/endpoints/gql_media_likers.py) — `GET /gql/media/likers`.
- [Get video usertags by media IDs](../examples/endpoints/gql_media_usertags.py) — `GET /gql/media/usertags`.

</details>

<details>
<summary>Story · 6 examples</summary>

- [Get story by ID](../examples/endpoints/v1_story_by_id.py) — `GET /v1/story/by/id`.
- [Get story by URL](../examples/endpoints/v1_story_by_url.py) — `GET /v1/story/by/url`.
- [Download story by ID](../examples/endpoints/v1_story_download.py) — `GET /v1/story/download`.
- [Download story by direct media URL (unlimited usage)](../examples/endpoints/v1_story_download_by_url.py) — `GET /v1/story/download/by/url`.
- [Download story file by story URL (IG story link)](../examples/endpoints/v1_story_download_by_story_url.py) — `GET /v1/story/download/by/story/url`.
- [Get story by ID](../examples/endpoints/v2_story_by_id.py) — `GET /v2/story/by/id`.

</details>

<details>
<summary>Highlight · 3 examples</summary>

- [Get highlight by ID](../examples/endpoints/v1_highlight_by_id.py) — `GET /v1/highlight/by/id`.
- [Get highlight by URL](../examples/endpoints/v1_highlight_by_url.py) — `GET /v1/highlight/by/url`.
- [Get highlight by ID](../examples/endpoints/v2_highlight_by_id.py) — `GET /v2/highlight/by/id`.

</details>

<details>
<summary>Location · 6 examples</summary>

- [Get location by ID](../examples/endpoints/v1_location_by_id.py) — `GET /v1/location/by/id`.
- [Get location top medias](../examples/endpoints/v1_location_medias_top.py) — `GET /v1/location/medias/top`.
- [Get location recent medias](../examples/endpoints/v1_location_medias_recent.py) — `GET /v1/location/medias/recent`.
- [Get location top medias (chunked)](../examples/endpoints/v1_location_medias_top_chunk.py) — `GET /v1/location/medias/top/chunk`.
- [Get location recent medias (chunked)](../examples/endpoints/v1_location_medias_recent_chunk.py) — `GET /v1/location/medias/recent/chunk`.
- [Search locations](../examples/endpoints/v1_location_search.py) — `GET /v1/location/search`.

</details>

<details>
<summary>Hashtag · 8 examples</summary>

- [Get hashtag by name](../examples/endpoints/v1_hashtag_by_name.py) — `GET /v1/hashtag/by/name`.
- [Get hashtag top medias](../examples/endpoints/v1_hashtag_medias_top.py) — `GET /v1/hashtag/medias/top`.
- [Get hashtag top medias (chunked)](../examples/endpoints/v1_hashtag_medias_top_chunk.py) — `GET /v1/hashtag/medias/top/chunk`.
- [Get hashtag recent medias (chunked)](../examples/endpoints/v1_hashtag_medias_top_recent_chunk.py) — `GET /v1/hashtag/medias/top/recent/chunk`.
- [Get hashtag clips (chunked)](../examples/endpoints/v1_hashtag_medias_clips_chunk.py) — `GET /v1/hashtag/medias/clips/chunk`.
- [Get hashtag by name](../examples/endpoints/v2_hashtag_by_name.py) — `GET /v2/hashtag/by/name`.
- [Get hashtag top medias](../examples/endpoints/v2_hashtag_medias_top.py) — `GET /v2/hashtag/medias/top`.
- [Get hashtag recent medias](../examples/endpoints/v2_hashtag_medias_recent.py) — `GET /v2/hashtag/medias/recent`.

</details>

<details>
<summary>Search · 5 examples</summary>

- [Search hashtags](../examples/endpoints/v1_search_hashtags.py) — `GET /v1/search/hashtags`.
- [Search users](../examples/endpoints/v1_search_users.py) — `GET /v1/search/users`.
- [Search music](../examples/endpoints/v1_search_music.py) — `GET /v1/search/music`.
- [Search hashtags](../examples/endpoints/v2_search_hashtags.py) — `GET /v2/search/hashtags`.
- [Search music](../examples/endpoints/v2_search_music.py) — `GET /v2/search/music`.

</details>

<details>
<summary>Fbsearch · 8 examples</summary>

- [Search places](../examples/endpoints/v1_fbsearch_places.py) — `GET /v1/fbsearch/places`.
- [Top search](../examples/endpoints/v1_fbsearch_topsearch.py) — `GET /v1/fbsearch/topsearch`.
- [Search accounts (users)](../examples/endpoints/v2_fbsearch_accounts.py) — `GET /v2/fbsearch/accounts`.
- [Search places (locations)](../examples/endpoints/v2_fbsearch_places.py) — `GET /v2/fbsearch/places`.
- [Top search](../examples/endpoints/v2_fbsearch_topsearch.py) — `GET /v2/fbsearch/topsearch`.
- [Search reels (clips)](../examples/endpoints/v2_fbsearch_reels.py) — `GET /v2/fbsearch/reels`.
- [Search users](../examples/endpoints/v3_fbsearch_accounts.py) — `GET /v3/fbsearch/accounts`.
- [Search places (locations)](../examples/endpoints/v3_fbsearch_places.py) — `GET /v3/fbsearch/places`.

</details>

<details>
<summary>Userstream · 2 examples</summary>

- [Get user info stream by ID](../examples/endpoints/v2_userstream_by_id.py) — `GET /v2/userstream/by/id`.
- [Get user info stream by username](../examples/endpoints/v2_userstream_by_username.py) — `GET /v2/userstream/by/username`.

</details>

<details>
<summary>Track · 2 examples</summary>

- [Get music feed by canonical ID](../examples/endpoints/v2_track_by_canonical_id.py) — `GET /v2/track/by/canonical/id`.
- [Get music feed by ID](../examples/endpoints/v2_track_by_id.py) — `GET /v2/track/by/id`.

</details>

<details>
<summary>Comments · 2 examples</summary>

- [Get comments list by media ID (chunked)](../examples/endpoints/gql_comments_chunk.py) — `GET /gql/comments/chunk`.
- [Get threaded replies list by comment ID (chunked)](../examples/endpoints/gql_comments_threaded_chunk.py) — `GET /gql/comments/threaded/chunk`.

</details>

<details>
<summary>Comment · 1 examples</summary>

- [Get comment likers list by comment ID (chunked)](../examples/endpoints/gql_comment_likers_chunk.py) — `GET /gql/comment/likers/chunk`.

</details>

<details>
<summary>Topsearch · 1 examples</summary>

- [Search top content by keyword](../examples/endpoints/gql_topsearch.py) — `GET /gql/topsearch`.

</details>

## Configuration

Default API base URL: **`https://ig.jsonscraper.com`**. Configure `base_url`, `timeout` (seconds), `retries`, `cache_timeout`. HTTPS is required except for explicit localhost test servers. Default timeout is 30 seconds.

Retries default to **0**; opt in to 0–5 retries for HTTP 429, 502, 503 and 504. Numeric `Retry-After` is respected up to 60 seconds; otherwise bounded exponential backoff applies. HTTP-date values use backoff. Retries may consume API quota, and total elapsed time can exceed one request timeout.

The configured license key is sent using the API's `license_key` query parameter. It overrides per-request attempts to supply a different key. Redirects are disabled, TLS verification stays enabled, and transport errors do not include request URLs. Keep credential-bearing URLs out of your application and reverse-proxy logs.

## Errors, pagination and caching

HTTP exceptions expose the status code and retry information. Transport failures have a credential-safe message. HTTP 200 alone is not application success: inspect `status` and any quota/product error fields. HTTP 403 can indicate an access restriction; 429 means you should wait or check the plan's limits.

Pagination is endpoint-specific. Pass a returned cursor unchanged to the next request, stop when `has_more` is false/0, and stop if a cursor repeats. Always set your own page/request budget. The SDK does not invent cursor fields or automatically spend your quota.

`cache_timeout=60` enables API-side caching for 60 seconds; `0` disables it. See the current product terms for quota treatment. The SDK does not cache responses locally.

Large IDs must remain strings in your application. Python preserves integer precision; JavaScript converts unsafe JSON integers to strings; PHP uses `JSON_BIGINT_AS_STRING`; Go provides `Decode()` with `json.Number`; Java returns response bytes for your chosen JSON library; C# exposes bytes and `JsonDocument`.

## FAQ

**Is this the official platform API?** This is the jsonscraper service SDK. jsonscraper is independent and is not affiliated with or endorsed by Instagram, Meta.

**Is the library free?** The SDK source is MIT-licensed. The hosted API requires a separate paid license. See [current plans and access](https://jsonscraper.com/services/ig-scraper-api?utm_source=github&utm_medium=sdk&utm_campaign=instagram-api-python&utm_content=faq).

**Does it work without a key?** A valid product license key is required for normal API requests. Never use a README example as a source of credentials.

**Can I use it in an existing application?** Yes. Install the package, configure the client, and call it from your server-side service. It does not require a web framework.

**Where do I ask for help?** For reproducible SDK bugs, open a [GitHub issue](https://github.com/jsonscraper/instagram-api-python/issues) with sanitized details. For plans, license questions and service support, use [jsonscraper contacts](https://jsonscraper.com/contacts?utm_source=github&utm_medium=sdk&utm_campaign=instagram-api-python&utm_content=support).

## Development and releases

```sh
python3 tests/contract.py
```

Tests run offline against a local/mock HTTP server and require no API key. A GitHub Actions template is included in `docs/github-actions.yml`; enabling it later requires `workflow` permission. No automatic workflow is enabled by this release.

See [CHANGELOG.md](../CHANGELOG.md) for release notes. Package registry publishing is tracked separately from the public GitHub source release.

## Privacy

The SDK includes no installation, API usage or conversion telemetry. It sends requests only to the configured API endpoint. README website links carry UTM campaign parameters so jsonscraper can attribute website visits and actions to this repository; website tracking respects Do Not Track and Global Privacy Control. Purchase clicks are measured as intent, not confirmed payment.
