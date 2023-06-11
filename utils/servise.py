import json
from datetime import datetime as dt

def load_json(path= '../data/operations.json'):
    with open(path, "r",encoding="utf-8") as f:
        json_dict = json.load(f)
        return json_dict

def filter_data(data):
    return [item for item in data if item]

def date_format(data_str):
    parsed = dt.strptime(data_str, "%Y-%m-%dT%H:%M:%S.%f")
    return parsed.strftime('%d.%m.%Y')

def get_succesful_operations(data):
    succesful_operations = [op for op in data if op["state"] == "EXECUTED"]
    return succesful_operations[:5]

def sort_by_date(data):
    return sorted(data, key=lambda x: x.get("date"), reverse=True)

def mask_card(operation_credentials):
    if operation_credentials:
        credentials_name = " ".join(operation_credentials.split(" ")[:-1]) # Visa classic
        credentials_number = operation_credentials.split(" ")[-1] # 6831982476737658

        if len(credentials_number) == 16:

            number_hide = credentials_number[:6] + "*" * 6 +credentials_number[-4:]  #683198******7658
            number_sep = [number_hide[i:i + 4] for i in range(0, len(credentials_number), 4)]  #6831 98** **** 7658

            return  f"{credentials_name} {' '.join(number_sep)}" # Visa Classic 6831 98******7658

        elif len(credentials_number) == 20:

            return f"{credentials_name} {credentials_number.replace(credentials_number[:-4], '**')}"

    return "N/A"

def print_info(operations):

    for op in operations:
        print(f"{date_format(op['date'])} {op['description']}"
              f"{mask_card(op.get('from'))} -> {mask_card(op.get('to'))}\n"
              f"{op['operationAmount'].get('amount')} {op['operationAmount'].get('currency')['code']}\n")
