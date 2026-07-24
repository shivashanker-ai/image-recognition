import tensorflow as tf

model=tf.keras.sequential([
    tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),
    tf.keras.layers.Dense(8, activation="relu",)
    tf.keras.layers.Dense(3, activation="softmax")
])

model.summary()
print()