# FindMe-CodingAssessment

Full Stack Developer Coding Test
This project includes solutions for image processing, machine learning, backend API development, and augmented reality integration using Python. Follow the instructions below to set up and run each part of the project.

Table of Contents
Project Overview
Prerequisites
Installation
Running the Code
Part 1: Image Processing and Machine Learning
Part 2: Backend and API Development
Part 3: Data Handling and Augmented Reality Integration
Troubleshooting
Project Overview
This project consists of three parts:

Part 1: Object detection on shelf images using OpenCV and YOLO.
Part 2: A Flask-based REST API for CRUD operations on product data.
Part 3: Simulation of augmented reality effects using OpenCV to overlay text and animations on images.
Prerequisites
Ensure you have the following installed:

Python: Version 3.8 or higher
pip: Python package installer
Installation
Clone this repository to your local machine.

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Install required Python libraries:

bash
Copy code
pip install -r requirements.txt
Note: If requirements.txt isn’t available, you can manually install the libraries:

bash
Copy code
pip install opencv-python torch torchvision flask setuptools
Running the Code
Part 1: Image Processing and Machine Learning
Set the Image Path: Open part1.py and specify the path to the image you want to process.

python
Copy code
image_path = 'path/to/your/image.jpg'  # Replace with your actual image path
Run the Script:

bash
Copy code
python part1.py
Output: Processed images with bounding boxes will be saved in the default output directory.

Part 2: Backend and API Development
Start the Flask API:

bash
Copy code
python part2.py
Access the API: You can test API endpoints (CRUD operations) using tools like Postman or curl.

Example curl command to add a product:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"name": "Product1", "price": 100}' http://127.0.0.1:5000/product
Part 3: Data Handling and Augmented Reality Integration
Set the Image Path: Open part3.py and specify the path to the image you want to process with AR effects.

Run the Script:

bash
Copy code
python part3.py
Output: Processed images with AR overlays and animations will be saved in the specified directory.

Troubleshooting
ModuleNotFoundError: No module named 'pkg_resources':

Install setuptools by running:
bash
Copy code
pip install setuptools
Issues with Image Paths:

Ensure the image paths in part1.py and part3.py are correct and point to existing images.
Author
This code was developed by Akhil Kumar Baitipuli, as part of a Full Stack Developer Coding Test.
