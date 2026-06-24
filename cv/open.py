import cv2

# Load the image (ensure 'image.jpg' is in your folder)
img = cv2.imread('C:\\Users\\shubh\\Desktop\\cv\\Screenshot_20260128_130143_YouTube.jpg')

# Check if image was loaded correctly
if img is not None:
    # Display the image in a window titled 'Output Window'
    cv2.imshow('Output Window', img)
    
    print("Image displayed successfully. Press any key to close.")
    
    # Wait for a key press to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image file not found!")
