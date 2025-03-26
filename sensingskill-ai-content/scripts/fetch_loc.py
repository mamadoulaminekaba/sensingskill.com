#!/usr/bin/env python3
"""
fetch_loc.py
Fetch Library of Congress Subject Headings (LCSH) from LOC Linked Data Service.
"""

import requests
import json

# Example: LCSH base URL
base_url = "https://id.loc.gov/authorities/subjects/"
query = "Library Science"  # Change this keyword to fetch other subjects
params = {
    'q': query,
    'format': 'json'
}

# API endpoint (note: LOC has no formal API, this fetches example linked data)
response = requests.get(f"{base_url}.json")

if response.status_code == 200:
    data = response.json()
    with open("../datasets/loc_lis_subjects.json", "w") as outfile:
        json.dump(data, outfile, indent=2)
    print("✅ LOC LCSH data saved to ../datasets/loc_lis_subjects.json")
else:
    print(f"❌ Failed to fetch LOC LCSH data. Status code: {response.status_code}")

