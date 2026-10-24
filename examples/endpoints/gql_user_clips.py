#!/usr/bin/env python3
"""Get user clips (reels).

Run: python examples/endpoints/gql_user_clips.py --help
Requires an installed jsonscraper-instagram package and JSONSCRAPER_INSTAGRAM_LICENSE_KEY.
The example makes one request and prints the full API envelope.
"""
import argparse
import json
import os
import sys
from pathlib import Path
from jsonscraper_instagram import Instagram, APIError, TransportError


def main():
    parser = argparse.ArgumentParser(description='Get user clips (reels)\nGET /gql/user/clips\n\nEnvironment: JSONSCRAPER_INSTAGRAM_LICENSE_KEY\nCommon options: --timeout=30, --help\nQuery options:\n  --user_id=VALUE  Target user ID.\n  --max_id=VALUE  Cursor for the next page. Use the max_id value from the previous response.\n  --sort_by_views=VALUE  If true, clips will be sorted by view count (typically descending).\n  --flat=VALUE  If true, returns clips in a flattened list format.\n  --cache_timeout=VALUE  Caching is disabled by default. Set a value greater than 0 to enable response caching for the specified number of seconds; repeated requests within this window will be served from \n\nValues omitted from the command use the public Postman sample defaults. Replace IDs/URLs with your own inputs. Each run makes one request; live requests may consume quota.', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--timeout", type=float, default=30, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=0, help="Optional retries, 0 to 5; may consume quota")
    parser.add_argument("--output", help="Save binary/JSON response to this file instead of standard output")
    parser.add_argument("--user_id", default='1107766105', help='Target user ID.')
    parser.add_argument("--max_id", default=None, help='Cursor for the next page. Use the max_id value from the previous response.')
    parser.add_argument("--sort_by_views", default=None, help='If true, clips will be sorted by view count (typically descending).')
    parser.add_argument("--flat", default=None, help='If true, returns clips in a flattened list format.')
    parser.add_argument("--cache_timeout", default='60', help='Caching is disabled by default. Set a value greater than 0 to enable response caching for the specified number of seconds; repeated requests within this window will be served from ')
    args = parser.parse_args()
    key = os.environ.get("JSONSCRAPER_INSTAGRAM_LICENSE_KEY", "").strip()
    if not key:
        parser.error("Set JSONSCRAPER_INSTAGRAM_LICENSE_KEY before making a licensed request")
    if args.timeout <= 0 or not 0 <= args.retries <= 5:
        parser.error("Use a positive timeout and 0 to 5 retries")
    try:
        client = Instagram(key, timeout=args.timeout, retries=args.retries)
        response = client.gql_user_clips(user_id=args.user_id, max_id=args.max_id, sort_by_views=args.sort_by_views, flat=args.flat, cache_timeout=args.cache_timeout)
        if isinstance(response, bytes):
            if not args.output:
                parser.error("Binary response: provide --output=filename")
            Path(args.output).write_bytes(response)
            return 0
        if not isinstance(response, dict) or response.get("status") != "ok":
            print("The API returned an application error. Inspect the envelope below.", file=sys.stderr)
            print(json.dumps(response, ensure_ascii=False, indent=2))
            return 1
        if response.get("rate_limit_reached"):
            print("The API reports that the license rate limit was reached.", file=sys.stderr)
            return 1
        rendered = json.dumps(response, ensure_ascii=False, indent=2)
        if args.output:
            Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        else:
            print(rendered)
        return 0
    except APIError as error:
        print(f"HTTP {error.status}. Check parameters, access and quota. Retry-After: {error.retry_after or 'not provided'}", file=sys.stderr)
        return 1
    except (TransportError, ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
