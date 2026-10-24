# Instagram python request examples

Every file below is a complete single-request CLI program with environment-based authentication, all documented query options, timeout configuration, error handling and full response output. Sample defaults come from Postman; replace account names, IDs and URLs for your use case. `--help` requires no API key and makes no network request.

Set `JSONSCRAPER_INSTAGRAM_LICENSE_KEY` and install the SDK as described in the main README. Each execution makes one live request and may consume quota. None of these programs loops through a feed automatically.

## Get user info by ID

[Open the complete example](endpoints/v1_user_by_id.py) · `GET /v1/user/by/id`

```sh
python examples/endpoints/v1_user_by_id.py --help
```

## Get user info by username (by ID is faster)

[Open the complete example](endpoints/v1_user_by_username.py) · `GET /v1/user/by/username`

```sh
python examples/endpoints/v1_user_by_username.py --help
```

## Get user info by URL (by ID is faster)

[Open the complete example](endpoints/v1_user_by_url.py) · `GET /v1/user/by/url`

```sh
python examples/endpoints/v1_user_by_url.py --help
```

## Get info about user by ID

[Open the complete example](endpoints/v1_user_about.py) · `GET /v1/user/about`

```sh
python examples/endpoints/v1_user_about.py --help
```

## Get posts (chunked)

[Open the complete example](endpoints/v1_user_medias_chunk.py) · `GET /v1/user/medias/chunk`

```sh
python examples/endpoints/v1_user_medias_chunk.py --help
```

## Get pinned posts

[Open the complete example](endpoints/v1_user_medias_pinned.py) · `GET /v1/user/medias/pinned`

```sh
python examples/endpoints/v1_user_medias_pinned.py --help
```

## Get reels (chunked)

[Open the complete example](endpoints/v1_user_clips_chunk.py) · `GET /v1/user/clips/chunk`

```sh
python examples/endpoints/v1_user_clips_chunk.py --help
```

## Get tagged (mentions) posts

[Open the complete example](endpoints/v1_user_tag_medias_chunk.py) · `GET /v1/user/tag/medias/chunk`

```sh
python examples/endpoints/v1_user_tag_medias_chunk.py --help
```

## Get user stories by ID

[Open the complete example](endpoints/v1_user_stories.py) · `GET /v1/user/stories`

```sh
python examples/endpoints/v1_user_stories.py --help
```

## Get user stories by username (by ID is faster)

[Open the complete example](endpoints/v1_user_stories_by_username.py) · `GET /v1/user/stories/by/username`

```sh
python examples/endpoints/v1_user_stories_by_username.py --help
```

## Get user highlights by ID

[Open the complete example](endpoints/v1_user_highlights.py) · `GET /v1/user/highlights`

```sh
python examples/endpoints/v1_user_highlights.py --help
```

## Get user highlights by username (by ID is faster)

[Open the complete example](endpoints/v1_user_highlights_by_username.py) · `GET /v1/user/highlights/by/username`

```sh
python examples/endpoints/v1_user_highlights_by_username.py --help
```

## Search in followers list by query (not working for legacy verified accounts)

[Open the complete example](endpoints/v1_user_search_followers.py) · `GET /v1/user/search/followers`

```sh
python examples/endpoints/v1_user_search_followers.py --help
```

## Search in followings list by query (not working for legacy verified accounts)

[Open the complete example](endpoints/v1_user_search_following.py) · `GET /v1/user/search/following`

```sh
python examples/endpoints/v1_user_search_following.py --help
```

## Get user following (chunked)

[Open the complete example](endpoints/v1_user_following_chunk.py) · `GET /v1/user/following/chunk`

```sh
python examples/endpoints/v1_user_following_chunk.py --help
```

## Get user followers (chunked)

[Open the complete example](endpoints/v1_user_followers_chunk.py) · `GET /v1/user/followers/chunk`

```sh
python examples/endpoints/v1_user_followers_chunk.py --help
```

## Get media info by ID

[Open the complete example](endpoints/v1_media_by_id.py) · `GET /v1/media/by/id`

```sh
python examples/endpoints/v1_media_by_id.py --help
```

## Get media info by shortcode

