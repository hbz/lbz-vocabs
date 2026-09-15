import rdflib
import sys
import os
import argparse

if not os.path.exists('output'):
   os.makedirs('output')

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to the input Turtle file")
parser.add_argument(
    "--no-top-levels",
    action="store_true",
    help="Include skos:broader in the SPARQL query",
)
args = parser.parse_args()

input_file = args.input_file
no_top_levels = args.no_top_levels

g = rdflib.Graph()

# Load file in format ttl
g.parse(input_file, format="ttl")

# SPARQL query for URI and label of each concept
predicate_pattern = f'skos:prefLabel ?label {"; skos:broader ?broader" if no_top_levels else ""} .'

query = f"""
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?label ?concept ?definition
       WHERE {{
           ?concept a skos:Concept ;
                {predicate_pattern}
           OPTIONAL {{?concept skos:definition ?definition}}
       }}
"""

qres = g.query(query)

# Write results to file per line
with open("output/%s.ndjson" % input_file.replace(".ttl",""), "w") as output:
   for row in qres:
        if row.definition is not None:
           output.write("{\"prefLabel\":\"%s\",\"uri\":\"%s\",\"definition\":\"%s\"}\n" % row)
        else:
            row = row[0:2]
            output.write("{\"prefLabel\":\"%s\",\"uri\":\"%s\"}\n" % row)
