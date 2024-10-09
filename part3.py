#Part 3: Data Handling and Augmented Reality Integration

#Task: Write a Python script to simulate the integration of detected objects with augmented 
#reality by overlaying text on images.

# Import necessary libraries
import cv2
import numpy as np

# Function to overlay text and draw bounding boxes on an image
def overlay_text(image, box, text):
    """
    To draw a bounding box around the detected object and overlay text.

    Parameters:
    - image: The image on which to draw.
    - box: A tuple (x, y, w, h) representing the bounding box coordinates.
    - text: The text to overlay on the bounding box.
    """
    # Unpack the coordinates and size of the bounding box
    x, y, w, h = box

    # Draw a rectangle around the detected object (bounding box)
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Place text above the bounding box indicating the object's label or name
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Function to simulate a color-changing AR effect on the bounding box
def color_change_effect(image, box):
    """
    Applies a color change effect to simulate an AR experience.

    Parameters:
    - image: The image on which to apply the effect.
    - box: A tuple (x, y, w, h) representing the bounding box coordinates.
    """
    # Unpack the bounding box coordinates
    x, y, w, h = box

    # Create a semi-transparent overlay on the bounding box area
    overlay = image.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 0), -1)  # Green overlay
    alpha = 0.3  # Transparency level
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)  # Apply overlay with transparency

# Main function to load an image, apply bounding boxes, and simulate AR effects
def main():
    # Set the path to your image file
    image_path = 'C:/Users/akhil/OneDrive/Desktop/FindMeCodingAssessment/shelf_pic.jpg'

    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return

    # Example bounding boxes and labels (I hardcoded these; in a real scenario, they would come from an object detection model)
    bounding_boxes = [(50, 50, 100, 150), (200, 200, 120, 160)]  # Example boxes [(x, y, w, h), ...]
    labels = ["Product 1", "Product 2"]  # Example labels

    # Apply overlay text and color change effect on each detected object
    for box, label in zip(bounding_boxes, labels):
        overlay_text(image, box, label)  # Overlay text on the bounding box
        color_change_effect(image, box)  # Apply AR color effect

    # Display the image with overlays
    cv2.imshow("Augmented Reality Simulation", image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the displayed window

    # Optionally, I am saving the output image with AR effects applied
    output_path = 'C:/Users/akhil/OneDrive/Desktop/FindMeCodingAssessment/part3output/augmented_image.jpg'
    cv2.imwrite(output_path, image)
    print("Image saved at", output_path)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
