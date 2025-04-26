Breast Cancer Prediction
This project is a web application that predicts whether a breast cancer tumor is benign or malignant based on five key features using a Random Forest machine learning model. The application is built with Flask, features a modern Bootstrap 5 interface, and provides a REST API for programmatic predictions. It is deployed on Render for public access.
Features

Web Interface: A user-friendly form to input five tumor features and receive predictions with confidence scores.
REST API: A /api/predict endpoint to make predictions programmatically via JSON requests.
Machine Learning Model: A Random Forest classifier trained on the Breast Cancer Wisconsin Dataset using five selected features: worst area, worst concave points, mean concave points, worst radius, and mean concavity.
Deployment: Hosted on Render at https://breast-cancer-prediction-eimi.onrender.com.

Project Structure
breast-cancer-prediction/
├── app.py                    # Flask application with web and API routes
├── rf_model_selected.pkl     # Trained Random Forest model
├── scaler_selected.pkl       # StandardScaler for feature scaling
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html            # Bootstrap 5 interface
└── README.md                 # Project documentation

Prerequisites

Python 3.11.9
Git
A web browser (for the web interface)
Postman or cURL (for API testing)

Installation

Clone the Repository:
git clone https://github.com/BlackRazor34/breast-cancer-prediction.git
cd breast-cancer-prediction


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the Application Locally:
python app.py


The app will be available at http://127.0.0.1:8080.



Usage
Web Interface

Open https://breast-cancer-prediction-eimi.onrender.com (or http://127.0.0.1:8080 for local).
Enter the five tumor features:
worst area: e.g., 711.2 (range: 200–2500)
worst concave points: e.g., 0.1288 (range: 0–0.3)
mean concave points: e.g., 0.04781 (range: 0–0.3)
worst radius: e.g., 15.11 (range: 6–28)
mean concavity: e.g., 0.06664 (range: 0–0.3)


Click Predict to see the result (Benign or Malignant) and confidence score.
Use the Fill Example Values button to populate the form with sample data.

REST API
The API endpoint /api/predict accepts POST requests with JSON data.

Endpoint: https://breast-cancer-prediction-eimi.onrender.com/api/predict

Method: POST

Header: Content-Type: application/json

Body:
{
  "worst area": 711.2,
  "worst concave points": 0.1288,
  "mean concave points": 0.04781,
  "worst radius": 15.11,
  "mean concavity": 0.06664
}


Example Request (cURL):
curl -X POST -H "Content-Type: application/json" -d '{"worst area": 711.2, "worst concave points": 0.1288, "mean concave points": 0.04781, "worst radius": 15.11, "mean concavity": 0.06664}' https://breast-cancer-prediction-eimi.onrender.com/api/predict


Example Response:
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


Testing with Postman:

Open Postman and create a new HTTP request.
Set method to POST and URL to https://breast-cancer-prediction-eimi.onrender.com/api/predict.
Add header: Content-Type: application/json.
In the “Body” tab, select “raw” and “JSON”, then paste the example JSON above.
Click “Send” to receive the response.



Deployment on Render

Create a new Web Service on Render.
Connect your GitHub repository: https://github.com/BlackRazor34/breast-cancer-prediction.
Configure:
Environment: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free


Deploy the service. The app will be live at a URL like https://breast-cancer-prediction-eimi.onrender.com.

Notes

Free Tier Limitations: Render’s free plan may put the app to sleep after inactivity, causing a delay on the first request.
Model Files: Ensure rf_model_selected.pkl and scaler_selected.pkl are included in the repository or manually uploaded to Render’s /app/ directory if using Git LFS or .gitignore.
Future Improvements:
Add a /docs endpoint for API documentation.
Implement input validation to prevent negative or invalid values.
Optimize the model for lower resource usage.



License
This project is licensed under the MIT License.
Acknowledgments

Built with Flask, Scikit-learn, and Bootstrap 5.
Deployed using Render.
Dataset: Breast Cancer Wisconsin Dataset.

