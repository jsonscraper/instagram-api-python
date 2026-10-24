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
