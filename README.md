# SKOS-Vokabulare des Landesbibliothekszentrums Rheinland-Pfalz

Dieses Repo enthält die vom Landesbibliothekszentrum erstellten und gepflegten SKOS-Vokabulare. Zur Arbeit mit den SKOS-Dateien siehe [diese Anleitung](https://github.com/hbz/lobid-vocabs/blob/master/how-to-edit/guide.md) zum Editieren und Committen von Änderungen.

Hinweis: Das git-Repo wurde am 2024-08-28 geklont von https://github.com/hbz/lobid-vocabs, um ein dediziertes Repo für die LBZ-Vokabulare zu haben.


## Erstellen der NDJSON-Files 

1. Skript ausführen mit `python3 scripts/skos2json.py <inputfile>.ttl` (ggf. auch `python scripts/skos2json.py <inputfile>.ttl`)
2. die erzeugten Dateien befinden sich im `output`-Ordner

## Automatische Generierung bei Änderungen

Bei einem Push auf den `main`- oder `dev`-Branch wird automatisch geprüft, ob sich eine oder mehrere `.ttl`-Dateien geändert haben. Falls ja, wird das Skript für diese Dateien ausgeführt und die resultierenden `.ndjson`-Dateien direkt im Repository committed und gepusht. Die Umsetzung erfolgt über die GitHub Action in [.github/workflows/generate-ndjson.yml](.github/workflows/generate-ndjson.yml). In den Einstellungen des Repos unter [https://github.com/hbz/lbz-vocabs/settings/actions](https://github.com/hbz/lbz-vocabs/settings/actions) müssen im Abschnitt "Workflow permissions" die "Read and write permissions" gesetzt sein. 

## Requirements
* python3
* rdflib

