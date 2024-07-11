from flask import Flask, request, jsonify
import joblib
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the trained KNN model
model = joblib.load('knn_model.pkl')

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('L')
    image = image.resize((8, 8))
    image = np.array(image)
    image = image / 16.0
    return image.flatten().reshape(1, -1)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image_file = request.files['image']
    image_bytes = image_file.read()
    processed_image = preprocess_image(image_bytes)
    
    prediction = model.predict(processed_image)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
