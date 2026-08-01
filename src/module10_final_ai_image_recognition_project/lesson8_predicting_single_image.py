# ============================================================
# MODULE 10 - LESSON 8
# PREDICT SINGLE IMAGE
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

from pathlib import Path

import cv2
import numpy as np

from tensorflow.keras.models import load_model

# ------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------

PROJECT_FOLDER = Path.cwd()

MODEL_PATH = PROJECT_FOLDER / "models" / "cat_dog_cnn.keras"

TEST_IMAGES_FOLDER = PROJECT_FOLDER / "dataset" / "test" / "cat"

image_files = sorted(TEST_IMAGES_FOLDER.glob("*.jpg"))

if len(image_files) == 0:

    print("\nNo images found!")
    exit()

IMAGE_PATH = image_files[0]

IMAGE_SIZE = (150, 150)

WINDOW_NAME = "AI IMAGE PREDICTION"

# ------------------------------------------------------------
# DISPLAY INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("          AI IMAGE PREDICTION")
print("=" * 60)

print(f"\nModel File : {MODEL_PATH}")
print(f"Image File : {IMAGE_PATH}")

# ------------------------------------------------------------
# CHECK FILES
# ------------------------------------------------------------

if not MODEL_PATH.exists():

    print("\nModel not found!")
    exit()

if not IMAGE_PATH.exists():

    print("\nImage not found!")
    exit()

print("\nModel Found Successfully!")
print("Image Found Successfully!")
# ------------------------------------------------------------
# LOAD TRAINED MODEL
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOADING TRAINED MODEL")
print("=" * 60)

model = load_model(MODEL_PATH)

print("\nModel Loaded Successfully!")

# ------------------------------------------------------------
# LOAD IMAGE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOADING IMAGE")
print("=" * 60)

image = cv2.imread(str(IMAGE_PATH))

if image is None:

    print("\nUnable to load image!")
    exit()

print("\nImage Loaded Successfully!")

# ------------------------------------------------------------
# PREPROCESS IMAGE
# ------------------------------------------------------------

display_image = image.copy()

image = cv2.resize(

    image,

    IMAGE_SIZE

)

image = image.astype("float32") / 255.0

image = np.expand_dims(

    image,

    axis=0

)

print("Image Preprocessing Completed!")
# ------------------------------------------------------------
# MAKE PREDICTION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PREDICTING IMAGE")
print("=" * 60)

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

print(f"\nPrediction : {predicted_class}")
print(f"Confidence : {confidence_percentage:.2f}%")
# ------------------------------------------------------------
# DISPLAY RESULT
# ------------------------------------------------------------

label = f"{predicted_class} ({confidence_percentage:.2f}%)"

cv2.putText(

    display_image,

    label,

    (20, 40),

    cv2.FONT_HERSHEY_SIMPLEX,

    1,

    (0, 255, 0),

    2

)

cv2.namedWindow(

    WINDOW_NAME,

    cv2.WINDOW_NORMAL

)

cv2.resizeWindow(

    WINDOW_NAME,

    900,

    700

)

cv2.imshow(

    WINDOW_NAME,

    display_image

)

print("\nDisplaying Prediction...")

print("\nPress any key to close.")

cv2.waitKey(0)

cv2.destroyAllWindows()

# ------------------------------------------------------------
# LESSON SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LESSON SUMMARY")
print("=" * 60)

print(f"Predicted Class : {predicted_class}")
print(f"Confidence      : {confidence_percentage:.2f}%")

print("\nLesson 8 Completed Successfully!")