[Open the complete example](endpoints/v1_media_by_code.py) · `GET /v1/media/by/code`

```sh
python examples/endpoints/v1_media_by_code.py --help
```

## Get media info by URL

[Open the complete example](endpoints/v1_media_by_url.py) · `GET /v1/media/by/url`

```sh
python examples/endpoints/v1_media_by_url.py --help
```

## Get media insights

[Open the complete example](endpoints/v1_media_insight.py) · `GET /v1/media/insight`

```sh
python examples/endpoints/v1_media_insight.py --help
```

## Get media comments (chunked)

[Open the complete example](endpoints/v1_media_comments_chunk.py) · `GET /v1/media/comments/chunk`

```sh
python examples/endpoints/v1_media_comments_chunk.py --help
```

## Get media likers

[Open the complete example](endpoints/v1_media_likers.py) · `GET /v1/media/likers`

```sh
python examples/endpoints/v1_media_likers.py --help
```

## Get author of the media

[Open the complete example](endpoints/v1_media_user.py) · `GET /v1/media/user`

```sh
python examples/endpoints/v1_media_user.py --help
```

## Get media oEmbed data

[Open the complete example](endpoints/v1_media_oembed.py) · `GET /v1/media/oembed`

```sh
python examples/endpoints/v1_media_oembed.py --help
```

## Get media code from media ID (PK) (unlimited usage)

[Open the complete example](endpoints/v1_media_code_from_pk.py) · `GET /v1/media/code/from/pk`

```sh
python examples/endpoints/v1_media_code_from_pk.py --help
```

## Get media ID (PK) from shortcode (unlimited usage)

[Open the complete example](endpoints/v1_media_pk_from_code.py) · `GET /v1/media/pk/from/code`

```sh
python examples/endpoints/v1_media_pk_from_code.py --help
```

## Get media ID (PK) from URL (unlimited usage)

[Open the complete example](endpoints/v1_media_pk_from_url.py) · `GET /v1/media/pk/from/url`

```sh
python examples/endpoints/v1_media_pk_from_url.py --help
```

## Get story by ID

[Open the complete example](endpoints/v1_story_by_id.py) · `GET /v1/story/by/id`

```sh
python examples/endpoints/v1_story_by_id.py --help
```

## Get story by URL

[Open the complete example](endpoints/v1_story_by_url.py) · `GET /v1/story/by/url`

```sh
python examples/endpoints/v1_story_by_url.py --help
```

## Download story by ID

[Open the complete example](endpoints/v1_story_download.py) · `GET /v1/story/download`

```sh
python examples/endpoints/v1_story_download.py --help
```

## Download story by direct media URL (unlimited usage)

[Open the complete example](endpoints/v1_story_download_by_url.py) · `GET /v1/story/download/by/url`

```sh
python examples/endpoints/v1_story_download_by_url.py --help
```

## Download story file by story URL (IG story link)

[Open the complete example](endpoints/v1_story_download_by_story_url.py) · `GET /v1/story/download/by/story/url`

```sh
python examples/endpoints/v1_story_download_by_story_url.py --help
```

## Get highlight by ID

[Open the complete example](endpoints/v1_highlight_by_id.py) · `GET /v1/highlight/by/id`

```sh
python examples/endpoints/v1_highlight_by_id.py --help
```

## Get highlight by URL

[Open the complete example](endpoints/v1_highlight_by_url.py) · `GET /v1/highlight/by/url`

```sh
python examples/endpoints/v1_highlight_by_url.py --help
```

## Get location by ID

[Open the complete example](endpoints/v1_location_by_id.py) · `GET /v1/location/by/id`

```sh
python examples/endpoints/v1_location_by_id.py --help
```

## Get location top medias

[Open the complete example](endpoints/v1_location_medias_top.py) · `GET /v1/location/medias/top`

```sh
python examples/endpoints/v1_location_medias_top.py --help
```

## Get location recent medias

[Open the complete example](endpoints/v1_location_medias_recent.py) · `GET /v1/location/medias/recent`

```sh
python examples/endpoints/v1_location_medias_recent.py --help
```

## Get location top medias (chunked)

[Open the complete example](endpoints/v1_location_medias_top_chunk.py) · `GET /v1/location/medias/top/chunk`

