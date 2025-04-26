🎗️ Breast Cancer Prediction
Welcome to Breast Cancer Prediction—a tool to classify breast cancer tumors as benign or malignant using a Random Forest model. Built with Flask, featuring a Bootstrap 5 interface and a REST API, this app is deployed on Render for public access.
🌟 Live Demo: Try it now!
📋 Overview
This project uses machine learning to predict breast cancer tumor types based on five features from the Breast Cancer Wisconsin Dataset. It offers a user-friendly web interface and an API for programmatic predictions.
🛠️ Tech Stack

Flask: Backend framework
Bootstrap 5: Responsive UI
Scikit-learn: Machine learning
Render: Hosting platform

✨ Features

🌐 Web interface for easy predictions
⚙️ REST API for programmatic access
📈 Model trained on 5 features: worst area, worst concave points, mean concave points, worst radius, mean concavity

📂 Project Structure
breast-cancer-prediction/
├── app.py                    # Flask app
├── rf_model_selected.pkl     # Trained model
├── scaler_selected.pkl       # Feature scaler
├── requirements.txt          # Dependencies
├── templates/
│   └── index.html            # Web interface
├── images/
│   └── cancer_samples.jpg    # Cancer tissue samples
└── README.md                 # Documentation

🚀 Getting Started
Prerequisites

Python 3.8+
Git
A web browser
Postman or cURL (for API testing)

Installation

Clone the repository:git clone https://github.com/BlackRazor34/breast-cancer-prediction.git
cd breast-cancer-prediction


Set up a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Run locally:python app.py

Access at http://127.0.0.1:8080.

🌟 Usage
🖥️ Web Interface

Visit https://breast-cancer-prediction-eimi.onrender.com.
Enter the tumor features:


Feature
Example Value
Typical Range



worst area
711.2
200–2500


worst concave points
0.1288
0–0.3


mean concave points
0.04781
0–0.3


worst radius
15.11
6–28


mean concavity
0.06664
0–0.3



Click Predict to see the result and confidence score.
Use Fill Example Values to test with sample data.

⚙️ REST API

Endpoint: https://breast-cancer-prediction-eimi.onrender.com/api/predict
Method: POST
Header: Content-Type: application/json
Body:{
  "worst area": 711.2,
  "worst concave points": 0.1288,
  "mean concave points": 0.04781,
  "worst radius": 15.11,
  "mean concavity": 0.06664
}



Example Request (cURL)
curl -X POST -H "Content-Type: application/json" -d '{"worst area": 711.2, "worst concave points": 0.1288, "mean concave points": 0.04781, "worst radius": 15.11, "mean concavity": 0.06664}' https://breast-cancer-prediction-eimi.onrender.com/api/predict

Example Response
{
  "prediction": "Benign",
  "confidence": 99.50,
  "features": {
    "worst area": 711.2,
    "worst concave points": 0.1288,
    "mean concave points": 0.04781,
    "worst radius": 15.11,
    "mean concavity": 0.06664
  }
}

📸 Cancer Tissue Samples
Below is a comparison of benign and malignant breast cancer tissue samples at different magnifications (4x, 10x, 20x):


Benign: More organized, less dense.
Malignant: Irregular, highly dense.

☁️ Deployment on Render

Create a Web Service on Render.
Connect your GitHub repo: https://github.com/BlackRazor34/breast-cancer-prediction.
Configure:
Environment: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free


Deploy and access at https://breast-cancer-prediction-eimi.onrender.com.

📝 Notes

Render’s free plan may cause delays after inactivity.
Ensure rf_model_selected.pkl and scaler_selected.pkl are uploaded.
Future improvements: Add API documentation, input validation.

📜 License
MIT License. See LICENSE for details.
🙌 Acknowledgments

Flask
Scikit-learn
Bootstrap 5
Render
Breast Cancer Wisconsin Dataset

