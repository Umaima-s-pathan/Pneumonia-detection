# -*- coding: utf-8 -*-
"""Copy of Pneumonia Detection app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u0zok_6IYkdDk77BFyK8hG1-0F6ArGyr
"""

from flask import Flask, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load the saved model
model = load_model('pneumonia_detection_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    img = image.load_img(file, target_size=(150, 150))  # Adjust size as per your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image

    prediction = model.predict(img_array)
    class_label = 'Pneumonia' if prediction[0][0] > 0.5 else 'Normal'

    return jsonify({'prediction': class_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

!gunicorn "Copy of Pneumonia Detection app:app" --bind 0.0.0.0

