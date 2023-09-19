import cv2

# Read the solar system image
img = cv2.imread("solar-system.jpg")

# Define the font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # White color
font_thickness = 2

# Add the names of planets using putText
cv2.putText(img, "Mercury", (100, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Venus", (320, 430), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Earth", (550, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Mars", (800, 430), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Jupiter", (300, 700), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Saturn", (600, 680), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Uranus", (900, 700), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Neptune", (1200, 700), font, font_scale, font_color, font_thickness)

# Display the image with planet names
cv2.imshow("Solar System with Names", img)

# Save the final image with names
cv2.imwrite("Solar_system_with_names.jpg", img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
