import os
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def create_dummy_model():
    # Input shape based on app.py: (224, 224, 3)
    input_shape = (224, 224, 3)
    # Number of classes based on app.py: 9
    num_classes = 9
    
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(4, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    
    # Save model
    model.save('model.h5')
    print("Dummy model created and saved as model.h5")

if __name__ == "__main__":
    create_dummy_model()
