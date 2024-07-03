import cv2 
import numpy as np 
import json

# Read the image
img = cv2.imread("running1 - Copy.png")

# Resize the image
image = cv2.resize(img, (700, 600)) 

# Convert image to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

# Define HSV range for the white ball
white_lower = np.array([0, 190, 0])   # Lower bound for hue, saturation, and value
white_upper = np.array([255, 255, 255]) # Upper bound for hue, saturation, and value

# Define the mask for detecting color 
mask = cv2.inRange(hsv, white_lower, white_upper) 

# Find contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Prepare contour data for JSON
contour_data = []
# Draw circle around the contour
ii= 0 
# print("contour[0]", contours)

for contour in contours:
    for point in contour:
        contour_data.append(point[0].tolist())
        # print("point[0]", point[0])
        cv2.circle(image, tuple(point[0]), 1, (0, 0, 0), 2)
    
print(contour_data) 
# Export contour data to JSON
with open('contour_data1.json', 'w') as f:
    json.dump(contour_data, f)

# Display image with contours and circle
cv2.imshow("Contours with Circle", image)

# Wait for any key to be pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
