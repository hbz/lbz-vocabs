import rdflib
import sys
import os

if not os.path.exists('output'):
   os.makedirs('output')

g = rdflib.Graph()

# Load file in format ttl
input_file = sys.argv[1]
g.parse("./%s" % input_file, format="ttl")

# SPARQL query for URI and label of each concept
qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?label ?concept ?definition
       WHERE {
           ?concept a skos:Concept ;
                skos:prefLabel ?label .
               OPTIONAL {?concept skos:definition ?definition}
       }""")

# Write results to file per line
with open("output/%s.ndjson" % input_file.replace(".ttl",""), "w") as output:
   for row in qres:
        if row.definition is not None:
           output.write("{\"prefLabel\":\"%s\",\"uri\":\"%s\",\"definition\":\"%s\"}\n" % row)
        else:
            row = row[0:2]
            output.write("{\"prefLabel\":\"%s\",\"uri\":\"%s\"}\n" % row)
