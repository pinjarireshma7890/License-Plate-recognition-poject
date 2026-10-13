# Car License Plate Recognition System

## Overview
A Python-based computer vision project that attempts to detect vehicle license plate regions from images and recognize the text using Optical Character Recognition (OCR).

This project uses OpenCV for image processing and EasyOCR for text recognition.

## Features
- Loads a vehicle image
- Converts the image to grayscale and reduces noise
- Detects edges and searches for possible license plate regions
- Enhances the selected region for OCR
- Prints recognized text from original and enhanced plate crops

## Technologies Used
- Python
- OpenCV
- EasyOCR
- NumPy

## Project Structure
```text
License-Plate-recognition-poject/
├── car.jpeg
├── lpr.py
├── project6.python
└── README.md
```

## Installation
Install the required Python libraries:

```bash
pip install opencv-python easyocr numpy
```

## How to Run
1. Keep `car.jpeg` in the same folder as `lpr.py`.
2. Open Command Prompt in the project folder.
3. Run:

```bash
python lpr.py


The program searches for a possible plate region and prints OCR results for the original and enhanced image crops.

## Limitations
- Uses contour-based heuristics for plate detection.
- Results depend on image quality, lighting, and viewing angle.
- Similar characters, such as `S` and `5`, may be confused.
- This is a beginner-level prototype and may not work reliably for every image.

## Future Improvements
- Improve plate detection and OCR accuracy
- Test with different vehicle images
- Display the detected plate region
- Evaluate accuracy using labeled images

## Author
Developed as a Python computer vision project.
