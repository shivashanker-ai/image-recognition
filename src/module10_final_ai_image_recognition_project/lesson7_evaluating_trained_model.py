# ============================================================
# MODULE 10 - LESSON 7
# EVALUATE TRAINED MODEL
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

from pathlib import Path

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image_dataset_from_directory

# ------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------

DATASET_FOLDER = Path("dataset")

TEST_FOLDER = DATASET_FOLDER / "test"

MODEL_PATH = Path("models") / "cat_dog_cnn.keras"

IMAGE_SIZE = (150, 150)

BATCH_SIZE = 32

# ------------------------------------------------------------
# DISPLAY INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("          EVALUATE TRAINED MODEL")
print("=" * 60)

print(f"\nModel : {MODEL_PATH}")
print(f"Test Dataset : {TEST_FOLDER}")

# ------------------------------------------------------------
# CHECK FILES
# ------------------------------------------------------------

if not MODEL_PATH.exists():

    print("\nModel not found!")
    exit()

if not TEST_FOLDER.exists():

    print("\nTest dataset not found!")
    exit()

print("\nModel Found Successfully!")
print("Test Dataset Found Successfully!")
# ------------------------------------------------------------
# LOAD TRAINED MODEL
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOADING TRAINED MODEL")
print("=" * 60)

model = load_model(MODEL_PATH)

print("\nModel Loaded Successfully!")

# ------------------------------------------------------------
# LOAD TEST DATASET
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOADING TEST DATASET")
print("=" * 60)

test_dataset = image_dataset_from_directory(

    TEST_FOLDER,

    image_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    shuffle=False

)

print("\nTest Dataset Loaded Successfully!")
# ------------------------------------------------------------
# EVALUATE MODEL
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("EVALUATING MODEL")
print("=" * 60)

test_loss, test_accuracy = model.evaluate(

    test_dataset,

    verbose=1

)

print("\nEvaluation Completed Successfully!")

# ------------------------------------------------------------
# EVALUATION SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"\nTest Accuracy : {test_accuracy:.4f}")
print(f"Test Loss     : {test_loss:.4f}")

print("\nLesson 7 Completed Successfully!")