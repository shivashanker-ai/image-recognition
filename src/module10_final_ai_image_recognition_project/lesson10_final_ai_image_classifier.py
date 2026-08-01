"""
===============================================================
            AI CAT vs DOG IMAGE CLASSIFIER
===============================================================

Author      : Shiva Shankar
Project     : AI Image Recognition
Framework   : TensorFlow + OpenCV
Model       : Convolutional Neural Network (CNN)

Description
-----------
Professional AI application that predicts whether an image
contains a Cat or a Dog using a trained CNN model.

Features
--------
✓ Professional Console Interface
✓ Automatic File Validation
✓ File Explorer Image Selection
✓ TensorFlow CNN Prediction
✓ Confidence Percentage
✓ Inference Time
✓ Professional OpenCV Result Window
✓ Clean Resource Management
✓ Interview Quality Code

===============================================================
"""

# ===============================================================
# IMPORT LIBRARIES
# ===============================================================

import time
from pathlib import Path

import cv2
import numpy as np
import tensorflow as tf

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ===============================================================
# PROJECT CONFIGURATION
# ===============================================================

PROJECT_FOLDER = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_FOLDER / "models" / "cat_dog_cnn.keras"

IMAGE_SIZE = (150, 150)

WINDOW_NAME = "AI Cat vs Dog Image Classifier"

# ===============================================================
# APPLICATION BANNER
# ===============================================================

print("\n" + "=" * 70)
print("              AI CAT vs DOG IMAGE CLASSIFIER")
print("=" * 70)

print("\nApplication Information")
print("-" * 70)

print(f"Author           : Shiva Shankar")
print("Framework        : TensorFlow + OpenCV")
print("Architecture     : Convolutional Neural Network (CNN)")
print(f"Project Folder   : {PROJECT_FOLDER}")

print("\nProject Files")
print("-" * 70)

print(f"Model Path       : {MODEL_PATH}")

print("\nSystem Status")
print("-" * 70)

print("Preparing Application...")
print("Initializing Components...")
print("Loading Configuration...")

# ===============================================================
# SELECT IMAGE USING FILE EXPLORER
# ===============================================================

print("\nOpening File Explorer...")

root = Tk()

root.withdraw()

root.attributes("-topmost", True)

selected_image = askopenfilename(

    title="Select an Image for AI Prediction",

    filetypes=[

        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp"),

        ("JPEG Images", "*.jpg *.jpeg"),

        ("PNG Images", "*.png"),

        ("Bitmap Images", "*.bmp"),

        ("WEBP Images", "*.webp")

    ]

)

root.destroy()

if selected_image == "":

    print("\nNo image selected.")
    print("Application Closed Successfully.")

    raise SystemExit()

IMAGE_PATH = Path(selected_image)

print("✓ Image Selected Successfully!")
print(f"Selected Image : {IMAGE_PATH}")

# ===============================================================
# VALIDATE PROJECT FILES
# ===============================================================

print("\n" + "=" * 70)
print("VALIDATING PROJECT FILES")
print("=" * 70)

errors_found = False

if MODEL_PATH.exists():

    print("✓ CNN Model Found")

else:

    print("✗ CNN Model Not Found")
    print(f"Expected Location : {MODEL_PATH}")

    errors_found = True

if IMAGE_PATH.exists():

    print("✓ Input Image Found")

else:

    print("✗ Selected Image Not Found")
    print(f"Expected Location : {IMAGE_PATH}")

    errors_found = True

if errors_found:

    print("\nApplication Terminated.")

    raise SystemExit()

print("\nProject Validation Completed Successfully!")
# ===============================================================
# LOAD TRAINED CNN MODEL
# ===============================================================

print("\n" + "=" * 70)
print("LOADING TRAINED CNN MODEL")
print("=" * 70)

model_loading_start = time.time()

try:

    model = tf.keras.models.load_model(MODEL_PATH)

except Exception as error:

    print("\nFailed to load the trained CNN model.")
    print(f"\nReason : {error}")

    raise SystemExit()

model_loading_end = time.time()

model_loading_time = model_loading_end - model_loading_start

print("\n✓ CNN Model Loaded Successfully!")

print(f"Loading Time : {model_loading_time:.3f} seconds")

print("\nModel Information")
print("-" * 70)

print(f"Input Shape    : {model.input_shape}")
print(f"Output Shape   : {model.output_shape}")
print(f"Model Name     : {model.name}")

# ===============================================================
# LOAD INPUT IMAGE
# ===============================================================

print("\n" + "=" * 70)
print("LOADING INPUT IMAGE")
print("=" * 70)

original_image = cv2.imread(str(IMAGE_PATH))

if original_image is None:

    print("\nUnable to load the selected image.")

    raise SystemExit()

print("\n✓ Image Loaded Successfully!")

image_height, image_width = original_image.shape[:2]

print(f"Image Resolution : {image_width} x {image_height}")

# ===============================================================
# IMAGE PREPROCESSING
# ===============================================================

print("\n" + "=" * 70)
print("PREPROCESSING IMAGE")
print("=" * 70)

rgb_image = cv2.cvtColor(

    original_image,

    cv2.COLOR_BGR2RGB

)

resized_image = cv2.resize(

    rgb_image,

    IMAGE_SIZE,

    interpolation=cv2.INTER_AREA

)

