# ============================================================
# MODULE 10 - LESSON 3
# LOADING DATASET
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import tensorflow as tf
from pathlib import Path

# ------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------

DATASET_FOLDER = Path("dataset")

TRAIN_FOLDER = DATASET_FOLDER / "train"
VALIDATION_FOLDER = DATASET_FOLDER / "validation"
TEST_FOLDER = DATASET_FOLDER / "test"

# ------------------------------------------------------------
# DATASET CONFIGURATION
# ------------------------------------------------------------

IMAGE_SIZE = (150, 150)

BATCH_SIZE = 32

# ------------------------------------------------------------
# DISPLAY PROJECT INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("              LOADING DATASET")
print("=" * 60)

print(f"\nDataset Folder : {DATASET_FOLDER}")

# ------------------------------------------------------------
# CHECK DATASET
# ------------------------------------------------------------

if not DATASET_FOLDER.exists():
    print("\nDataset folder not found!")
    exit()

if not TRAIN_FOLDER.exists():
    print("\nTraining folder not found!")
    exit()

if not VALIDATION_FOLDER.exists():
    print("\nValidation folder not found!")
    exit()

if not TEST_FOLDER.exists():
    print("\nTesting folder not found!")
    exit()

print("\nDataset found successfully!")

# ------------------------------------------------------------
# LOAD TRAINING DATASET
# ------------------------------------------------------------

print("\nLoading Training Dataset...")

train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_FOLDER,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)

print("Training Dataset Loaded!")

# ------------------------------------------------------------
# LOAD VALIDATION DATASET
# ------------------------------------------------------------

print("\nLoading Validation Dataset...")

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    VALIDATION_FOLDER,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)

print("Validation Dataset Loaded!")

# ------------------------------------------------------------
# LOAD TEST DATASET
# ------------------------------------------------------------

print("\nLoading Testing Dataset...")

test_dataset = tf.keras.utils.image_dataset_from_directory(
    TEST_FOLDER,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("Testing Dataset Loaded!")

# ------------------------------------------------------------
# DISPLAY DATASET INFORMATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(f"\nImage Size : {IMAGE_SIZE}")
print(f"Batch Size : {BATCH_SIZE}")

print("\nClasses :")

for index, class_name in enumerate(train_dataset.class_names):
    print(f"{index} --> {class_name}")

print("\nTraining Batches   :", len(train_dataset))
print("Validation Batches :", len(validation_dataset))
print("Testing Batches    :", len(test_dataset))

# ------------------------------------------------------------
# FINAL REPORT
# ------------------------------------------------------------

print("\nDataset Loaded Successfully!")

print("\nLesson 3 Completed Successfully!")