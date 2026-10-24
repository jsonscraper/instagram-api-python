"""Official jsonscraper API clients. License keys stay on the server."""
import json
import math
import re
import time
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError

class APIError(Exception):
    def __init__(self, status, retry_after=None):
        self.status = status
        self.retry_after = retry_after
        super().__init__(f"jsonscraper API returned HTTP {status}")

class TransportError(Exception):
    pass

class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

class Client:
    def __init__(self, license_key, *, product="instagram", base_url=None, timeout=30, retries=0, cache_timeout=None):
        if product not in ("instagram", "tiktok"):
            raise ValueError("Unknown product")
        if not isinstance(license_key, str) or not license_key.strip():
            raise ValueError("A license key is required")
        base_url = base_url or {"instagram": "https://ig.jsonscraper.com", "tiktok": "https://tiktok.evelode.com"}[product]
        url = urlsplit(base_url)
        if url.scheme not in ("https", "http") or not url.netloc or url.username or url.password or url.query or url.fragment:
            raise ValueError("Invalid base URL")
        if url.scheme != "https" and url.hostname not in ("localhost", "127.0.0.1", "::1"):
            raise ValueError("HTTPS is required outside localhost")
        if not math.isfinite(timeout) or timeout <= 0 or not isinstance(retries, int) or not 0 <= retries <= 5:
            raise ValueError("Invalid timeout or retries")
        self._key, self.base_url = license_key, base_url.rstrip("/")
        self.timeout, self.retries, self.cache_timeout = timeout, retries, cache_timeout
        self._opener = build_opener(_NoRedirect())

    def request(self, path, **params):
        if not isinstance(path, str) or not re.fullmatch(r"/[A-Za-z0-9_/-]+", path) or ".." in path or "//" in path:
            raise ValueError("Use an API path, not a URL")
        params = {k: v for k, v in params.items() if v is not None and k != "license_key"}
        if self.cache_timeout is not None:
            params.setdefault("cache_timeout", self.cache_timeout)
        params["license_key"] = self._key
        query = urlencode({k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}, doseq=True)
        req = Request(self.base_url + path + "?" + query, headers={"Accept": "application/json", "User-Agent": "jsonscraper-python/0.1.0"})
        for attempt in range(self.retries + 1):
            try:
                with self._opener.open(req, timeout=self.timeout) as response:
                    body = response.read()
                    if "json" not in response.headers.get("Content-Type", "").lower():
                        return body
                    try:
                        return json.loads(body)
                    except (ValueError, UnicodeError):
                        raise TransportError("Invalid JSON response") from None
            except HTTPError as error:
                status, header = error.code, error.headers.get("Retry-After")
                error.close()
                delay = min(60, int(header)) if header and header.isdigit() else min(2 ** attempt, 30)
                if attempt == self.retries or status not in (429, 502, 503, 504):
                    raise APIError(status, header) from None
                time.sleep(delay)
            except (URLError, TimeoutError, OSError):
                raise TransportError("Unable to reach jsonscraper API") from None

