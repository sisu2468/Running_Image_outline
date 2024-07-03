import json
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt

# Function to load data from a JSON file
def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Load data from JSON file
data_file_path = 'contour_data1.json'
data = load_data_from_json(data_file_path)

# Separate the data into x and y coordinates
x = [point[0] for point in data]
y = [point[1] for point in data]

# # Sort the data points by x-value (optional, if needed)
# sorted_data = sorted(data, key=lambda point: point[0])
# x_sorted = [point[0] for point in sorted_data]
# y_sorted = [point[1] for point in sorted_data]

# Create a plot
plt.plot(x, y, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot from JSON Data Points')

# Save the plot to a file instead of showing it
plt.savefig('plot1.png')
