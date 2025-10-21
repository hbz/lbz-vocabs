# SKOS-Vokabulare des Landesbibliothekszentrums Rheinland-Pfalz

Dieses Repo enthält die vom Landesbibliothekszentrum erstellten und gepflegten SKOS-Vokabulare. Zur Arbeit mit den SKOS-Datien siehe [diese Anleitung](https://github.com/hbz/lobid-vocabs/blob/master/how-to-edit/guide.md) zum Editieren und Committen von Änderungen.

Hinweis: Das git-Repo wurde am 2024-08-28 geklont von https://github.com/hbz/lobid-vocabs, um ein dediziertes Repo für die LBZ-Vokabulare zu haben.


# Erstellen der NDJSON-Files 

1. Skript ausführen mit `python3 scripts/skos2json.py <inputfile>.ttl` (ggf. auch `python scripts/skos2json.py <inputfile>.ttl`)
2. die erzeugten Dateien befinden sich im `output`-Ordner

## Requirements
* python3

* rdflib