class Instagram(Client):
    def __init__(self, license_key, **options):
        super().__init__(license_key, product="instagram", **options)

    def v1_user_by_id(self, **params):
        """Get user info by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/user/by/id", **params)

    def v1_user_by_username(self, **params):
        """Get user info by username (by ID is faster). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/by/username", **params)

    def v1_user_by_url(self, **params):
        """Get user info by URL (by ID is faster). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/by/url", **params)

    def v1_user_about(self, **params):
        """Get info about user by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/user/about", **params)

    def v1_user_medias_chunk(self, **params):
        """Get posts (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/medias/chunk", **params)

    def v1_user_medias_pinned(self, **params):
        """Get pinned posts. See docs/endpoints.md for parameters."""
        return self.request("/v1/user/medias/pinned", **params)

    def v1_user_clips_chunk(self, **params):
        """Get reels (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/clips/chunk", **params)

    def v1_user_tag_medias_chunk(self, **params):
        """Get tagged (mentions) posts. See docs/endpoints.md for parameters."""
        return self.request("/v1/user/tag/medias/chunk", **params)

    def v1_user_stories(self, **params):
        """Get user stories by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/user/stories", **params)

    def v1_user_stories_by_username(self, **params):
        """Get user stories by username (by ID is faster). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/stories/by/username", **params)

    def v1_user_highlights(self, **params):
        """Get user highlights by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/user/highlights", **params)

    def v1_user_highlights_by_username(self, **params):
        """Get user highlights by username (by ID is faster). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/highlights/by/username", **params)

    def v1_user_search_followers(self, **params):
        """Search in followers list by query (not working for legacy verified accounts). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/search/followers", **params)

    def v1_user_search_following(self, **params):
        """Search in followings list by query (not working for legacy verified accounts). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/search/following", **params)

    def v1_user_following_chunk(self, **params):
        """Get user following (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/following/chunk", **params)

    def v1_user_followers_chunk(self, **params):
        """Get user followers (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/user/followers/chunk", **params)

    def v1_media_by_id(self, **params):
        """Get media info by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/by/id", **params)

    def v1_media_by_code(self, **params):
        """Get media info by shortcode. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/by/code", **params)

    def v1_media_by_url(self, **params):
        """Get media info by URL. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/by/url", **params)

    def v1_media_insight(self, **params):
        """Get media insights. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/insight", **params)

    def v1_media_comments_chunk(self, **params):
        """Get media comments (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/media/comments/chunk", **params)

    def v1_media_likers(self, **params):
        """Get media likers. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/likers", **params)

    def v1_media_user(self, **params):
        """Get author of the media. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/user", **params)

    def v1_media_oembed(self, **params):
        """Get media oEmbed data. See docs/endpoints.md for parameters."""
        return self.request("/v1/media/oembed", **params)

    def v1_media_code_from_pk(self, **params):
        """Get media code from media ID (PK) (unlimited usage). See docs/endpoints.md for parameters."""
        return self.request("/v1/media/code/from/pk", **params)

    def v1_media_pk_from_code(self, **params):
        """Get media ID (PK) from shortcode (unlimited usage). See docs/endpoints.md for parameters."""
        return self.request("/v1/media/pk/from/code", **params)

    def v1_media_pk_from_url(self, **params):
        """Get media ID (PK) from URL (unlimited usage). See docs/endpoints.md for parameters."""
        return self.request("/v1/media/pk/from/url", **params)

    def v1_story_by_id(self, **params):
        """Get story by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/story/by/id", **params)

    def v1_story_by_url(self, **params):
        """Get story by URL. See docs/endpoints.md for parameters."""
        return self.request("/v1/story/by/url", **params)

    def v1_story_download(self, **params):
        """Download story by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/story/download", **params)

    def v1_story_download_by_url(self, **params):
        """Download story by direct media URL (unlimited usage). See docs/endpoints.md for parameters."""
        return self.request("/v1/story/download/by/url", **params)

    def v1_story_download_by_story_url(self, **params):
        """Download story file by story URL (IG story link). See docs/endpoints.md for parameters."""
        return self.request("/v1/story/download/by/story/url", **params)

    def v1_highlight_by_id(self, **params):
        """Get highlight by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/highlight/by/id", **params)

    def v1_highlight_by_url(self, **params):
        """Get highlight by URL. See docs/endpoints.md for parameters."""
        return self.request("/v1/highlight/by/url", **params)

    def v1_location_by_id(self, **params):
        """Get location by ID. See docs/endpoints.md for parameters."""
        return self.request("/v1/location/by/id", **params)

    def v1_location_medias_top(self, **params):
        """Get location top medias. See docs/endpoints.md for parameters."""
        return self.request("/v1/location/medias/top", **params)

    def v1_location_medias_recent(self, **params):
        """Get location recent medias. See docs/endpoints.md for parameters."""
        return self.request("/v1/location/medias/recent", **params)

    def v1_location_medias_top_chunk(self, **params):
        """Get location top medias (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/location/medias/top/chunk", **params)

    def v1_location_medias_recent_chunk(self, **params):
        """Get location recent medias (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/location/medias/recent/chunk", **params)

    def v1_location_search(self, **params):
        """Search locations. See docs/endpoints.md for parameters."""
        return self.request("/v1/location/search", **params)

    def v1_hashtag_by_name(self, **params):
        """Get hashtag by name. See docs/endpoints.md for parameters."""
        return self.request("/v1/hashtag/by/name", **params)

    def v1_hashtag_medias_top(self, **params):
        """Get hashtag top medias. See docs/endpoints.md for parameters."""
        return self.request("/v1/hashtag/medias/top", **params)

    def v1_hashtag_medias_top_chunk(self, **params):
        """Get hashtag top medias (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/hashtag/medias/top/chunk", **params)

    def v1_hashtag_medias_top_recent_chunk(self, **params):
        """Get hashtag recent medias (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/hashtag/medias/top/recent/chunk", **params)

    def v1_hashtag_medias_clips_chunk(self, **params):
        """Get hashtag clips (chunked). See docs/endpoints.md for parameters."""
        return self.request("/v1/hashtag/medias/clips/chunk", **params)

    def v1_search_hashtags(self, **params):
        """Search hashtags. See docs/endpoints.md for parameters."""
        return self.request("/v1/search/hashtags", **params)

    def v1_search_users(self, **params):
        """Search users. See docs/endpoints.md for parameters."""
        return self.request("/v1/search/users", **params)

    def v1_search_music(self, **params):
        """Search music. See docs/endpoints.md for parameters."""
        return self.request("/v1/search/music", **params)

    def v1_fbsearch_places(self, **params):
        """Search places. See docs/endpoints.md for parameters."""
        return self.request("/v1/fbsearch/places", **params)

    def v1_fbsearch_topsearch(self, **params):
        """Top search. See docs/endpoints.md for parameters."""
        return self.request("/v1/fbsearch/topsearch", **params)

    def v2_user_by_id(self, **params):
        """Get user info by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/by/id", **params)

    def v2_user_by_username(self, **params):
        """Get user info by username. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/by/username", **params)

    def v2_userstream_by_id(self, **params):
        """Get user info stream by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/userstream/by/id", **params)

    def v2_userstream_by_username(self, **params):
        """Get user info stream by username. See docs/endpoints.md for parameters."""
        return self.request("/v2/userstream/by/username", **params)

    def v2_user_stories(self, **params):
        """Get user stories by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/stories", **params)

    def v2_user_stories_by_username(self, **params):
        """Get user stories by username. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/stories/by/username", **params)

    def v2_user_clips(self, **params):
        """Get user reels by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/clips", **params)

    def v2_user_following(self, **params):
        """Get user following list. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/following", **params)

    def v2_user_followers(self, **params):
        """Get user followers list. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/followers", **params)

    def v2_user_tag_medias(self, **params):
        """Get media where user is tagged. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/tag/medias", **params)

    def v2_user_highlights(self, **params):
        """Get user highlights by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/highlights", **params)

    def v2_user_highlights_by_username(self, **params):
        """Get user highlights by username (by ID is faster). See docs/endpoints.md for parameters."""
        return self.request("/v2/user/highlights/by/username", **params)

    def v2_user_explore_businesses_by_id(self, **params):
        """Get business suggestions for user. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/explore/businesses/by/id", **params)

    def v2_user_suggested_profiles(self, **params):
        """Get suggested profiles for user. See docs/endpoints.md for parameters."""
        return self.request("/v2/user/suggested/profiles", **params)

    def v2_media_info_by_id(self, **params):
        """Get media info by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/info/by/id", **params)

    def v2_media_info_by_code(self, **params):
        """Get media info by shortcode. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/info/by/code", **params)

    def v2_media_info_by_url(self, **params):
        """Get media info by URL. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/info/by/url", **params)

    def v2_media_comments(self, **params):
        """Get media comments. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/comments", **params)

    def v2_media_likers(self, **params):
        """Get media likers. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/likers", **params)

    def v2_media_comment_offensive(self, **params):
        """Check comment for offensiveness. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/comment/offensive", **params)

    def v2_media_comments_replies(self, **params):
        """Get comment replies. See docs/endpoints.md for parameters."""
        return self.request("/v2/media/comments/replies", **params)

    def v2_story_by_id(self, **params):
        """Get story by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/story/by/id", **params)

    def v2_track_by_canonical_id(self, **params):
        """Get music feed by canonical ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/track/by/canonical/id", **params)

    def v2_track_by_id(self, **params):
        """Get music feed by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/track/by/id", **params)

    def v2_hashtag_by_name(self, **params):
        """Get hashtag by name. See docs/endpoints.md for parameters."""
        return self.request("/v2/hashtag/by/name", **params)

    def v2_hashtag_medias_top(self, **params):
        """Get hashtag top medias. See docs/endpoints.md for parameters."""
        return self.request("/v2/hashtag/medias/top", **params)

    def v2_hashtag_medias_recent(self, **params):
        """Get hashtag recent medias. See docs/endpoints.md for parameters."""
        return self.request("/v2/hashtag/medias/recent", **params)

    def v2_highlight_by_id(self, **params):
        """Get highlight by ID. See docs/endpoints.md for parameters."""
        return self.request("/v2/highlight/by/id", **params)

    def v2_search_hashtags(self, **params):
        """Search hashtags. See docs/endpoints.md for parameters."""
        return self.request("/v2/search/hashtags", **params)

    def v2_search_music(self, **params):
        """Search music. See docs/endpoints.md for parameters."""
        return self.request("/v2/search/music", **params)

    def v2_fbsearch_accounts(self, **params):
        """Search accounts (users). See docs/endpoints.md for parameters."""
        return self.request("/v2/fbsearch/accounts", **params)

    def v2_fbsearch_places(self, **params):
        """Search places (locations). See docs/endpoints.md for parameters."""
        return self.request("/v2/fbsearch/places", **params)

    def v2_fbsearch_topsearch(self, **params):
        """Top search. See docs/endpoints.md for parameters."""
        return self.request("/v2/fbsearch/topsearch", **params)

    def v2_fbsearch_reels(self, **params):
        """Search reels (clips). See docs/endpoints.md for parameters."""
        return self.request("/v2/fbsearch/reels", **params)

    def gql_comments_chunk(self, **params):
        """Get comments list by media ID (chunked). See docs/endpoints.md for parameters."""
        return self.request("/gql/comments/chunk", **params)

    def gql_comments_threaded_chunk(self, **params):
        """Get threaded replies list by comment ID (chunked). See docs/endpoints.md for parameters."""
        return self.request("/gql/comments/threaded/chunk", **params)

    def gql_comment_likers_chunk(self, **params):
        """Get comment likers list by comment ID (chunked). See docs/endpoints.md for parameters."""
        return self.request("/gql/comment/likers/chunk", **params)

    def gql_topsearch(self, **params):
        """Search top content by keyword. See docs/endpoints.md for parameters."""
        return self.request("/gql/topsearch", **params)

    def gql_media_likers(self, **params):
        """Get media likers by media ID. See docs/endpoints.md for parameters."""
        return self.request("/gql/media/likers", **params)

    def gql_media_usertags(self, **params):
        """Get video usertags by media IDs. See docs/endpoints.md for parameters."""
        return self.request("/gql/media/usertags", **params)

    def gql_user_followers_chunk(self, **params):
        """Get user followers (chunked). See docs/endpoints.md for parameters."""
        return self.request("/gql/user/followers/chunk", **params)

    def gql_user_following_chunk(self, **params):
        """Get user following (chunked). See docs/endpoints.md for parameters."""
        return self.request("/gql/user/following/chunk", **params)

    def gql_user_reposts(self, **params):
        """Get user reposts. See docs/endpoints.md for parameters."""
        return self.request("/gql/user/reposts", **params)

    def gql_user_clips(self, **params):
        """Get user clips (reels). See docs/endpoints.md for parameters."""
        return self.request("/gql/user/clips", **params)

    def gql_user_medias(self, **params):
        """Get user profile media (grid). See docs/endpoints.md for parameters."""
        return self.request("/gql/user/medias", **params)

    def v3_fbsearch_accounts(self, **params):
        """Search users. See docs/endpoints.md for parameters."""
        return self.request("/v3/fbsearch/accounts", **params)

    def v3_fbsearch_places(self, **params):
        """Search places (locations). See docs/endpoints.md for parameters."""
        return self.request("/v3/fbsearch/places", **params)

class TikTok(Client):
    def __init__(self, license_key, **options):
        super().__init__(license_key, product="tiktok", **options)

    def get_no_watermark_url(self, **params):
        """Get non watermarked video url. See docs/endpoints.md for parameters."""
        return self.request("/getNoWatermarkUrl", **params)

    def get_no_watermark_url_by_id(self, **params):
        """Get non watermarked video url by video ID. See docs/endpoints.md for parameters."""
        return self.request("/getNoWatermarkUrlByID", **params)

    def get_video_by_id(self, **params):
        """Get video info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getVideoByID", **params)

    def get_video_by_url(self, **params):
        """Get video info by URL. See docs/endpoints.md for parameters."""
        return self.request("/getVideoByUrl", **params)

    def get_unshortened_url(self, **params):
        """Convert short TikTok video URL to full TikTok video URL. See docs/endpoints.md for parameters."""
        return self.request("/getUnshortenedUrl", **params)

    def get_comments_by_url(self, **params):
        """Get comments list by video URL. See docs/endpoints.md for parameters."""
        return self.request("/getCommentsByUrl", **params)

    def get_comments_by_id(self, **params):
        """Get comments list by video ID. See docs/endpoints.md for parameters."""
        return self.request("/getCommentsByID", **params)

    def get_comments_replies(self, **params):
        """Get comments replies. See docs/endpoints.md for parameters."""
        return self.request("/getCommentsReplies", **params)

    def search_user(self, **params):
        """Search for user by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchUser", **params)

    def search_video(self, **params):
        """Search for video by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchVideo", **params)

    def search_music(self, **params):
        """Search for music by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchMusic", **params)

    def search_live(self, **params):
        """Search for live by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchLive", **params)

    def search_hashtag(self, **params):
        """Search for hashtag by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchHashtag", **params)

    def search_location(self, **params):
        """Search for location by keyword. See docs/endpoints.md for parameters."""
        return self.request("/searchLocation", **params)

    def search_top(self, **params):
        """Top search by text query. See docs/endpoints.md for parameters."""
        return self.request("/searchTop", **params)

    def search_insights(self, **params):
        """Search insights by text query. See docs/endpoints.md for parameters."""
        return self.request("/searchInsights", **params)

    def search_comment_suggested_users(self, **params):
        """Search comment suggested users. See docs/endpoints.md for parameters."""
        return self.request("/searchCommentSuggestedUsers", **params)

    def get_user_info(self, **params):
        """Get user info by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getUserInfo", **params)

    def get_user_info_by_id(self, **params):
        """Get user info by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getUserInfoByID", **params)

    def get_basic_user_info(self, **params):
        """Get user info by username. See docs/endpoints.md for parameters."""
        return self.request("/getBasicUserInfo", **params)

    def get_user_feed(self, **params):
        """Get user feed by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getUserFeed", **params)

    def get_user_feed_by_id(self, **params):
        """Get user feed by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getUserFeedByID", **params)

    def get_user_id(self, **params):
        """Get user ID by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getUserID", **params)

    def get_username_by_id(self, **params):
        """Get username by TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getUsernameByID", **params)

    def get_twitter_username(self, **params):
        """Get Twitter username by profile URL, nickname or TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getTwitterUsername", **params)

    def get_instagram_username(self, **params):
        """Get Instagram username by profile URL, nickname or TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getInstagramUsername", **params)

    def get_youtube_channel(self, **params):
        """Get YouTube channel info by profile URL, nickname or TikTok user ID. See docs/endpoints.md for parameters."""
        return self.request("/getYoutubeChannel", **params)

    def get_followers(self, **params):
        """Get user followers by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getFollowers", **params)

    def get_followers_by_id(self, **params):
        """Get user followers by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getFollowersByID", **params)

    def get_following(self, **params):
        """Get user following by profile URL or nickname. See docs/endpoints.md for parameters."""
        return self.request("/getFollowing", **params)

    def get_following_by_id(self, **params):
        """Get user following by profile ID. See docs/endpoints.md for parameters."""
        return self.request("/getFollowingByID", **params)

    def get_live_event_info_by_id(self, **params):
        """Get live event info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getLiveEventInfoByID", **params)

    def get_hashtag_info(self, **params):
        """Get hashtag info by URL or tag name. See docs/endpoints.md for parameters."""
        return self.request("/getHashtagInfo", **params)

    def get_hashtag_feed(self, **params):
        """Get hashtag feed by URL or tag name. See docs/endpoints.md for parameters."""
        return self.request("/getHashtagFeed", **params)

    def get_hashtag_feed_by_id(self, **params):
        """Get hashtag feed by ID. See docs/endpoints.md for parameters."""
        return self.request("/getHashtagFeedByID", **params)

    def get_location_info_by_id(self, **params):
        """Get location info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getLocationInfoByID", **params)

    def get_location_feed_by_id(self, **params):
        """Get videos by location ID. See docs/endpoints.md for parameters."""
        return self.request("/getLocationFeedByID", **params)

    def get_music_info(self, **params):
        """Get music info by URL or ID. See docs/endpoints.md for parameters."""
        return self.request("/getMusicInfo", **params)

    def get_music_feed(self, **params):
        """Get music feed by URL or ID. See docs/endpoints.md for parameters."""
        return self.request("/getMusicFeed", **params)

    def get_music_charts(self, **params):
        """Get music charts. See docs/endpoints.md for parameters."""
        return self.request("/getMusicCharts", **params)

    def get_trending_categories_list(self, **params):
        """Get trending categories list. See docs/endpoints.md for parameters."""
        return self.request("/getTrendingCategoriesList", **params)

    def get_trending_feed(self, **params):
        """Get trending feed. See docs/endpoints.md for parameters."""
        return self.request("/getTrendingFeed", **params)

    def get_stickers_by_id(self, **params):
        """Get effect information by IDs. See docs/endpoints.md for parameters."""
        return self.request("/getStickersByID", **params)

    def get_sticker_by_id(self, **params):
        """Get effect information by ID. See docs/endpoints.md for parameters."""
        return self.request("/getStickerByID", **params)

    def get_sticker_feed_by_id(self, **params):
        """Get videos by effect ID. See docs/endpoints.md for parameters."""
        return self.request("/getStickerFeedByID", **params)

    def get_user_stories(self, **params):
        """Get user stories. See docs/endpoints.md for parameters."""
        return self.request("/getUserStories", **params)

    def get_story_info_by_id(self, **params):
        """Get story info by ID. See docs/endpoints.md for parameters."""
        return self.request("/getStoryInfoByID", **params)

    def get_user_playlists(self, **params):
        """Get user playlists. See docs/endpoints.md for parameters."""
        return self.request("/getUserPlaylists", **params)

    def get_user_playlist_by_id(self, **params):
        """Get user playlist by ID. See docs/endpoints.md for parameters."""
        return self.request("/getUserPlaylistByID", **params)

    def get_video_by_playlist_id(self, **params):
        """Get video by playlist ID. See docs/endpoints.md for parameters."""
        return self.request("/getVideoByPlaylistID", **params)

    def get_available_ranking_list(self, **params):
        """Get available ranking list. See docs/endpoints.md for parameters."""
        return self.request("/getAvailableRankingList", **params)

    def get_ranking_info(self, **params):
        """Get ranking info. See docs/endpoints.md for parameters."""
        return self.request("/getRankingInfo", **params)

    def get_live_info(self, **params):
        """Get live info. See docs/endpoints.md for parameters."""
        return self.request("/getLiveInfo", **params)

    def get_live_feed(self, **params):
        """Get live feed. See docs/endpoints.md for parameters."""
        return self.request("/getLiveFeed", **params)

