import json

# Step 1: Load the JSON data
with open('contour_data.json', 'r') as file:
    data = json.load(file)

# Step 2: Sort the data
# Sort by the first element, then by the second element if the first elements are equal
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))

# Step 3: Optionally, convert the sorted data back to JSON and print or save it
sorted_data_json = json.dumps(sorted_data, indent=2)
print(sorted_data_json)

# If you want to save the sorted data back to a JSON file
with open('sorted_data.json', 'w') as file:
    file.write(sorted_data_json)
