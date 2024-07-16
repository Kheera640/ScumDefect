import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Load data
x_sample_path = r'C:\ml\processed data\x_sample.csv'
y_sample_path = r'C:\ml\processed data\y_sample.csv'

x_sample = pd.read_csv(x_sample_path)
y_sample = pd.read_csv(y_sample_path)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_sample, y_sample, test_size=0.5)

# Build the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(5, input_dim=x_train.shape[1], activation="softmax"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1
                                                 ), 
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False), 
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=100, verbose=1)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')


predict_path = r'C:\ml\processed data\x_test.csv'
new_data = pd.read_csv(predict_path)

# Use the model to make predictions on the new data
predictions = model.predict(new_data)


print("predictions" ,predictions)

