import os
import json

# Assuming the labeling data is structured with a root folder containing 'Day' and 'Night' folders.
# Each of these folders contain multiple sub-folders, and inside them are JSON files.

# Define the path to the root of the labeling data
root_path = 'C:/Users/gjaischool/study_is_good/final_project/adas_data/validation_data/라벨링데이터/주간/주간_성남02'  # Replace this with the actual root path if it's different

# Function to search for the JSON file containing the term "전동이동체"
def find_file_with_term(root_path, term):
    for subdir, dirs, files in os.walk(root_path):
        for file in files:
            # We're only interested in '.json' files.
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                # Open and load the json file.
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Search for the term in the json data.
                    if term in json.dumps(data, ensure_ascii=False):
                        return file_path  # If found, return the path to the file.
    # If the term wasn't found in any file, return None.
    return None

search_term = "전동이동체"  # The term we're looking for in the .json files.

# Call the function and print the result.
found_file_path = find_file_with_term(root_path, search_term)

if found_file_path:
    print(f'Found file with term "{search_term}": {found_file_path}')
else:
    print(f'No file containing the term "{search_term}" was found.')
