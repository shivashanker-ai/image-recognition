# ============================================================
# MODULE 10 - LESSON 9
# AI VIDEO CLASSIFICATION
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

from pathlib import Path

import time

import cv2
import numpy as np

from tensorflow.keras.models import load_model

# ------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------

PROJECT_FOLDER = Path.cwd()

MODEL_PATH = PROJECT_FOLDER / "models" / "cat_dog_cnn.keras"

VIDEO_PATH = PROJECT_FOLDER / "src" / "module10_final_ai_image_recognition_project" / "test_video.mp4"

IMAGE_SIZE = (150, 150)

WINDOW_NAME = "AI VIDEO CLASSIFIER"

# ------------------------------------------------------------
# DISPLAY PROJECT INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("            AI VIDEO CLASSIFIER")
print("=" * 60)

print(f"\nProject Folder : {PROJECT_FOLDER}")
print(f"Model File     : {MODEL_PATH}")
print(f"Video File     : {VIDEO_PATH}")

# ------------------------------------------------------------
# CHECK FILES
# ------------------------------------------------------------

if not MODEL_PATH.exists():

    print("\nModel not found!")
    exit()

if not VIDEO_PATH.exists():

    print("\nVideo not found!")
    exit()

print("\nModel Found Successfully!")
print("Video Found Successfully!")
# ------------------------------------------------------------
# LOAD TRAINED MODEL
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOADING TRAINED MODEL")
print("=" * 60)

model = load_model(MODEL_PATH)

print("\nModel Loaded Successfully!")

# ------------------------------------------------------------
# OPEN VIDEO
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("OPENING VIDEO")
print("=" * 60)

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

VIDEO_PATH = askopenfilename(
    title="Select a Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
)

video = cv2.VideoCapture(VIDEO_PATH)

if not video.isOpened():

    print("\nUnable to open video!")
    exit()

print("\nVideo Opened Successfully!")

# ------------------------------------------------------------
# INITIALIZE VARIABLES
# ------------------------------------------------------------

previous_time = time.time()

print("\nInitialization Completed!")
# ------------------------------------------------------------
# START VIDEO PREDICTION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STARTING VIDEO PREDICTION")
print("=" * 60)

while True:

    success, frame = video.read()

    if not success:

        print("\nEnd of Video Reached.")
        break

    # --------------------------------------------------------
    # KEEP ORIGINAL FRAME
    # --------------------------------------------------------

    display_frame = frame.copy()

    # --------------------------------------------------------
    # PREPROCESS FRAME
    # --------------------------------------------------------

    image = cv2.resize(

        frame,

        IMAGE_SIZE

    )

    image = image.astype("float32") / 255.0

    image = np.expand_dims(

        image,

        axis=0

    )

    # --------------------------------------------------------
    # AI PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(

        image,

        verbose=0

    )

    confidence = float(prediction[0][0])

    if confidence >= 0.5:

        predicted_class = "DOG"

        confidence_percentage = confidence * 100

    else:

        predicted_class = "CAT"

        confidence_percentage = (1 - confidence) * 100

    # --------------------------------------------------------
    # FPS CALCULATION
    # --------------------------------------------------------

    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    # --------------------------------------------------------
    # DRAW USER INTERFACE
    # --------------------------------------------------------

    cv2.putText(

        display_frame,

        f"Prediction : {predicted_class}",

        (20, 40),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.9,

        (0, 255, 0),

        2

    )

    cv2.putText(

        display_frame,

        f"Confidence : {confidence_percentage:.2f}%",

        (20, 80),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.9,

        (0, 255, 0),

        2

    )

    cv2.putText(

        display_frame,

        f"FPS : {fps:.2f}",

        (20, 120),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.9,

        (0, 255, 0),

        2

    )

    cv2.putText(

        display_frame,

        "Press Q to Exit",

        (20, 160),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (255, 255, 0),

        2

    )

    # --------------------------------------------------------
    # DISPLAY VIDEO
    # --------------------------------------------------------

    cv2.namedWindow(

        WINDOW_NAME,

        cv2.WINDOW_NORMAL

    )

    cv2.resizeWindow(

        WINDOW_NAME,

        1000,

        700

    )

    cv2.imshow(

        WINDOW_NAME,

        display_frame

    )

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):

        print("\nApplication Closed by User.")
        break

# ------------------------------------------------------------
# RELEASE RESOURCES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("RELEASING RESOURCES")
print("=" * 60)

video.release()

print("\nVideo Released Successfully!")

cv2.destroyAllWindows()

print("OpenCV Windows Closed Successfully!")

# ------------------------------------------------------------
# PROGRAM SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("VIDEO CLASSIFICATION SUMMARY")
print("=" * 60)

print("\nFeatures")
print("--------")
print("✓ CNN Model Prediction")
print("✓ Real-Time Video Processing")
print("✓ Confidence Percentage")
print("✓ FPS Counter")
print("✓ Professional OpenCV Interface")
print("✓ Clean Resource Management")

print("\nControls")
print("--------")
print("Press Q -> Exit Application")

print("\nLesson 9 Completed Successfully!")