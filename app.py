# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Memuat model yang sudah disimpan
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Menerima data dalam format JSON
        data = request.get_json()
        features = np.array(data['features']).reshape(-1, 1)
        
        # Melakukan prediksi dengan model
        prediction = model.predict(features)
        
        # Mengembalikan hasil prediksi dalam format JSON
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
