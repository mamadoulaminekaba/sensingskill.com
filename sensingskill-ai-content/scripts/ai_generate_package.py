#!/usr/bin/env python3

import openai  # or import anthropic if using Claude
import json
import os
from datetime import datetime

# CONFIGURE YOUR OPENAI or CLAUDE KEY
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set as environment variable

# Load the dataset template
template_path = "../templates/knowledge_package_template.json"
with open(template_path, "r") as template_file:
    package = json.load(template_file)

# Populate metadata (example)
package["title"] = "Metadata for Digital Preservation"
package["description"] = "Step-by-step guide to generate preservation metadata."
package["library_type"] = "Archives"
package["workflow_stage"] = "Metadata creation"
package["metadata_models"] = ["PREMIS", "METS"]
package["data_sources"] = ["Wikipedia", "LOC"]
package["keywords"] = ["preservation", "metadata", "PREMIS", "digital archives"]
package["generation_timestamp"] = datetime.now().isoformat()

# Construct the GPT/Claude prompt dynamically
prompt = f"""
You are a Library and Information Science (LIS) expert.

Generate a detailed, step-by-step workflow for:
Title: {package['title']}
Description: {package['description']}
Library Type: {package['library_type']}
Metadata Models: {', '.join(package['metadata_models'])}
Data Sources: {', '.join(package['data_sources'])}

Include:
✅ Clear LIS workflow steps
✅ Metadata examples
✅ Suggested controlled vocabularies
✅ Suggested visual aids or diagrams
"""

# GPT or Claude call
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "system", "content": "You are a helpful LIS knowledge engineer."},
              {"role": "user", "content": prompt}],
    temperature=0.2
)

# Store AI-generated content
package["ai_generated_content"]["summary"] = response['choices'][0]['message']['content']

# Output JSON file
output_file = f"../datasets/generated_package_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(output_file, "w") as outfile:
    json.dump(package, outfile, indent=4)

print(f"✅ AI Knowledge Package generated: {output_file}")
