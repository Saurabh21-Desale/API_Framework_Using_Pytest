import csv
import json


# csv_file = r'C:\Users\saurabhd\pythonProject\API_Framework_Using_Pytest\api_framework\test\test_data\csv_data.csv'
# json_file = r'C:\Users\saurabhd\pythonProject\API_Framework_Using_Pytest\api_framework\test\test_data\csv_json_data.json'

class CsvToJsonFile(object):

    def __init__(self):
        self.data = []

    def convert_csv_to_json(self, csv_file, json_file):
        print("third")
        with open(csv_file, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                self.data.append(rows)

        with open(json_file, 'w', encoding='utf-8') as jsonf:
            jsonf.write('{')
            jsonf.write('"test_data":')
            json_string = json.dumps(self.data, indent=4)
            jsonf.write(json_string)
            jsonf.write('}')
            # jsonf.close()
            # csvf.close()
