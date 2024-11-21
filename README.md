# SKOS-Vokabulare des Landesbibliothekszentrums Rheinland-Pfalz

Dieses Repo enthält die vom Landesbibliothekszentrum erstellten und gepflegten SKOS-Vokabulare.

Hinweis: Das git-Repo wurde am 2024-08-28 geklont von https://github.com/hbz/lobid-vocabs, um ein dediziertes Repo für die LBZ-Vokabulare zu haben.


# Erstellen der NDJSON-Files 

1. In den Ordner `scripts` wechseln: `cd scripts/`
2. Skript ausführen mit `python3 skos2json.py <inputfile>.ttl` (ggf. auch `python skos2json.py <inputfile>.ttl`)
3. die erzeugten Dateien befinden sich im `Output`-Ordner

## Requirements
* python3
* rdflib