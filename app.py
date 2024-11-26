import os
import pickle
from flask import Flask, request, jsonify

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Extract the features (assuming data contains a list of feature values)
        features = data['features']
        
        # Predict using the model
        prediction = model.predict([features])
        
        # Return the prediction result
        return jsonify({'prediction': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
