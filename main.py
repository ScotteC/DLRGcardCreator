from weasyprint import HTML
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./template/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "card.html"
template = templateEnv.get_template(TEMPLATE_FILE)


person = {
        "name_last": "Hans",
        "name_first": "Martin",
        "birth_date": "01.04.1984",
        "street": "Erste Straße 17",
        "postcode": "52066",
        "city": "Aachen",
        "rank": "Bronze",
        "repetition": "",
        "first_registration": ""
}

course = {
    "id": "O-22-A1",
    "start": "15.08.2022",
    "end": "10.10.2022",
    "cost": "NFR",
    "trainer": "Fabian Schöttler, 09/181/056/08"
}

card = {
    "Bronze": [
        "200m Schwimmen in max 10min<br>"
            "(100m Bauchlage, 100m Rückenlage mit Grätschschwung ohne Armtätigkeit)",
        "100m Kleiderschwimmen in max 4min,<br>"
            "anschließend im Wasser entkleiden",
        "50m Transportschwimmen (Ziehen und Schieben)",
        "50m Schleppen (Fesselschleppgriff und Kopf- oder Achselschleppgriff)",
        "15m Streckentauchen",
        "2x 2-3m Tieftauchen in max 3min, davon 1x kopf- und 1x fußwärts<br>"
            "jeweils einen 5kg Tauchring heraufholen",
        "3 verschiedene Sprünge aus 1m Höhe (Kopfsprung, Fußsprung, Paketsprung)",
        "Fertigkeiten zur Vermeidung von Umklammerungen,<br>"
            "Befreiung aus Halsumklammerung und Halswürgegriff von hinten",
        "Kombinierte Übung",
        "Demonstration des Anlandbringens",
        "3min Vorführung der HLW",
        "Theoretische Prüfung",
    ],
    "Silber": [
        "400m Schwimmen in max 15min<br>"
            "(50m Kraul, 150m Brust, 200m Rücken mit Grätschschwung ohne Armtätigkeit)",
        "300m Kleiderschwimmen in max 12 Minuten,<br>"
            "anschließend im Wasser entkleiden",
        "50m Transportschwimmen in max 1:30min (Ziehen und Schieben)",
        "50m Schleppen in max 4min, beide Partner in Kleidung<br>"
            "(Fesselschleppgriff und Kopf- oder Achselschleppgriff)",
        "25m Streckentauchen",
        "3x 3-5m Tieftauchen in max 3min, davon 2x kopf- und 1x fußwärts<br>"
            "jeweils einen 5kg Tauchring heraufholen",
        "Sprung aus 3m Höhe",
        "Fertigkeiten zur Vermeidung von Umklammerungen,<br>"
            "Befreiung aus Halsumklammerung und Halswürgegriff von hinten",
        "Handhabung und praktischer Einsatz eines Rettungsgerät<br>"
            "(z.B. Gurtretter, Wurfleine, Rettungsball)",
        "Kombinierte Übung",
        "Theoretische Prüfung",
        "Erste-Hilfe Nachweis"
    ],
    "Gold": [
        "300m Flossenschwimmen in max 6min<br>"
            "(250m Bauch- oder Seitenlage, 50m Schleppen, Partner in Kleidung)",
        "300m Kleiderschwimmen in max 9min,<br>"
            "anschließend im Wasser entkleiden",
        "50m Transportschwimmen in max 1:30min, beide Partner bekleidet",
        "100m Schwimmen in max 1:40min",
        "30m Streckentauchen, dabei 8 von 10 Ringen aufsammeln",
        "3x 3-5m Tieftauchen in max 3min, 1. Kopfsprung, dann je 1x kopf- und fußwärts<br>"
            "jeweils zwei 5kg Tauchring heraufholen, in Bekleidung",
        "Fertigkeiten zur Vermeidung von Umklammerungen,<br>"
            "Befreiung aus Halsumklammerung und Halswürgegriff von hinten",
        "Kombinierte Übung",
        "Rettungsgeräte: a) Rettungsball: 6 Würfe in 5min, davon min 4 Treffer<br>"
            "b) Rettungsgurt mit Rettungsleine",
        "Hilfsmittel zur Wiederbelebung",
        "Theoretische Prüfung",
        "Erste-Hilfe Nachweis",
    ]
}

if __name__ == "__main__":
    sourceHtml = template.render(person=person, course=course, req=card[person["rank"]])

    html = HTML(string=sourceHtml, base_url="./")

    outputPath = "out/"
    outputFilename = "PK-DRSA-" + person["rank"] + "-" + course["id"] + "-" + person["name_first"] + person["name_last"] + ".pdf"

    html.write_pdf(outputPath + outputFilename)
