import csv
import json

def csv2json(csvFilePath, jsonFilePath):
    json_array = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csv_reader = csv.DictReader(csvf) 

        for row in csv_reader: 
            json_array.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(json_array, indent=4)
        jsonf.write(jsonString)

    return jsonString
