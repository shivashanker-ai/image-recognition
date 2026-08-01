# ============================================================
# MODULE 10 - LESSON 2
# DATASET PREPARATION & PREPROCESSING
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import random
import shutil
from pathlib import Path

# ------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------

PET_IMAGES_PATH = Path.home() / "Downloads" / "kagglecatsanddogs_5340" / "PetImages"

CAT_FOLDER = PET_IMAGES_PATH / "Cat"
DOG_FOLDER = PET_IMAGES_PATH / "Dog"

DATASET_FOLDER = Path("dataset")

TRAIN_FOLDER = DATASET_FOLDER / "train"
VALIDATION_FOLDER = DATASET_FOLDER / "validation"
TEST_FOLDER = DATASET_FOLDER / "test"

# ------------------------------------------------------------
# DATASET CONFIGURATION
# ------------------------------------------------------------


TRAIN_RATIO = 0.70
VALIDATION_RATIO = 0.15
TEST_RATIO = 0.15

# ------------------------------------------------------------
# DISPLAY PROJECT INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("      DATASET PREPARATION & PREPROCESSING")
print("=" * 60)

print(f"\nPetImages Folder : {PET_IMAGES_PATH}")
print(f"Dataset Folder   : {DATASET_FOLDER}")

# ------------------------------------------------------------
# CHECK DATASET
# ------------------------------------------------------------

if not CAT_FOLDER.exists():
    print("\nCat folder not found!")
    exit()

if not DOG_FOLDER.exists():
    print("\nDog folder not found!")
    exit()

print("\nPetImages folder found successfully!")

# ------------------------------------------------------------
# READ IMAGES
# ------------------------------------------------------------

cat_images = [
    image
    for image in CAT_FOLDER.glob("*.jpg")
    if image.stat().st_size > 0
]

dog_images = [
    image
    for image in DOG_FOLDER.glob("*.jpg")
    if image.stat().st_size > 0
]

print(f"\nTotal Cat Images : {len(cat_images)}")
print(f"Total Dog Images : {len(dog_images)}")

# ------------------------------------------------------------
# RANDOMIZE IMAGES
# ------------------------------------------------------------

random.shuffle(cat_images)
random.shuffle(dog_images)

print("\nUsing ALL valid Cat Images")
print("Using ALL valid Dog Images")

# ------------------------------------------------------------
# REMOVE OLD DATASET
# ------------------------------------------------------------

if DATASET_FOLDER.exists():

    print("\nOld dataset found.")
    print("Cleaning dataset...")

    for item in DATASET_FOLDER.rglob("*"):

        if item.is_file():
            item.unlink()

    print("Dataset cleaned successfully!")
# ------------------------------------------------------------
# CREATE DATASET FOLDERS
# ------------------------------------------------------------

folders = [
    TRAIN_FOLDER / "cat",
    TRAIN_FOLDER / "dog",
    VALIDATION_FOLDER / "cat",
    VALIDATION_FOLDER / "dog",
    TEST_FOLDER / "cat",
    TEST_FOLDER / "dog",
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

print("\nDataset folders created successfully!")

# ------------------------------------------------------------
# SPLIT DATASET
# ------------------------------------------------------------
cat_train = int(len(cat_images) * TRAIN_RATIO)
cat_validation = int(len(cat_images) * VALIDATION_RATIO)

dog_train = int(len(dog_images) * TRAIN_RATIO)
dog_validation = int(len(dog_images) * VALIDATION_RATIO)

train_cat = cat_images[:cat_train]
validation_cat = cat_images[cat_train:cat_train + cat_validation]
test_cat = cat_images[cat_train + cat_validation:]

train_dog = dog_images[:dog_train]
validation_dog = dog_images[dog_train:dog_train + dog_validation]
test_dog = dog_images[dog_train + dog_validation:]
# ------------------------------------------------------------
# COPY IMAGES
# ------------------------------------------------------------

def copy_images(images, destination):

    for image in images:
        shutil.copy2(image, destination / image.name)

print("\nCopying Training Images...")

copy_images(train_cat, TRAIN_FOLDER / "cat")
copy_images(train_dog, TRAIN_FOLDER / "dog")

print("Training Images Completed!")

print("\nCopying Validation Images...")

copy_images(validation_cat, VALIDATION_FOLDER / "cat")
copy_images(validation_dog, VALIDATION_FOLDER / "dog")

print("Validation Images Completed!")

print("\nCopying Testing Images...")

copy_images(test_cat, TEST_FOLDER / "cat")
copy_images(test_dog, TEST_FOLDER / "dog")

print("Testing Images Completed!")

# ------------------------------------------------------------
# FINAL REPORT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(f"Training Images   : {len(train_cat) + len(train_dog)}")
print(f"Validation Images : {len(validation_cat) + len(validation_dog)}")
print(f"Testing Images    : {len(test_cat) + len(test_dog)}")

print(f"\nTotal Images Used : {len(cat_images) + len(dog_images)}")

print("\nDataset Prepared Successfully!")

print("\nLesson 2 Completed Successfully!")