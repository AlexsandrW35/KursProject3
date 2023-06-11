from utils.servise import load_json,filter_data,get_succesful_operations,sort_by_date,print_info

def main():
    json_raw_data = load_json()
    json_data = filter_data(json_raw_data)
    sorted_operation = sort_by_date(json_data)
    last_five_operations = get_succesful_operations(sorted_operation)
    print_info(last_five_operations)

main()