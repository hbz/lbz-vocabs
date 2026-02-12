# SKOS-Vokabulare des Landesbibliothekszentrums Rheinland-Pfalz

Dieses Repo enthält die vom Landesbibliothekszentrum erstellten und gepflegten SKOS-Vokabulare. Zur Arbeit mit den SKOS-Dateien siehe [diese Anleitung](https://github.com/hbz/lobid-vocabs/blob/master/how-to-edit/guide.md) zum Editieren und Committen von Änderungen.

Hinweis: Das git-Repo wurde am 2024-08-28 geklont von https://github.com/hbz/lobid-vocabs, um ein dediziertes Repo für die LBZ-Vokabulare zu haben.


## Erstellen der NDJSON-Files 

1. Skript ausführen mit `python3 scripts/skos2json.py <inputfile>.ttl` (ggf. auch `python scripts/skos2json.py <inputfile>.ttl`)
2. die erzeugten Dateien befinden sich im `output`-Ordner

## Requirements
* python3
* rdflib

## Titel mit fehlerhaft erfassten LBZ-Notationen, RPB-Sach‐ und Raumnotationen

Wenn bei Verbund-Titeln LBZ-Notationen oder RPB-Sach- oder Raumnotationen falsch erfasst werden, führt es dazu, dass keine passenden Labels in lobid-resources übernommen werden können.

Mit folgenden Abfragen kann man nach die fehlerhaften Titel suchen: 

- LBZ-Notationen: [subject.label:"https://w3id.org/lobid/rpb2*"](https://lobid.org/resources/search?q=subject.label%3A%22https%3A%2F%2Fw3id.org%2Flobid%2Frpb2*%22)
- RPB-Sachsystematik: [subject.label:"http://purl.org/lobid/rpb*"](https://lobid.org/resources/search?q=subject.label%3A%22http%3A%2F%2Fpurl.org%2Flobid%2Frpb%22)
- RPB-Raumsystematik: [spatial.label:"https://rpb.lobid.org/spatial*"](https://lobid.org/resources/search?q=spatial.label%3A+%22https%3A%2F%2Frpb.lobid.org%2Fspatial*%22)

Die fehlerhaften Notationen müssen im Feld 084 entsprechend angepasst werden.

Auf den Detailseiten erkennt man die fehlerhaften Einträge durch die URL anstelle des Konzepts:

<img width="867" height="695" alt="image" src="https://github.com/user-attachments/assets/663ecc9f-0bc1-41ba-842d-0100eb88f59f" />

