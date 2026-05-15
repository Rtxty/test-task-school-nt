import sys
import json

def fill_values(tests, values_dict):
    if isinstance(tests, dict):
        if "id" in tests and "value" in tests:
            if tests["id"] in values_dict:
                tests["value"] = values_dict[tests["id"]]
        for key in tests:
            fill_values(tests[key], values_dict)
    elif isinstance(tests, list):
        for item in tests:
            fill_values(item, values_dict)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    
    with open(values_path, 'r') as f:
        values_data = json.load(f)
    
    with open(tests_path, 'r') as f:
        tests_data = json.load(f)
    
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}
    
    fill_values(tests_data, values_dict)
    
    with open(report_path, 'w') as f:
        json.dump(tests_data, f, indent=2)
