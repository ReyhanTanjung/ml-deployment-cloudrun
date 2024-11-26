# model.py
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Membuat data dummy untuk pelatihan
X = np.array([[1], [2], [3], [4], [5]])  # Fitur
y = np.array([1, 2, 3, 4, 5])  # Target

# Melatih model regresi linear
model = LinearRegression()
model.fit(X, y)

# Menyimpan model ke file
joblib.dump(model, 'model.pkl')