model_input = np.expand_dims(
    resized_image.astype(np.float32),
    axis=0
)

print("\n✓ Image Preprocessing Completed Successfully!")

print(f"Model Input Size : {IMAGE_SIZE[0]} x {IMAGE_SIZE[1]}")
# ===============================================================
# RUN AI PREDICTION
# ===============================================================

print("\n" + "=" * 70)
print("RUNNING AI PREDICTION")
print("=" * 70)

prediction_start = time.time()

prediction = model.predict(

    model_input,

    verbose=0

)

prediction_end = time.time()

inference_time = prediction_end - prediction_start

prediction_probability = float(prediction[0][0])

print(f"\nRaw Model Output : {prediction_probability:.6f}")

# ===============================================================
# DETERMINE PREDICTION
# ===============================================================

CLASS_NAMES = [

    "CAT 🐱",

    "DOG 🐶"

]

if prediction_probability >= 0.5:

    predicted_index = 1

    confidence_percentage = prediction_probability * 100

else:

    predicted_index = 0

    confidence_percentage = (1.0 - prediction_probability) * 100

predicted_class = CLASS_NAMES[predicted_index]

# ===============================================================
# SELECT DISPLAY COLOR
# ===============================================================

if predicted_index == 0:

    display_color = (255, 170, 0)

else:

    display_color = (0, 255, 0)

print("\n✓ Prediction Completed Successfully!")

print("\nPrediction Results")
print("-" * 70)

print(f"Predicted Class : {predicted_class}")
print(f"Confidence      : {confidence_percentage:.2f}%")
print(f"Inference Time  : {inference_time:.4f} seconds")
# ===============================================================
# PREPARE RESULT WINDOW
# ===============================================================

print("\n" + "=" * 70)
print("PREPARING RESULT WINDOW")
print("=" * 70)

display_image = original_image.copy()

display_image = cv2.resize(

    display_image,

    (900, 650),

    interpolation=cv2.INTER_AREA

)

# ===============================================================
# DRAW HEADER
# ===============================================================

cv2.rectangle(

    display_image,

    (0, 0),

    (900, 150),

    (35, 35, 35),

    -1

)

cv2.putText(

    display_image,

    "AI CAT vs DOG IMAGE CLASSIFIER",

    (20, 45),

    cv2.FONT_HERSHEY_SIMPLEX,

    1.0,

    (255, 255, 255),

    2

)

# ===============================================================
# DRAW PREDICTION INFORMATION
# ===============================================================

cv2.putText(

    display_image,

    f"Prediction : {predicted_class}",

    (20, 85),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.8,

    display_color,

    2

)

cv2.putText(

    display_image,

    f"Confidence : {confidence_percentage:.2f}%",

    (20, 120),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.8,

    (255, 255, 255),

    2

)

# ===============================================================
# DRAW IMAGE INFORMATION
# ===============================================================

cv2.putText(

    display_image,

    f"Inference Time : {inference_time:.4f} sec",

    (520, 85),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.7,

    (0, 255, 255),

    2

)

cv2.putText(

    display_image,

    f"Resolution : {image_width} x {image_height}",

    (520, 120),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.7,

    (0, 255, 255),

    2

)

# ===============================================================
# FOOTER
# ===============================================================

cv2.rectangle(

    display_image,

    (0, 620),

    (900, 650),

    (35, 35, 35),

    -1

)

cv2.putText(

    display_image,

    "Press any key to close the application",

    (220, 642),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.6,

    (255, 255, 255),

    1

)

# ===============================================================
# DISPLAY RESULT
# ===============================================================

print("\nDisplaying AI Prediction...")

cv2.namedWindow(

    WINDOW_NAME,

    cv2.WINDOW_NORMAL

)

cv2.resizeWindow(

    WINDOW_NAME,

    900,

    650

)

cv2.imshow(

    WINDOW_NAME,

    display_image

)

cv2.waitKey(0)
# ===============================================================
# RELEASE RESOURCES
# ===============================================================

print("\nClosing Application...")

cv2.destroyAllWindows()

print("✓ OpenCV Windows Closed Successfully!")

# ===============================================================
# APPLICATION SUMMARY
# ===============================================================

print("\n" + "=" * 70)
print("APPLICATION SUMMARY")
print("=" * 70)

print("\nProject")
print("-" * 70)

print("AI Cat vs Dog Image Classifier")

print("\nPrediction Results")
print("-" * 70)

print(f"Predicted Class : {predicted_class}")
print(f"Confidence      : {confidence_percentage:.2f}%")
print(f"Raw Output      : {prediction_probability:.6f}")
print(f"Inference Time  : {inference_time:.4f} seconds")

print("\nImage Information")
print("-" * 70)

print(f"Image Name      : {IMAGE_PATH.name}")
print(f"Image Size      : {image_width} x {image_height}")

print("\nApplication Features")
print("-" * 70)

features = [

    "Professional Console Interface",
    "Automatic File Explorer",
    "CNN Model Prediction",
    "Professional OpenCV Window",
    "Confidence Score",
    "Inference Time Measurement",
    "Image Validation",
    "Model Validation",
    "Resource Cleanup"

]

for feature in features:

    print(f"✓ {feature}")

print("\nApplication Finished Successfully!")

print("=" * 70)