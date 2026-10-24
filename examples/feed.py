import os
from jsonscraper_instagram import Instagram
client = Instagram(os.environ["JSONSCRAPER_INSTAGRAM_LICENSE_KEY"])
response = client.request("/v1/user/medias/chunk", **{'user_id': '5821462185', 'end_cursor': '', 'cache_timeout': 60})
print(response)
