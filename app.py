from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Modeli ve ölçekleyiciyi yükleme
with open('rf_model_selected.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)
with open('scaler_selected.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Özellik isimleri
feature_names = [
    'worst area',
    'worst concave points',
    'mean concave points',
    'worst radius',
    'mean concavity'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Formdan verileri alma
            input_data = [float(request.form[feature]) for feature in feature_names]
            
            # Veriyi NumPy dizisine çevirme ve yeniden şekillendirme
            input_data_np = np.array(input_data).reshape(1, -1)
            
            # Veriyi ölçeklendirme
            input_data_scaled = scaler.transform(input_data_np)
            
            # Tahmin yapma
            prediction = rf_model.predict(input_data_scaled)[0]
            prediction_proba = rf_model.predict_proba(input_data_scaled)[0]
            
            # Sonucu hazırlama
            result = 'Malignant' if prediction == 0 else 'Benign'
            confidence = prediction_proba[prediction] * 100
            
            return render_template('index.html', result=result, confidence=confidence, feature_names=feature_names)
        except ValueError:
            return render_template('index.html', error="Lütfen tüm alanlara geçerli sayısal değerler girin.", feature_names=feature_names)
    
    return render_template('index.html', feature_names=feature_names)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        # JSON verisini alma
        data = request.get_json()
        input_data = [float(data[feature]) for feature in feature_names]
        
        # Veriyi NumPy dizisine çevirme ve yeniden şekillendirme
        input_data_np = np.array(input_data).reshape(1, -1)
        
        # Veriyi ölçeklendirme
        input_data_scaled = scaler.transform(input_data_np)
        
        # Tahmin yapma
        prediction = rf_model.predict(input_data_scaled)[0]
        prediction_proba = rf_model.predict_proba(input_data_scaled)[0]
        
        # Sonucu hazırlama
        result = 'Malignant' if prediction == 0 else 'Benign'
        confidence = prediction_proba[prediction] * 100
        
        return jsonify({
            'prediction': result,
            'confidence': round(confidence, 2),
            'features': {feature: value for feature, value in zip(feature_names, input_data)}
        })
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input. Please provide all features as numbers in JSON format.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)