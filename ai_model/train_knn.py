import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Contoh data pelatihan (gunakan data pelatihan sebenarnya)
X_train = np.random.rand(100, 64*64)  # Ganti dengan data pelatihan sebenarnya
y_train = np.random.randint(0, 2, 100)  # Ganti dengan label pelatihan sebenarnya

# Latih model KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Simpan model
joblib.dump(model, 'knn_model.pkl')
