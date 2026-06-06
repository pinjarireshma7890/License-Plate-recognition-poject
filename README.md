# License Plate Recognition System

## Overview
The License Plate Recognition (LPR) System is a computer vision project that automatically detects and recognizes vehicle license plate numbers from images. It uses OpenCV for image processing and EasyOCR for character recognition.

## Features
- Detects text from vehicle images
- Extracts license plate numbers automatically
- Displays recognized plate numbers
- Simple and easy to implement

## Technologies Used
- Python
- OpenCV
- EasyOCR
- NumPy

## Requirements

Install the required libraries:

pip install opencv-python
pip install easyocr
pip install numpy

## Project Structure

License-Plate-Recognition/
│
├── car.jpg
├── lpr.py
└── README.md

## Code

```python
import cv2
import easyocr

# Initialize OCR Reader
reader = easyocr.Reader(['en'])

# Load vehicle image
image = cv2.imread('car.jpg')

# Detect and read text
results = reader.readtext(image)

# Print detected text
for result in results:
    print("Detected Plate Number:", result[1])

# Display image
cv2.imshow("Vehicle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
