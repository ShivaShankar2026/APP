# REAL-TIME-PROJECT
# 🚦 Real-Time Traffic Density Detection using Computer Vision

A Python-based desktop application that estimates road traffic density using **Canny Edge Detection** and automatically allocates green signal timing based on detected traffic intensity.

## 📌 Project Overview

This project analyzes a traffic image using Computer Vision techniques. It detects edges using the Canny Edge Detection algorithm, counts the number of white (edge) pixels, compares them with a reference image, and allocates an appropriate traffic signal duration.

The application provides a simple GUI built with Tkinter for easy interaction.

---

## ✨ Features

- Upload traffic images
- Image preprocessing using Canny Edge Detection
- Automatic white pixel counting
- Traffic density estimation
- Dynamic green signal time allocation
- Easy-to-use Tkinter GUI

---

## 🛠 Technologies Used

- Python 3.x
- OpenCV
- NumPy
- SciPy
- Matplotlib
- Scikit-Image
- Tkinter

---

## 📂 Project Structure

```
Real-Time-Traffic-Detection/
│
├── Main.py                    # Main GUI application
├── CannyEdgeDetector.py       # Custom Canny Edge Detection implementation
├── test.py                    # Testing script
├── req.txt                    # Required Python packages
├── run.bat                    # Windows execution script
├── images/                    # Input traffic images
├── gray/                      # Processed edge images
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Real-Time-Traffic-Detection.git
cd Real-Time-Traffic-Detection
```

### Install dependencies

```bash
pip install -r req.txt
```

or install the required libraries manually:

```bash
pip install opencv-python numpy scipy matplotlib scikit-image pillow
```

---

## ▶️ Run the Project

```bash
python Main.py
```

Or double-click:

```
run.bat
```

---

## 📖 How It Works

1. Upload a traffic image.
2. Convert the image to grayscale.
3. Apply Gaussian smoothing.
4. Detect edges using the Canny Edge Detection algorithm.
5. Count the white pixels.
6. Compare the result with a reference image.
7. Estimate traffic density.
8. Allocate green signal timing.

---

## 🚥 Traffic Signal Allocation

| Traffic Density | Green Signal Time |
|-----------------|------------------:|
| Very High (≥90%) | 60 seconds |
| High (85–90%) | 50 seconds |
| Moderate (75–85%) | 40 seconds |
| Low (50–75%) | 30 seconds |
| Very Low (<50%) | 20 seconds |

---

## 🖥 GUI Workflow

1. Upload Traffic Image
2. Image Preprocessing Using Canny Edge Detection
3. White Pixel Count
4. Calculate Green Signal Time Allocation
5. Exit

---

## 📸 Sample Workflow

```
Traffic Image
      │
      ▼
Grayscale Conversion
      │
      ▼
Gaussian Blur
      │
      ▼
Canny Edge Detection
      │
      ▼
White Pixel Counting
      │
      ▼
Compare with Reference Image
      │
      ▼
Traffic Density Calculation
      │
      ▼
Green Signal Time Allocation
```

---

## 📈 Future Improvements

- Real-time video processing
- Live CCTV camera support
- Deep Learning based vehicle detection (YOLO)
- Vehicle counting and classification
- Multi-lane traffic analysis
- Emergency vehicle priority
- Smart city integration

---

## 👨‍💻 Author

**Kondrathi Shiva Shankar**

- B.Tech Computer Science & Engineering
- Python Developer
- Computer Vision Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile



## 📄 License

This project is developed for educational and research purposes.

MIT License