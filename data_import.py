import re
from openpyxl import *


def data_from_isc_seminar(filename, ) -> []:
    data = []

    wb = load_workbook(filename=filename)
    sheet = wb['Worksheet']

    # Create a dictionary of column names
    columns = {}
    index = 0
    for COL in sheet.iter_cols(1, sheet.max_column):
        columns[COL[0].value] = index
        index += 1

    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append({
            "name_last": str(row[columns["Nachname"]]).strip(),
            "name_first": str(row[columns["Vorname"]]).strip(),
            "birth_date": str(row[columns["Geb.Dat"]]).strip(),
            "street": str(row[columns["Strasse"]]).strip(),
            "postcode": str(row[columns["Plz"]]).strip(),
            "city": str(row[columns["Ort"]]).strip(),
            "country": "DEU",
            "mail": str(row[columns["E-Mail"]]).strip().lower(),
            "rank": str(re.findall("Bronze|Silber", row[columns["Gewünschtes Abzeichen"]])[0]).strip(),
            "repetition": "",
            "first_registration": ""
        })

    return data


def data_from_group_register(filename) -> []:
    data = []

    ranks = ["Bronze", "Silber", "Gold"]

    wb = load_workbook(filename=filename)

    for rank in ranks:
        sheet = wb[rank]
        # Create a dictionary of column names
        columns = {}
        index = 0
        for COL in sheet.iter_cols(1, sheet.max_column):
            columns[COL[0].value] = index
            index += 1

        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append({
                "name_last": str(row[columns["Nachname"]]).strip(),
                "name_first": str(row[columns["Vorname"]]).strip(),
                "birth_date": str(row[columns["GebDatum"]]).strip(),
                "street": str(row[columns["Straße"]]).strip(),
                "postcode": str(row[columns["PLZ"]]).strip(),
                "city": str(row[columns["Wohnort"]]).strip(),
                "country": "DEU",
                "mail": str(row[columns["E-Mail"]]).strip().lower(),
                "rank": rank,
                "repetition": "",
                "first_registration": ""
            })
    return data
