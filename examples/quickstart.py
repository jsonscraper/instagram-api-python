import os
from jsonscraper import Instagram, TikTok, APIError

ig = Instagram(os.environ["JSONSCRAPER_INSTAGRAM_LICENSE_KEY"], timeout=30, retries=1)
profile = ig.v1_user_by_username(username="apple", cache_timeout=60)
print(profile)

tiktok = TikTok(os.environ["JSONSCRAPER_TIKTOK_LICENSE_KEY"])
video = tiktok.get_video_by_id(video_id="7106855913906081070", cache_timeout=60)
print(video["tiktok"]["aweme_detail"]["aweme_id"])
