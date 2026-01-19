"""
House Price Prediction API
Flask-based REST API for serving house price predictions
"""

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import traceback
import os

app = Flask(__name__)

# Global model variable
model = None

def load_model_on_startup():
    """Load the trained model on startup"""
    global model
    try:
        # Find the model file
        model_files = [f for f in os.listdir('.') if f.startswith('best_model_pipeline_') and f.endswith('.pkl')]
        if not model_files:
            raise FileNotFoundError("No model file found. Run the notebook first to generate the model.")
        
        model_path = model_files[0]
        model = joblib.load(model_path)
        print(f"Model loaded successfully: {model_path}")
        return True
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    if model is None:
        return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict house price
    
    Expected JSON format:
    {
        "bedrooms": 3,
        "bathrooms": 2,
        "sqft_living": 2000,
        ...other features
    }
    """
    try:
        if model is None:
            return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500
        
        # Get JSON data
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'No JSON data provided'}), 400
        
        # Convert to DataFrame
        features_df = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(features_df)[0]
        
        return jsonify({
            'status': 'success',
            'predicted_price': float(prediction),
            'features_received': len(data)
        }), 200
        
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'status': 'error',
            'message': f'Prediction failed: {str(e)}'
        }), 400

@app.route('/model-info', methods=['GET'])
def model_info():
    """Get information about the loaded model"""
    try:
        if model is None:
            return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500
        
        return jsonify({
            'status': 'success',
            'model_type': str(type(model)),
            'pipeline_steps': str(model.named_steps) if hasattr(model, 'named_steps') else 'Unknown'
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    """API documentation"""
    return jsonify({
        'name': 'House Price Prediction API',
        'version': '1.0',
        'endpoints': {
            'GET /': 'This documentation',
            'GET /health': 'Health check',
            'GET /model-info': 'Model information',
            'POST /predict': 'Make a price prediction'
        },
        'usage': {
            'method': 'POST',
            'endpoint': '/predict',
            'example': {
                'bedrooms': 3,
                'bathrooms': 2,
                'sqft_living': 2000,
                'sqft_lot': 5000
            }
        }
    }), 200

if __name__ == '__main__':
    # Load model on startup
    if load_model_on_startup():
        app.run(
            debug=False,
            host='0.0.0.0',
            port=5000,
            threaded=True
        )
    else:
        print("Failed to start API - model could not be loaded")
