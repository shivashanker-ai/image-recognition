import tensorflow as tf

model = tf.keras.models.load_model("models/cat_dog_cnn.keras")

model.summary()