```sh
python examples/endpoints/v1_location_medias_top_chunk.py --help
```

## Get location recent medias (chunked)

[Open the complete example](endpoints/v1_location_medias_recent_chunk.py) · `GET /v1/location/medias/recent/chunk`

```sh
python examples/endpoints/v1_location_medias_recent_chunk.py --help
```

## Search locations

[Open the complete example](endpoints/v1_location_search.py) · `GET /v1/location/search`

```sh
python examples/endpoints/v1_location_search.py --help
```

## Get hashtag by name

[Open the complete example](endpoints/v1_hashtag_by_name.py) · `GET /v1/hashtag/by/name`

```sh
python examples/endpoints/v1_hashtag_by_name.py --help
```

## Get hashtag top medias

[Open the complete example](endpoints/v1_hashtag_medias_top.py) · `GET /v1/hashtag/medias/top`

```sh
python examples/endpoints/v1_hashtag_medias_top.py --help
```

## Get hashtag top medias (chunked)

[Open the complete example](endpoints/v1_hashtag_medias_top_chunk.py) · `GET /v1/hashtag/medias/top/chunk`

```sh
python examples/endpoints/v1_hashtag_medias_top_chunk.py --help
```

## Get hashtag recent medias (chunked)

[Open the complete example](endpoints/v1_hashtag_medias_top_recent_chunk.py) · `GET /v1/hashtag/medias/top/recent/chunk`

```sh
python examples/endpoints/v1_hashtag_medias_top_recent_chunk.py --help
```

## Get hashtag clips (chunked)

[Open the complete example](endpoints/v1_hashtag_medias_clips_chunk.py) · `GET /v1/hashtag/medias/clips/chunk`

```sh
python examples/endpoints/v1_hashtag_medias_clips_chunk.py --help
```

## Search hashtags

[Open the complete example](endpoints/v1_search_hashtags.py) · `GET /v1/search/hashtags`

```sh
python examples/endpoints/v1_search_hashtags.py --help
```

## Search users

[Open the complete example](endpoints/v1_search_users.py) · `GET /v1/search/users`

```sh
python examples/endpoints/v1_search_users.py --help
```

## Search music

[Open the complete example](endpoints/v1_search_music.py) · `GET /v1/search/music`

```sh
python examples/endpoints/v1_search_music.py --help
```

## Search places

[Open the complete example](endpoints/v1_fbsearch_places.py) · `GET /v1/fbsearch/places`

```sh
python examples/endpoints/v1_fbsearch_places.py --help
```

## Top search

[Open the complete example](endpoints/v1_fbsearch_topsearch.py) · `GET /v1/fbsearch/topsearch`

```sh
python examples/endpoints/v1_fbsearch_topsearch.py --help
```

## Get user info by ID

[Open the complete example](endpoints/v2_user_by_id.py) · `GET /v2/user/by/id`

```sh
python examples/endpoints/v2_user_by_id.py --help
```

## Get user info by username

[Open the complete example](endpoints/v2_user_by_username.py) · `GET /v2/user/by/username`

```sh
python examples/endpoints/v2_user_by_username.py --help
```

## Get user info stream by ID

[Open the complete example](endpoints/v2_userstream_by_id.py) · `GET /v2/userstream/by/id`

```sh
python examples/endpoints/v2_userstream_by_id.py --help
```

## Get user info stream by username

[Open the complete example](endpoints/v2_userstream_by_username.py) · `GET /v2/userstream/by/username`

```sh
python examples/endpoints/v2_userstream_by_username.py --help
```

## Get user stories by ID

[Open the complete example](endpoints/v2_user_stories.py) · `GET /v2/user/stories`

```sh
python examples/endpoints/v2_user_stories.py --help
```

## Get user stories by username

[Open the complete example](endpoints/v2_user_stories_by_username.py) · `GET /v2/user/stories/by/username`

```sh
python examples/endpoints/v2_user_stories_by_username.py --help
```

## Get user reels by ID

[Open the complete example](endpoints/v2_user_clips.py) · `GET /v2/user/clips`

```sh
python examples/endpoints/v2_user_clips.py --help
```

