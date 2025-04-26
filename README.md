🎗️ Breast Cancer Prediction

Welcome to Breast Cancer Prediction—a powerful tool to predict whether a breast cancer tumor is benign or malignant using a Random Forest model. This Flask-based web application features a sleek Bootstrap 5 interface and a REST API for seamless predictions. 🚀
🌟 Live Demo: Try it now on Render!

✨ Overview
This project leverages machine learning to classify breast cancer tumors based on five key features from the Breast Cancer Wisconsin Dataset. Whether you're using the intuitive web interface or the API, you can get predictions with confidence scores in seconds!
🛠️ Tech Stack

Flask 🐍: Backend framework for web and API.
Bootstrap 5 🎨: Modern and responsive UI.
Scikit-learn 📊: Machine learning with Random Forest.
Render ☁️: Hosting platform for deployment.

📋 Features

🌐 Web Interface: Input tumor features and get instant predictions.
⚙️ REST API: Programmatically predict via /api/predict.
📈 Model: Trained on five features: worst area, worst concave points, mean concave points, worst radius, mean concavity.
🎯 Accuracy: High-confidence predictions with detailed results.


📂 Project Structure
breast-cancer-prediction/
├── app.py                    # Flask app with web and API routes
├── rf_model_selected.pkl     # Trained Random Forest model
├── scaler_selected.pkl       # StandardScaler for feature scaling
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html            # Bootstrap 5 interface
├── images/
│   └── cancer_samples.jpg    # Cancer tissue samples (Benign vs. Malignant)
└── README.md                 # Project documentation


🚀 Getting Started
Prerequisites

🐍 Python 3.8+
📥 Git
🌐 A web browser (for the web interface)
🛠️ Postman or cURL (for API testing)

Installation Steps

Clone the Repository 📦
git clone https://github.com/BlackRazor34/breast-cancer-prediction.git
cd breast-cancer-prediction


Set Up a Virtual Environment 🖥️
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies 📚
pip install -r requirements.txt


Run Locally ▶️
python app.py

Access the app at http://127.0.0.1:8080.



🌟 How to Use
🖥️ Web Interface

Visit the live app: https://breast-cancer-prediction-eimi.onrender.com 🌐
Enter the following tumor features:


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



Click Predict to see the result (Benign or Malignant) and confidence score. ✅
Use the Fill Example Values button to test with sample data.

⚙️ REST API
The /api/predict endpoint accepts POST requests with JSON data.

Endpoint: https://breast-cancer-prediction-eimi.onrender.com/api/predict
Method: POST
Header: Content-Type: application/json
Request Body:{
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

Test with Postman 🛠️

Open Postman and create a new HTTP request.
Set method to POST and URL to https://breast-cancer-prediction-eimi.onrender.com/api/predict.
Add header: Content-Type: application/json.
In the “Body” tab, select “raw” and “JSON”, then paste the example JSON.
Click “Send” to see the response.


☁️ Deployment on Render

Create a new Web Service on Render.
Connect your GitHub repository: https://github.com/BlackRazor34/breast-cancer-prediction.
Configure:
Environment: Python 🐍
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free


Deploy the service. Your app will be live at https://breast-cancer-prediction-eimi.onrender.com.


📸 Understanding Cancer Tissue Samples
The model is trained on histological images of breast cancer tissues. Below is a visual comparison of benign and malignant samples at different magnifications (4x, 10x, 20x):


Benign Samples: Typically show more organized structures and less cellular density.
Malignant Samples: Display irregular structures, higher cellular density, and more aggressive growth patterns.


📝 Notes

Free Tier Limitations: Render’s free plan may cause delays after inactivity. Be patient with the first request! ⏳
Model Files: Ensure rf_model_selected.pkl and scaler_selected.pkl are in the repository or manually uploaded to Render’s /app/ directory.
Future Improvements:
Add a /docs endpoint for API documentation.
Implement input validation for negative values.
Optimize the model for better performance on free-tier hosting.




📜 License
This project is licensed under the MIT License.
🙌 Acknowledgments

Built with ❤️ using Flask, Scikit-learn, and Bootstrap 5.
Hosted on Render.
Dataset: Breast Cancer Wisconsin Dataset.

