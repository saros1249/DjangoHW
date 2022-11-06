import csv
import json

CSV_ADS = "ads.csv"
JSON_ADS = "ads.json"
CSV_CATEGORIES = "categories.csv"
JSON_CATEGORIES = "categories.json"
CSV_LOCATION = "location.csv"
JSON_LOCATION = "location.json"
CSV_USER = "user.csv"
JSON_USER = "user.json"


def csv_to_json(csv_file, json_file, model_name):
    json_list = []

    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            to_add = {'model': model_name, 'pk': int(row['Id']) if 'Id' in row else row['id']}
            if 'Id' in row:
                del row['Id']
            else:
                del row["id"]
            if "is_published" in row:
                if row["is_published"] == 'TRUE':
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "age" in row:
                row["age"] = int(row["age"])
            if "location_id" in row:
                row["location_id"] = int(row["location_id"])
            to_add['fields'] = row
            json_list.append(to_add)


    with open(json_file, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(json_list, ensure_ascii=False, indent=4)
        jsonf.write(json_string)


csv_to_json(CSV_ADS, JSON_ADS, 'ads.ads')
csv_to_json(CSV_CATEGORIES, JSON_CATEGORIES, 'ads.categories')
csv_to_json(CSV_LOCATION, JSON_LOCATION, 'users.location')
csv_to_json(CSV_USER, JSON_USER, 'users.user')
