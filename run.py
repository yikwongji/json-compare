import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def compare_json_keys(file1, file2):
    # Load the JSON data from both files
    data1 = load_json(file1)
    data2 = load_json(file2)

    # Get the keys from both JSON objects
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())

    # Find common keys
    common_keys = keys1.intersection(keys2)

    # Find keys that are not common
    unique_to_file1 = keys1 - keys2
    unique_to_file2 = keys2 - keys1

    # Check if all keys are common
    if not unique_to_file1 and not unique_to_file2:
        print("Both files have the same keys.")
    else:
        print("The files do not have the same keys.")
        if unique_to_file1:
            print(f"Keys unique to {file1}: {unique_to_file1}")
        if unique_to_file2:
            print(f"Keys unique to {file2}: {unique_to_file2}")

# Example usage
file1 = 'file1.json'
file2 = 'file2.json'
compare_json_keys(file1, file2)
