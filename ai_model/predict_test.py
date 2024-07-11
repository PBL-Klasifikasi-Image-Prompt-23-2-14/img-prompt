import numpy as np
from PIL import Image
import joblib

# Load model
model = joblib.load('knn_model.pkl')

# Daftar kelas atau label yang mungkin
class_names = ['Alam', 'Kota', 'Binatang', 'Lainnya']

def preprocess_image(image_path, target_size=(128, 128)):
    img = Image.open(image_path)
    img = img.resize(target_size)  # Resize gambar ke ukuran target
    img = np.array(img)
    img = img.reshape(-1)  # Flatten gambar menjadi satu dimensi
    img = img / 255.0  # Normalisasi nilai piksel
    return img

if __name__ == "__main__":
    # Uji prediksi
    image_path = 'test/test_image.jpg'
    img_data = preprocess_image(image_path, target_size=(128, 128))  # Sesuaikan ukuran target di sini
    img_data = np.expand_dims(img_data, axis=0)
    predictions = model.predict(img_data)
    
    # Ambil kelas prediksi (indeks kelas dengan nilai tertinggi)
    predicted_class_index = np.argmax(predictions)
    predicted_class = class_names[predicted_class_index]
    prediction_prob = predictions[0][predicted_class_index]
    
    print(f"Prediction: {predicted_class} ({prediction_prob:.2f})")
