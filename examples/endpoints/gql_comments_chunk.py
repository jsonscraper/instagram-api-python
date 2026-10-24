#!/usr/bin/env python3
"""Get comments list by media ID (chunked).

Run: python examples/endpoints/gql_comments_chunk.py --help
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
    parser = argparse.ArgumentParser(description='Get comments list by media ID (chunked)\nGET /gql/comments/chunk\n\nEnvironment: JSONSCRAPER_INSTAGRAM_LICENSE_KEY\nCommon options: --timeout=30, --help\nQuery options:\n  --media_id=VALUE  IG media ID.\n  --sort_order=VALUE  Sorting mode. Allowed: recent, popular\n  --end_cursor=VALUE  Cursor for the next page. Use the end_cursor value from the previous response.\n  --cache_timeout=VALUE  Caching is disabled by default. Set a value greater than 0 to enable response caching for the specified number of seconds; repeated requests within this window will be served from \n\nValues omitted from the command use the public Postman sample defaults. Replace IDs/URLs with your own inputs. Each run makes one request; live requests may consume quota.', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--timeout", type=float, default=30, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=0, help="Optional retries, 0 to 5; may consume quota")
    parser.add_argument("--output", help="Save binary/JSON response to this file instead of standard output")
    parser.add_argument("--media_id", default='3816481912765155592', help='IG media ID.')
    parser.add_argument("--sort_order", default=None, help='Sorting mode. Allowed: recent, popular')
    parser.add_argument("--end_cursor", default=None, help='Cursor for the next page. Use the end_cursor value from the previous response.')
    parser.add_argument("--cache_timeout", default='60', help='Caching is disabled by default. Set a value greater than 0 to enable response caching for the specified number of seconds; repeated requests within this window will be served from ')
    args = parser.parse_args()
    key = os.environ.get("JSONSCRAPER_INSTAGRAM_LICENSE_KEY", "").strip()
    if not key:
        parser.error("Set JSONSCRAPER_INSTAGRAM_LICENSE_KEY before making a licensed request")
    if args.timeout <= 0 or not 0 <= args.retries <= 5:
        parser.error("Use a positive timeout and 0 to 5 retries")
    try:
        client = Instagram(key, timeout=args.timeout, retries=args.retries)
        response = client.gql_comments_chunk(media_id=args.media_id, sort_order=args.sort_order, end_cursor=args.end_cursor, cache_timeout=args.cache_timeout)
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
