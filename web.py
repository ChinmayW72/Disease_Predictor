from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import time

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:5173"}})

# Load the trained model
model = joblib.load('disease_prediction_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    
    data = request.get_json()
    predictions = model.predict(data)
    
    end_time = time.time()
    time_taken = end_time - start_time
    
    response = {
        "predictions": predictions.tolist(),
        "time_taken": time_taken
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
