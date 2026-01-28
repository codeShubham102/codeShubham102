
import cv2

# Load the image
img = cv2.imread('C:\\Users\\shubh\\Desktop\\cv\\Screenshot_20260128_130143_YouTube.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY) # Clear the background
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # Approximate the shape
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    
    # Get coordinates to place the text
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    # Logic to identify shape based on number of vertices (corners)
    num_corners = len(approx)

    if num_corners == 3:
        shape_name = "Triangle"
    elif num_corners == 4:
        shape_name = "Quadrilateral"
    elif num_corners == 5:
        shape_name = "Pentagon"
    elif num_corners == 6:
        shape_name = "Hexagon"
    else:
        shape_name = "Circle"

    # Draw the text on the image
    cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv2.imshow("Shape Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()