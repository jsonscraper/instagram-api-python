import os
from jsonscraper_instagram import Instagram
client = Instagram(os.environ["JSONSCRAPER_INSTAGRAM_LICENSE_KEY"])
response = client.request("/v1/search/users", **{'query': 'apple', 'cache_timeout': 60})
print(response)
