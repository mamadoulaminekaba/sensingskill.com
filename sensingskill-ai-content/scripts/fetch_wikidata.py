#!/usr/bin/env python3
"""
fetch_wikidata.py
Fetch LIS-related entities from Wikidata using SPARQL.
"""

from SPARQLWrapper import SPARQLWrapper, JSON
import json

# Set the SPARQL endpoint
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

# Example query: Fetch library science entities and their descriptions
query = """
SELECT ?item ?itemLabel ?description
WHERE {
  ?item wdt:P31 wd:Q18610173.  # Q18610173 = field of study
  ?item rdfs:label ?itemLabel.
  ?item schema:description ?description.
  FILTER (LANG(?itemLabel) = "en")
  FILTER (LANG(?description) = "en")
}
LIMIT 50
"""

sparql.setQuery(query)
sparql.setReturnFormat(JSON)

# Execute query and fetch results
results = sparql.query().convert()

# Write to JSON file
with open("../datasets/wikidata_lis_entities.json", "w") as outfile:
    json.dump(results, outfile, indent=2)

print("✅ Wikidata LIS entities fetched and saved to ../datasets/wikidata_lis_entities.json")
