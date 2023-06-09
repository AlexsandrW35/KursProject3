import json

file_name = "../data/operations.json"
def load_json(file_name):
    with open(file_name, "r",encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data

load_json(file_name)

print(load_json(file_name))
