import csv
import datetime
import re
from os.path import exists


def create_stamp_list(data, target_path):
    entry_info = ["NAME", "ZUSATZ", "STRASSE", "NUMMER", "PLZ", "STADT", "LAND", "ADRESS_TYP"]
    sender = {
        "NAME": "Max Muster",
        "ZUSATZ": "",
        "STRASSE": "Musterstraße",
        "NUMMER": "11A",
        "PLZ": "12345",
        "STADT": "Einestadt",
        "LAND": "DEU",
        "ADRESS_TYP": "HOUSE"
    }
    if exists('./instance/local.py'):
        from instance.local import local_sender
        sender = local_sender()

    # postcode_regex = [
    #     {"RE": r"(?<=^)(\d{5})(?=[\W]*$)", "CODE": "DEU"},                  # germany
    #     {"RE": r"(?<=^)(\d{4}\s*[a-zA-Z]{2})(?=[\W]*$)", "CODE": "NL"},     # netherlands
    #     {"RE": r"(?<=^)(\d{4})(?=[\W]*$)", "CODE": "BE"}                    # belgium
    # ]

    data_national = []
    data_international = []
    for person in data:
        street = ""
        number = ""
        m = re.match(r"(.*?)\s*(\d+\w*(?:[/-]\d+\w*)?)?$", person["street"])
        if m:
            street, number = m.groups()
            if not number:
                number = ""

        postcode_raw = person["postcode"]
        postcode = postcode_raw
        # country = ""
        # for regex in postcode_regex:
        #     c = re.match(regex["RE"], postcode_raw)
        #     if m:
        #         postcode = c.group()
        #         country = regex["CODE"]
        #         break

        entry = {
            "NAME": "{first} {last}".format(first=person["name_first"], last=person["name_last"]),
            "ZUSATZ": "",
            "STRASSE": street,
            "NUMMER": number,
            "PLZ": postcode,
            "STADT": person["city"],
            "LAND": person["country"],
            "ADRESS_TYP": "HOUSE"
        }

        data_national.append(entry)

        # if entry["LAND"] == "DEU":
        #     data_national.append(entry)
        # else:
        #     data_international.append(entry)

    today = datetime.datetime.now().date()

    out_nat = "{path}/Marken-national-{year}-{month:02d}-{day:02d}.csv".format(
        path=target_path,
        year=today.year, month=today.month, day=today.day)

    # out_int = "{path}/Marken-international-{year}-{month:02d}-{day:02d}.csv".format(
    #     path=target_path,
    #     year=today.year, month=today.month, day=today.day)

    with open(out_nat, "w", newline='') as csv_national:
        writer = csv.DictWriter(csv_national, fieldnames=entry_info, delimiter=';')
        writer.writeheader()
        writer.writerow(sender)
        writer.writerows(data_national)

    # with open(out_int, "w", newline='') as csv_international:
    #     writer = csv.DictWriter(csv_international, fieldnames=entry_info, delimiter=';')
    #     writer.writeheader()
    #     writer.writerow(sender)
    #     writer.writerows(data_international)


def create_registration_list(data, course, target_path):
    entry_info = ["RSw", "Halle", "Kursbeginn", "Vorname", "Nachname", "Straße", "Land", "PLZ", "Wohnort", "GebDatum",
                  "GebOrt", "Telefon", "E-Mail", "Grund", "Eltern-Ort", "Eltern-Datum", "Prüfer", "LehrscheinNr"]

    data_out = []
    for person in data:
        entry = {
            "RSw": person["rank"],
            "Halle": course["pool"],
            "Kursbeginn": "",
            "Vorname": person["name_first"],
            "Nachname": person["name_last"],
            "Straße": person["street"],
            "Land": person["country"],
            "PLZ": person["postcode"],
            "Wohnort": person["city"],
            "GebDatum": person["birth_date"],
            "GebOrt": "",
            "Telefon": "",
            "E-Mail": "",
            "Grund": "",
            "Eltern-Ort": "",
            "Eltern-Datum": "",
            "Prüfer": course["trainer_name"],
            "LehrscheinNr": course["trainer_licence"]
        }
        data_out.append(entry)

    today = datetime.datetime.now().date()

    file_out = "{path}/DRSA-Registration-{year}-{month:02d}-{day:02d}.csv".format(
        path=target_path,
        year=today.year, month=today.month, day=today.day)

    with open(file_out, "w", newline='', encoding='utf_8_sig') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=entry_info, delimiter=';')
        writer.writeheader()
        writer.writerows(data_out)