## Get user following list

[Open the complete example](endpoints/v2_user_following.py) · `GET /v2/user/following`

```sh
python examples/endpoints/v2_user_following.py --help
```

## Get user followers list

[Open the complete example](endpoints/v2_user_followers.py) · `GET /v2/user/followers`

```sh
python examples/endpoints/v2_user_followers.py --help
```

## Get media where user is tagged

[Open the complete example](endpoints/v2_user_tag_medias.py) · `GET /v2/user/tag/medias`

```sh
python examples/endpoints/v2_user_tag_medias.py --help
```

## Get user highlights by ID

[Open the complete example](endpoints/v2_user_highlights.py) · `GET /v2/user/highlights`

```sh
python examples/endpoints/v2_user_highlights.py --help
```

## Get user highlights by username (by ID is faster)

[Open the complete example](endpoints/v2_user_highlights_by_username.py) · `GET /v2/user/highlights/by/username`

```sh
python examples/endpoints/v2_user_highlights_by_username.py --help
```

## Get business suggestions for user

[Open the complete example](endpoints/v2_user_explore_businesses_by_id.py) · `GET /v2/user/explore/businesses/by/id`

```sh
python examples/endpoints/v2_user_explore_businesses_by_id.py --help
```

## Get suggested profiles for user

[Open the complete example](endpoints/v2_user_suggested_profiles.py) · `GET /v2/user/suggested/profiles`

```sh
python examples/endpoints/v2_user_suggested_profiles.py --help
```

## Get media info by ID

[Open the complete example](endpoints/v2_media_info_by_id.py) · `GET /v2/media/info/by/id`

```sh
python examples/endpoints/v2_media_info_by_id.py --help
```

## Get media info by shortcode

[Open the complete example](endpoints/v2_media_info_by_code.py) · `GET /v2/media/info/by/code`

```sh
python examples/endpoints/v2_media_info_by_code.py --help
```

## Get media info by URL

[Open the complete example](endpoints/v2_media_info_by_url.py) · `GET /v2/media/info/by/url`

```sh
python examples/endpoints/v2_media_info_by_url.py --help
```

## Get media comments

[Open the complete example](endpoints/v2_media_comments.py) · `GET /v2/media/comments`

```sh
python examples/endpoints/v2_media_comments.py --help
```

## Get media likers

[Open the complete example](endpoints/v2_media_likers.py) · `GET /v2/media/likers`

```sh
python examples/endpoints/v2_media_likers.py --help
```

## Check comment for offensiveness

[Open the complete example](endpoints/v2_media_comment_offensive.py) · `GET /v2/media/comment/offensive`

```sh
python examples/endpoints/v2_media_comment_offensive.py --help
```

## Get comment replies

[Open the complete example](endpoints/v2_media_comments_replies.py) · `GET /v2/media/comments/replies`

```sh
python examples/endpoints/v2_media_comments_replies.py --help
```

## Get story by ID

[Open the complete example](endpoints/v2_story_by_id.py) · `GET /v2/story/by/id`

```sh
python examples/endpoints/v2_story_by_id.py --help
```

## Get music feed by canonical ID

[Open the complete example](endpoints/v2_track_by_canonical_id.py) · `GET /v2/track/by/canonical/id`

```sh
python examples/endpoints/v2_track_by_canonical_id.py --help
```

## Get music feed by ID

[Open the complete example](endpoints/v2_track_by_id.py) · `GET /v2/track/by/id`

```sh
python examples/endpoints/v2_track_by_id.py --help
```

## Get hashtag by name

[Open the complete example](endpoints/v2_hashtag_by_name.py) · `GET /v2/hashtag/by/name`

```sh
python examples/endpoints/v2_hashtag_by_name.py --help
```

## Get hashtag top medias

[Open the complete example](endpoints/v2_hashtag_medias_top.py) · `GET /v2/hashtag/medias/top`

```sh
python examples/endpoints/v2_hashtag_medias_top.py --help
```

## Get hashtag recent medias

[Open the complete example](endpoints/v2_hashtag_medias_recent.py) · `GET /v2/hashtag/medias/recent`

```sh
python examples/endpoints/v2_hashtag_medias_recent.py --help
```

