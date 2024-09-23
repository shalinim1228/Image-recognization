import cv2

# Load the image
img = cv2.imread("images.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load the image.")
    exit()

# Get desired dimensions from user
h = int(input("Enter height: "))
w = int(input("Enter width: "))

# Resize the image
resize = cv2.resize(img, (w, h))  # Note: (width, height) order

# Display the resized image
cv2.imshow("Resized Image", resize)

# Convert the original image to grayscale
face1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("bw.jpg", face1)

# Wait for a key press indefinitely or for a specified amount of time
cv2.waitKey(0)  # Change to 0 to wait indefinitely

# Clean up windows
cv2.destroyAllWindows()
