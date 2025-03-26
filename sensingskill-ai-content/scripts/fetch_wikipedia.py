#!/usr/bin/env python3

"""
Wikipedia Fetcher for SensingSkill.com AI Pipeline
Pulls structured content from Wikipedia based on a search term.
"""

import requests
import json
import sys

def fetch_wikipedia_summary(topic):
    """
    Fetches the summary section of a Wikipedia page.
    """
    endpoint = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title"),
            "extract": data.get("extract"),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page")
        }
    else:
        print(f"❌ Failed to fetch {topic}: {response.status_code}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_wikipedia.py 'Search_Term'")
        sys.exit(1)

    search_term = sys.argv[1].replace(' ', '_')
    result = fetch_wikipedia_summary(search_term)
    if result:
        print(json.dumps(result, indent=4, ensure_ascii=False))
