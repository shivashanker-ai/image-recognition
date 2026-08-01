# ============================================================
# MODULE 10 - LESSON 6
# TRAINING THE CNN
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

from pathlib import Path

import tensorflow as tf

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (

    Input,
    Rescaling,

    Conv2D,
    MaxPooling2D,

    BatchNormalization,

    Flatten,

    Dense,

    Dropout

)

from tensorflow.keras.callbacks import (

    EarlyStopping,
    ModelCheckpoint

)

from tensorflow.keras.utils import image_dataset_from_directory

# ------------------------------------------------------------
# DATASET SETTINGS
# ------------------------------------------------------------

DATASET_FOLDER = Path("dataset")

TRAIN_FOLDER = DATASET_FOLDER / "train"

VALIDATION_FOLDER = DATASET_FOLDER / "validation"

IMAGE_SIZE = (150, 150)

BATCH_SIZE = 32

EPOCHS = 15

# ------------------------------------------------------------
# MODEL SETTINGS
# ------------------------------------------------------------

MODEL_FOLDER = Path("models")

MODEL_FOLDER.mkdir(exist_ok=True)

MODEL_PATH = MODEL_FOLDER / "cat_dog_cnn.keras"

# ------------------------------------------------------------
# DISPLAY PROJECT INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("                TRAINING THE CNN")
print("=" * 60)

print(f"\nDataset Folder : {DATASET_FOLDER}")
print(f"Training Folder : {TRAIN_FOLDER}")
print(f"Validation Folder : {VALIDATION_FOLDER}")
print(f"Image Size : {IMAGE_SIZE}")
print(f"Batch Size : {BATCH_SIZE}")
print(f"Epochs : {EPOCHS}")
# ------------------------------------------------------------
# LOAD DATASETS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOADING DATASETS")
print("=" * 60)

# ------------------------------------------------------------
# CHECK DATASET
# ------------------------------------------------------------

if not TRAIN_FOLDER.exists():

    raise FileNotFoundError(

        f"Training folder not found:\n{TRAIN_FOLDER}"

    )

if not VALIDATION_FOLDER.exists():

    raise FileNotFoundError(

        f"Validation folder not found:\n{VALIDATION_FOLDER}"

    )

print("\nDataset Found Successfully!")

# ------------------------------------------------------------
# LOAD TRAINING DATASET
# ------------------------------------------------------------

train_dataset = image_dataset_from_directory(

    TRAIN_FOLDER,

    image_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    shuffle=True

)
print("\nClass Names:", train_dataset.class_names)
print("Class Index Mapping:", dict(enumerate(train_dataset.class_names)))

# ------------------------------------------------------------
# LOAD VALIDATION DATASET
# ------------------------------------------------------------

validation_dataset = image_dataset_from_directory(

    VALIDATION_FOLDER,

    image_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    shuffle=False

)

print("\nDatasets Loaded Successfully!")

# ------------------------------------------------------------
# DATASET OPTIMIZATION
# ------------------------------------------------------------

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(AUTOTUNE)

validation_dataset = validation_dataset.prefetch(AUTOTUNE)

print("Dataset Optimization Completed!")

print("\nTraining Dataset Ready!")
print("Validation Dataset Ready!")
# ------------------------------------------------------------
# BUILD CNN MODEL
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BUILDING CNN MODEL")
print("=" * 60)

model = Sequential([

    # Input Layer
    Input(shape=(150, 150, 3)),

    # Normalize Pixel Values (0-255 -> 0-1)
    Rescaling(1.0 / 255),

    # ---------------- First Block ----------------

    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        padding="same",
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(pool_size=(2, 2)),

    # ---------------- Second Block ----------------

    Conv2D(
        filters=64,
        kernel_size=(3, 3),
        padding="same",
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(pool_size=(2, 2)),

    # ---------------- Third Block ----------------

    Conv2D(
        filters=128,
        kernel_size=(3, 3),
        padding="same",
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(pool_size=(2, 2)),

    # ---------------- Fourth Block ----------------

    Conv2D(
        filters=256,
        kernel_size=(3, 3),
        padding="same",
        activation="relu"
    ),

    BatchNormalization(),

    MaxPooling2D(pool_size=(2, 2)),

    # ------------------------------------------------

    Flatten(),

    Dense(
        units=512,
        activation="relu"
    ),

    Dropout(0.50),

    Dense(
        units=256,
        activation="relu"
    ),

    Dropout(0.30),

    Dense(
        units=1,
        activation="sigmoid"
    )

])

print("\nCNN Model Created Successfully!")

# ------------------------------------------------------------
# COMPILE MODEL
# ------------------------------------------------------------

model.compile(

    optimizer="adam",

    loss="binary_crossentropy",

    metrics=["accuracy"]

)

print("Model Compiled Successfully!")
# ------------------------------------------------------------
# TRAINING CALLBACKS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PREPARING TRAINING")
print("=" * 60)

early_stopping = EarlyStopping(

    monitor="val_loss",

    patience=3,

    restore_best_weights=True,

    verbose=1

)

model_checkpoint = ModelCheckpoint(

    filepath=MODEL_PATH,

    monitor="val_accuracy",

    save_best_only=True,

    verbose=1

)

# ------------------------------------------------------------
# START TRAINING
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STARTING CNN TRAINING")
print("=" * 60)

history = model.fit(

    train_dataset,

    validation_data=validation_dataset,

    epochs=EPOCHS,

    callbacks=[

        early_stopping,

        model_checkpoint

    ]

)

print("\nTraining Completed Successfully!")

# ------------------------------------------------------------
# TRAINING SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TRAINING SUMMARY")
print("=" * 60)

best_train_accuracy = max(history.history["accuracy"])
best_validation_accuracy = max(history.history["val_accuracy"])

print(f"Epochs Completed          : {len(history.history['accuracy'])}")
print(f"Best Training Accuracy    : {best_train_accuracy:.4f}")
print(f"Best Validation Accuracy  : {best_validation_accuracy:.4f}")

print(f"\nBest Model Saved At : {MODEL_PATH}")

print("\nLesson 6 Completed Successfully!")