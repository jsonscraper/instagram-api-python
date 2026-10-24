# Instagram API endpoint reference

97 unique GET routes from the published Postman collection. Configure `license_key` on the client. Query parameters below use the same names as the API; check Postman for required/optional rules.

| SDK method | GET path | Query parameters | Purpose |
| --- | --- | --- | --- |
| `v1_user_by_id` | `/v1/user/by/id` | `id`, `cache_timeout` | Get user info by ID |
| `v1_user_by_username` | `/v1/user/by/username` | `username`, `cache_timeout` | Get user info by username (by ID is faster) |
| `v1_user_by_url` | `/v1/user/by/url` | `url`, `cache_timeout` | Get user info by URL (by ID is faster) |
| `v1_user_about` | `/v1/user/about` | `id`, `cache_timeout` | Get info about user by ID |
| `v1_user_medias_chunk` | `/v1/user/medias/chunk` | `user_id`, `end_cursor`, `cache_timeout` | Get posts (chunked) |
| `v1_user_medias_pinned` | `/v1/user/medias/pinned` | `user_id`, `amount`, `cache_timeout` | Get pinned posts |
| `v1_user_clips_chunk` | `/v1/user/clips/chunk` | `user_id`, `end_cursor`, `cache_timeout` | Get reels (chunked) |
| `v1_user_tag_medias_chunk` | `/v1/user/tag/medias/chunk` | `user_id`, `max_id`, `cache_timeout` | Get tagged (mentions) posts |
| `v1_user_stories` | `/v1/user/stories` | `user_id`, `amount`, `force`, `cache_timeout` | Get user stories by ID |
| `v1_user_stories_by_username` | `/v1/user/stories/by/username` | `username`, `amount`, `force`, `cache_timeout` | Get user stories by username (by ID is faster) |
| `v1_user_highlights` | `/v1/user/highlights` | `user_id`, `amount`, `force`, `cache_timeout` | Get user highlights by ID |
| `v1_user_highlights_by_username` | `/v1/user/highlights/by/username` | `username`, `amount`, `force`, `cache_timeout` | Get user highlights by username (by ID is faster) |
| `v1_user_search_followers` | `/v1/user/search/followers` | `user_id`, `query`, `force`, `cache_timeout` | Search in followers list by query (not working for legacy verified accounts) |
| `v1_user_search_following` | `/v1/user/search/following` | `user_id`, `query`, `force`, `cache_timeout` | Search in followings list by query (not working for legacy verified accounts) |
| `v1_user_following_chunk` | `/v1/user/following/chunk` | `user_id`, `max_id`, `cache_timeout` | Get user following (chunked) |
| `v1_user_followers_chunk` | `/v1/user/followers/chunk` | `user_id`, `max_id`, `cache_timeout` | Get user followers (chunked) |
| `v1_media_by_id` | `/v1/media/by/id` | `id`, `cache_timeout` | Get media info by ID |
| `v1_media_by_code` | `/v1/media/by/code` | `code`, `cache_timeout` | Get media info by shortcode |
| `v1_media_by_url` | `/v1/media/by/url` | `url`, `cache_timeout` | Get media info by URL |
| `v1_media_insight` | `/v1/media/insight` | `media_id`, `cache_timeout` | Get media insights |
| `v1_media_comments_chunk` | `/v1/media/comments/chunk` | `id`, `min_id`, `max_id`, `can_support_threading`, `cache_timeout` | Get media comments (chunked) |
| `v1_media_likers` | `/v1/media/likers` | `id`, `cache_timeout` | Get media likers |
| `v1_media_user` | `/v1/media/user` | `media_id`, `cache_timeout` | Get author of the media |
| `v1_media_oembed` | `/v1/media/oembed` | `url`, `cache_timeout` | Get media oEmbed data |
| `v1_media_code_from_pk` | `/v1/media/code/from/pk` | `pk`, `cache_timeout` | Get media code from media ID (PK) (unlimited usage) |
| `v1_media_pk_from_code` | `/v1/media/pk/from/code` | `code`, `cache_timeout` | Get media ID (PK) from shortcode (unlimited usage) |
| `v1_media_pk_from_url` | `/v1/media/pk/from/url` | `url`, `cache_timeout` | Get media ID (PK) from URL (unlimited usage) |
| `v1_story_by_id` | `/v1/story/by/id` | `id`, `cache_timeout` | Get story by ID |
| `v1_story_by_url` | `/v1/story/by/url` | `url`, `cache_timeout` | Get story by URL |
| `v1_story_download` | `/v1/story/download` | `id` | Download story by ID |
| `v1_story_download_by_url` | `/v1/story/download/by/url` | `url` | Download story by direct media URL (unlimited usage) |
| `v1_story_download_by_story_url` | `/v1/story/download/by/story/url` | `url` | Download story file by story URL (IG story link) |
| `v1_highlight_by_id` | `/v1/highlight/by/id` | `id`, `cache_timeout` | Get highlight by ID |
| `v1_highlight_by_url` | `/v1/highlight/by/url` | `url`, `cache_timeout` | Get highlight by URL |
| `v1_location_by_id` | `/v1/location/by/id` | `id`, `cache_timeout` | Get location by ID |
| `v1_location_medias_top` | `/v1/location/medias/top` | `location_pk`, `amount`, `cache_timeout` | Get location top medias |
| `v1_location_medias_recent` | `/v1/location/medias/recent` | `location_pk`, `amount`, `cache_timeout` | Get location recent medias |
| `v1_location_medias_top_chunk` | `/v1/location/medias/top/chunk` | `location_pk`, `max_id`, `cache_timeout` | Get location top medias (chunked) |
| `v1_location_medias_recent_chunk` | `/v1/location/medias/recent/chunk` | `location_pk`, `max_id`, `cache_timeout` | Get location recent medias (chunked) |
| `v1_location_search` | `/v1/location/search` | `lat`, `lng`, `cache_timeout` | Search locations |
| `v1_hashtag_by_name` | `/v1/hashtag/by/name` | `name`, `cache_timeout` | Get hashtag by name |
| `v1_hashtag_medias_top` | `/v1/hashtag/medias/top` | `name`, `amount`, `cache_timeout` | Get hashtag top medias |
| `v1_hashtag_medias_top_chunk` | `/v1/hashtag/medias/top/chunk` | `name`, `max_id`, `cache_timeout` | Get hashtag top medias (chunked) |
| `v1_hashtag_medias_top_recent_chunk` | `/v1/hashtag/medias/top/recent/chunk` | `name`, `max_id`, `cache_timeout` | Get hashtag recent medias (chunked) |
| `v1_hashtag_medias_clips_chunk` | `/v1/hashtag/medias/clips/chunk` | `name`, `max_id`, `cache_timeout` | Get hashtag clips (chunked) |
| `v1_search_hashtags` | `/v1/search/hashtags` | `query`, `cache_timeout` | Search hashtags |
| `v1_search_users` | `/v1/search/users` | `query`, `cache_timeout` | Search users |
| `v1_search_music` | `/v1/search/music` | `query`, `cache_timeout` | Search music |
| `v1_fbsearch_places` | `/v1/fbsearch/places` | `query`, `lat`, `lng`, `cache_timeout` | Search places |
| `v1_fbsearch_topsearch` | `/v1/fbsearch/topsearch` | `query`, `cache_timeout` | Top search |
| `v2_user_by_id` | `/v2/user/by/id` | `id`, `cache_timeout` | Get user info by ID |
| `v2_user_by_username` | `/v2/user/by/username` | `username`, `cache_timeout` | Get user info by username |
| `v2_userstream_by_id` | `/v2/userstream/by/id` | `id`, `cache_timeout` | Get user info stream by ID |
| `v2_userstream_by_username` | `/v2/userstream/by/username` | `username`, `cache_timeout` | Get user info stream by username |
| `v2_user_stories` | `/v2/user/stories` | `user_id`, `force`, `safe_int`, `cache_timeout` | Get user stories by ID |
| `v2_user_stories_by_username` | `/v2/user/stories/by/username` | `username`, `force`, `safe_int`, `cache_timeout` | Get user stories by username |
| `v2_user_clips` | `/v2/user/clips` | `user_id`, `page_id`, `safe_int`, `cache_timeout` | Get user reels by ID |
| `v2_user_following` | `/v2/user/following` | `user_id`, `page_id`, `cache_timeout` | Get user following list |
| `v2_user_followers` | `/v2/user/followers` | `user_id`, `page_id`, `cache_timeout` | Get user followers list |
| `v2_user_tag_medias` | `/v2/user/tag/medias` | `user_id`, `page_id`, `cache_timeout` | Get media where user is tagged |
| `v2_user_highlights` | `/v2/user/highlights` | `user_id`, `amount`, `force`, `cache_timeout` | Get user highlights by ID |
| `v2_user_highlights_by_username` | `/v2/user/highlights/by/username` | `username`, `amount`, `force`, `cache_timeout` | Get user highlights by username (by ID is faster) |
| `v2_user_explore_businesses_by_id` | `/v2/user/explore/businesses/by/id` | `user_id`, `cache_timeout` | Get business suggestions for user |
| `v2_user_suggested_profiles` | `/v2/user/suggested/profiles` | `user_id`, `expand_suggestion`, `cache_timeout` | Get suggested profiles for user |
| `v2_media_info_by_id` | `/v2/media/info/by/id` | `id`, `cache_timeout` | Get media info by ID |
| `v2_media_info_by_code` | `/v2/media/info/by/code` | `code`, `cache_timeout` | Get media info by shortcode |
| `v2_media_info_by_url` | `/v2/media/info/by/url` | `url`, `cache_timeout` | Get media info by URL |
| `v2_media_comments` | `/v2/media/comments` | `id`, `page_id`, `can_support_threading`, `cache_timeout` | Get media comments |
| `v2_media_likers` | `/v2/media/likers` | `id`, `cache_timeout` | Get media likers |
| `v2_media_comment_offensive` | `/v2/media/comment/offensive` | `media_id`, `comment`, `cache_timeout` | Check comment for offensiveness |
| `v2_media_comments_replies` | `/v2/media/comments/replies` | `media_id`, `comment_id`, `min_id`, `cache_timeout` | Get comment replies |
| `v2_story_by_id` | `/v2/story/by/id` | `id`, `cache_timeout` | Get story by ID |
| `v2_track_by_canonical_id` | `/v2/track/by/canonical/id` | `canonical_id`, `page_id`, `cache_timeout` | Get music feed by canonical ID |
| `v2_track_by_id` | `/v2/track/by/id` | `track_id`, `page_id`, `cache_timeout` | Get music feed by ID |
| `v2_hashtag_by_name` | `/v2/hashtag/by/name` | `name`, `cache_timeout` | Get hashtag by name |
| `v2_hashtag_medias_top` | `/v2/hashtag/medias/top` | `name`, `page_id`, `cache_timeout` | Get hashtag top medias |
| `v2_hashtag_medias_recent` | `/v2/hashtag/medias/recent` | `name`, `page_id`, `cache_timeout` | Get hashtag recent medias |
| `v2_highlight_by_id` | `/v2/highlight/by/id` | `id`, `cache_timeout` | Get highlight by ID |
| `v2_search_hashtags` | `/v2/search/hashtags` | `query`, `page_token`, `cache_timeout` | Search hashtags |
| `v2_search_music` | `/v2/search/music` | `query`, `next_max_id`, `cache_timeout` | Search music |
| `v2_fbsearch_accounts` | `/v2/fbsearch/accounts` | `query`, `page_token`, `cache_timeout` | Search accounts (users) |
| `v2_fbsearch_places` | `/v2/fbsearch/places` | `query`, `cache_timeout` | Search places (locations) |
| `v2_fbsearch_topsearch` | `/v2/fbsearch/topsearch` | `query`, `next_max_id`, `cache_timeout` | Top search |
| `v2_fbsearch_reels` | `/v2/fbsearch/reels` | `query`, `reels_max_id`, `cache_timeout` | Search reels (clips) |
| `gql_comments_chunk` | `/gql/comments/chunk` | `media_id`, `sort_order`, `end_cursor`, `cache_timeout` | Get comments list by media ID (chunked) |
| `gql_comments_threaded_chunk` | `/gql/comments/threaded/chunk` | `media_id`, `comment_id`, `end_cursor`, `cache_timeout` | Get threaded replies list by comment ID (chunked) |
| `gql_comment_likers_chunk` | `/gql/comment/likers/chunk` | `comment_id`, `end_cursor`, `cache_timeout` | Get comment likers list by comment ID (chunked) |
| `gql_topsearch` | `/gql/topsearch` | `query`, `cache_timeout` | Search top content by keyword |
| `gql_media_likers` | `/gql/media/likers` | `media_id`, `cache_timeout` | Get media likers by media ID |
| `gql_media_usertags` | `/gql/media/usertags` | `media_ids`, `cache_timeout` | Get video usertags by media IDs |
| `gql_user_followers_chunk` | `/gql/user/followers/chunk` | `user_id`, `force`, `end_cursor`, `cache_timeout` | Get user followers (chunked) |
| `gql_user_following_chunk` | `/gql/user/following/chunk` | `user_id`, `force`, `end_cursor`, `cache_timeout` | Get user following (chunked) |
| `gql_user_reposts` | `/gql/user/reposts` | `user_id`, `repost_next_max_id`, `flat`, `cache_timeout` | Get user reposts |
| `gql_user_clips` | `/gql/user/clips` | `user_id`, `max_id`, `sort_by_views`, `flat`, `cache_timeout` | Get user clips (reels) |
| `gql_user_medias` | `/gql/user/medias` | `user_id`, `profile_grid_items_cursor`, `flat`, `cache_timeout` | Get user profile media (grid) |
| `v3_fbsearch_accounts` | `/v3/fbsearch/accounts` | `query`, `page_token`, `cache_timeout` | Search users |
| `v3_fbsearch_places` | `/v3/fbsearch/places` | `query`, `cache_timeout` | Search places (locations) |
