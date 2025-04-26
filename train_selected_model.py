import pickle
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score

# Veri setini yükleme
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['diagnosis'] = data.target  # 0: malignant, 1: benign

# En önemli 5 özelliği seçme
selected_features = [
    'worst area',
    'worst concave points',
    'mean concave points',
    'worst radius',
    'mean concavity'
]
X = df[selected_features]
y = df['diagnosis']

# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Özellik ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Yeni Random Forest modelini eğitme
rf_model_selected = RandomForestClassifier(n_estimators=200, random_state=42)
rf_model_selected.fit(X_train_scaled, y_train)

# Modelin performansını değerlendirme
y_train_pred = rf_model_selected.predict(X_train_scaled)
y_test_pred = rf_model_selected.predict(X_test_scaled)

print("Eğitim Seti Performansı:")
print(f"Accuracy: {accuracy_score(y_train, y_train_pred):.4f}")
print(f"Precision: {precision_score(y_train, y_train_pred):.4f}")

print("\nTest Seti Performansı:")
print(f"Accuracy: {accuracy_score(y_test, y_test_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_test_pred):.4f}")

# Modeli ve ölçekleyiciyi kaydetme
with open('rf_model_selected.pkl', 'wb') as model_file:
    pickle.dump(rf_model_selected, model_file)
with open('scaler_selected.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Yeni model ve ölçekleyici kaydedildi.")