## Get highlight by ID

[Open the complete example](endpoints/v2_highlight_by_id.py) · `GET /v2/highlight/by/id`

```sh
python examples/endpoints/v2_highlight_by_id.py --help
```

## Search hashtags

[Open the complete example](endpoints/v2_search_hashtags.py) · `GET /v2/search/hashtags`

```sh
python examples/endpoints/v2_search_hashtags.py --help
```

## Search music

[Open the complete example](endpoints/v2_search_music.py) · `GET /v2/search/music`

```sh
python examples/endpoints/v2_search_music.py --help
```

## Search accounts (users)

[Open the complete example](endpoints/v2_fbsearch_accounts.py) · `GET /v2/fbsearch/accounts`

```sh
python examples/endpoints/v2_fbsearch_accounts.py --help
```

## Search places (locations)

[Open the complete example](endpoints/v2_fbsearch_places.py) · `GET /v2/fbsearch/places`

```sh
python examples/endpoints/v2_fbsearch_places.py --help
```

## Top search

[Open the complete example](endpoints/v2_fbsearch_topsearch.py) · `GET /v2/fbsearch/topsearch`

```sh
python examples/endpoints/v2_fbsearch_topsearch.py --help
```

## Search reels (clips)

[Open the complete example](endpoints/v2_fbsearch_reels.py) · `GET /v2/fbsearch/reels`

```sh
python examples/endpoints/v2_fbsearch_reels.py --help
```

## Get comments list by media ID (chunked)

[Open the complete example](endpoints/gql_comments_chunk.py) · `GET /gql/comments/chunk`

```sh
python examples/endpoints/gql_comments_chunk.py --help
```

## Get threaded replies list by comment ID (chunked)

[Open the complete example](endpoints/gql_comments_threaded_chunk.py) · `GET /gql/comments/threaded/chunk`

```sh
python examples/endpoints/gql_comments_threaded_chunk.py --help
```

## Get comment likers list by comment ID (chunked)

[Open the complete example](endpoints/gql_comment_likers_chunk.py) · `GET /gql/comment/likers/chunk`

```sh
python examples/endpoints/gql_comment_likers_chunk.py --help
```

## Search top content by keyword

[Open the complete example](endpoints/gql_topsearch.py) · `GET /gql/topsearch`

```sh
python examples/endpoints/gql_topsearch.py --help
```

## Get media likers by media ID

[Open the complete example](endpoints/gql_media_likers.py) · `GET /gql/media/likers`

```sh
python examples/endpoints/gql_media_likers.py --help
```

## Get video usertags by media IDs

[Open the complete example](endpoints/gql_media_usertags.py) · `GET /gql/media/usertags`

```sh
python examples/endpoints/gql_media_usertags.py --help
```

## Get user followers (chunked)

[Open the complete example](endpoints/gql_user_followers_chunk.py) · `GET /gql/user/followers/chunk`

```sh
python examples/endpoints/gql_user_followers_chunk.py --help
```

## Get user following (chunked)

[Open the complete example](endpoints/gql_user_following_chunk.py) · `GET /gql/user/following/chunk`

```sh
python examples/endpoints/gql_user_following_chunk.py --help
```

## Get user reposts

[Open the complete example](endpoints/gql_user_reposts.py) · `GET /gql/user/reposts`

```sh
python examples/endpoints/gql_user_reposts.py --help
```

## Get user clips (reels)

[Open the complete example](endpoints/gql_user_clips.py) · `GET /gql/user/clips`

```sh
python examples/endpoints/gql_user_clips.py --help
```

## Get user profile media (grid)

[Open the complete example](endpoints/gql_user_medias.py) · `GET /gql/user/medias`

```sh
python examples/endpoints/gql_user_medias.py --help
```

## Search users

[Open the complete example](endpoints/v3_fbsearch_accounts.py) · `GET /v3/fbsearch/accounts`

```sh
python examples/endpoints/v3_fbsearch_accounts.py --help
```

## Search places (locations)

[Open the complete example](endpoints/v3_fbsearch_places.py) · `GET /v3/fbsearch/places`

```sh
python examples/endpoints/v3_fbsearch_places.py --help
```

