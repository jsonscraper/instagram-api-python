import os
from jsonscraper_instagram import Instagram
client = Instagram(os.environ["JSONSCRAPER_INSTAGRAM_LICENSE_KEY"])
response = client.request("/v1/media/by/code", **{'code': 'DT23hQ-EgkI', 'cache_timeout': 60})
print(response)
