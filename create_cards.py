import csv
import jinja2
from weasyprint import HTML

templateLoader = jinja2.FileSystemLoader(searchpath="./template/")
templateEnv = jinja2.Environment(loader=templateLoader)


exams = {
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


def create_drsa_cards(data, course, target_path):
    # source file for mail merge
    mail_info = ["name_first", "name_last", "mail", "start", "pool", "day",
                 "time_water", "time_gather", "time_entrance", "contact", "card"]
    mail_data = []

    template = templateEnv.get_template("exam_card.html")

    for person in data:
        source_html = template.render(person=person, course=course, req=exams[person["rank"]])
        html = HTML(string=source_html, base_url="./")

        output_filename = "PK-DRSA-" + person["rank"] + "-" + course["id"] + "-" + person["name_first"] + person["name_last"] + ".pdf"

        html.write_pdf("{path}/{file}".format(path=target_path, file=output_filename))

        # data for mail-merge
        mail_data.append({
            "name_last": person["name_last"],
            "name_first": person["name_first"],
            "mail": person["mail"],
            "start": course["start"],
            "pool": course["pool"],
            "day": course["day"],
            "time_water": course["time_water"],
            "time_gather": course["time_gather"],
            "time_entrance": course["time_entrance"],
            "contact": course["contact"],
            "card": output_filename
        })

    mail_out = "{path}/Mail-{course}.csv".format(
        path=target_path, course=course["id"])

    with open(mail_out, "w", newline='', encoding='utf_8') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=mail_info, delimiter=';')
        writer.writeheader()
        writer.writerows(mail_data)


def create_course_card():
    course = {
        "id": "TestCourse",
        "pool": "Testhalle"
    }
    rank = "Bronze"

    template = templateEnv.get_template("course_card.html")
    source_html = template.render(course=course, req=exams[rank], rank=rank)
    html = HTML(string=source_html, base_url="./")

    output_filename = "RK-DRSA-" + rank + "-" + course["id"] + ".pdf"
    html.write_pdf("{path}/{file}".format(path='./out', file=output_filename))


if __name__ == "__main__":
    create_course_card()
