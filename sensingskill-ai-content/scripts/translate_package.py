#!/usr/bin/env python3

import openai  # or use Google Translate API / any LLM translation model
import json
import os
from datetime import datetime

# Load OpenAI or translation API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Input: JSON knowledge package file
input_file = "../datasets/generated_package_sample.json"
with open(input_file, "r") as f:
    package = json.load(f)

# Target language (can loop later for multiple)
target_language = "French"

# Construct translation prompt
prompt = f"""
Translate the following LIS knowledge package content into {target_language}:
{package['ai_generated_content']['summary']}

✅ Ensure accuracy of LIS-specific terms like MARC, PREMIS, Dublin Core
✅ Do not translate technical metadata model names
✅ Maintain structured formatting
"""

# GPT translation API call
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "system", "content": "You are a professional academic translator specialized in Library and Information Science."},
              {"role": "user", "content": prompt}],
    temperature=0.1
)

# Store the translated content
package["translated"] = {
    "language": target_language,
    "content": response['choices'][0]['message']['content']
}

# Save translated output
output_file = f"../datasets/translated_package_{target_language.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(output_file, "w") as outfile:
    json.dump(package, outfile, indent=4)

print(f"✅ Translated package saved: {output_file}")
