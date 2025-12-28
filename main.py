import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    
    
    
    if filter_type == "red":
        filtered_image[:, :, 0] = 0  # Zero out Blue
        filtered_image[:, :, 1] = 0  # Zero out Green
    elif filter_type == "green":
        filtered_image[:, :, 0] = 0  # Zero out Blue
        filtered_image[:, :, 2] = 0  # Zero out Red
    elif filter_type == "blue":
        filtered_image[:, :, 1] = 0  # Zero out Green
        filtered_image[:, :, 2] = 0  # Zero out Red
    elif filter_type == "magenta":
        filtered_image[:, :, 1] = 0  # Zero out Green (leaves Blue + Red)
    elif filter_type == "greyscale":
        
        filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
        
    
    return filtered_image

image_path = "mesirati.webp"
image = cv2.imread(image_path)

if image is None:
    print(f"Error loading image: '{image_path}'")
    print("Make sure the file exists in the correct path.")
else:
    filter_type = "original"
    print("Click the following keys to apply filters:")
    print("r - Red")
    print("g - Green")
    print("b - Blue")
    print("m - Magenta")
    print("s - Grayscale")
    print("o - Original")
    print("q - Quit")
    
    while True:
        if filter_type == "original":
            display_image = image.copy()
        else:
            display_image = apply_color_filter(image, filter_type)
            
        cv2.imshow("Image Filter", display_image)
        
        # FIXED: waitKey (capital K)
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord("r"):
            filter_type = "red"
        elif key == ord("g"):
            filter_type = "green"
        elif key == ord("b"):
            filter_type = "blue"
        elif key == ord("m"):
            filter_type = "magenta"
        elif key == ord("s"):
             filter_type = "greyscale"
        elif key == ord("o"): # FIXED: Changed "go" to "o"
            filter_type = "original"
        elif key == ord("q"):
             break
        else:
            print("Invalid key pressed")
            
    cv2.destroyAllWindows()
