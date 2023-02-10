import csv
import json


class CsvToJsonFile(object):

    def convert_csv_to_json(self, csv_file, json_file):
        data = []

        with open(csv_file, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                data.append(rows)

        with open(json_file, 'w', encoding='utf-8') as jsonf:
            jsonf.write('{')
            jsonf.write('"test_data":')
            json_string = json.dumps(data, indent=4)
            jsonf.write(json_string)
            jsonf.write('}')
