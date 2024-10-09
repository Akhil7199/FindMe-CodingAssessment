#Part 1: Image Processing and Machine Learning with Python

#Task: Develop a Python script using OpenCV and a pre-trained machine learning model to perform object detection on images of shelves


#First, Import the OpenCV library for image processing
import cv2

# Import the PyTorch library, which is used here for loading and using pre-trained machine learning models like YOLO
import torch

# Specify the path to your image
image_path = 'C:/Users/akhil/OneDrive/Desktop/FindMeCodingAssessment/shelf_pic.jpg'

#Define a function that loads and preprocesses an image
def preprocess_image(image_path):
    # Read the image from the given file path
    image = cv2.imread(image_path)
    
    # Resize the image to 640x480 pixels to make processing consistent
    image = cv2.resize(image, (640, 480))
    
    # Normalize pixel values by dividing by 255 to scale between [0 and 1]
    image = image / 255.0
    
    # Return the processed image
    return image

# Preprocess the image using the function
preprocessed_image = preprocess_image(image_path)

# Load the YOLOv5 model from PyTorch Hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Perform object detection on the original (unprocessed) image
results = model(image_path)

# Save and display the result with bounding boxes
results.save()

