
---

# Full Stack Developer Coding Test (FindMe)

This project includes solutions for image processing, machine learning, backend API development, and augmented reality integration using Python. Follow the instructions below to set up and run each part of the project.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Code](#running-the-code)
   - [Part 1: Image Processing and Machine Learning](#part-1-image-processing-and-machine-learning)
   - [Part 2: Backend and API Development](#part-2-backend-and-api-development)
   - [Part 3: Data Handling and Augmented Reality Integration](#part-3-data-handling-and-augmented-reality-integration)
5. [Troubleshooting](#troubleshooting)

---

## Project Overview

This project consists of three parts:
- **Part 1**: Object detection on shelf images using OpenCV and YOLO.
- **Part 2**: A Flask-based REST API for CRUD operations on product data.
- **Part 3**: Simulation of augmented reality effects using OpenCV to overlay text and animations on images.

## Prerequisites

Ensure you have the following installed:
- **Python**: Version 3.8 or higher
- **pip**: Python package installer

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: If `requirements.txt` isn’t available, you can manually install the libraries:
   ```bash
   pip install opencv-python torch torchvision flask setuptools
   ```

## Running the Code

### Part 1: Image Processing and Machine Learning

1. **Set the Image Path**: Open `part1.py` and specify the path to the image you want to process.
   ```python
   image_path = 'path/to/your/image.jpg'  # Replace with your actual image path
   ```

2. **Run the Script**:
   ```bash
   python part1.py
   ```

3. **Output**: Processed images with bounding boxes will be saved in the default output directory.

### Part 2: Backend and API Development

1. **Start the Flask API**: 
   ```bash
   python part2.py
   ```

2. **Access the API**: You can test API endpoints (CRUD operations) using tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/).

   Example `curl` command to add a product:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "Product1", "price": 100}' http://127.0.0.1:5000/product
   ```

### Part 3: Data Handling and Augmented Reality Integration

1. **Set the Image Path**: Open `part3.py` and specify the path to the image you want to process with AR effects.

2. **Run the Script**:
   ```bash
   python part3.py
   ```

3. **Output**: Processed images with AR overlays and animations will be saved in the specified directory.

## Troubleshooting

- **ModuleNotFoundError: No module named 'pkg_resources'**:
  - Install `setuptools` by running:
    ```bash
    pip install setuptools
    ```

- **Issues with Image Paths**:
  - Ensure the image paths in `part1.py` and `part3.py` are correct and point to existing images.

---

### Author

Akhil Kumar Baitipuli
