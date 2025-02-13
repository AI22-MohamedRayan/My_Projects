import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

train_df = pd.read_excel('train.xlsx')
test_df = pd.read_excel('train.xlsx')

print(train_df.head())

X = train_df.drop(columns='target')
y = train_df['target']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(test_df.drop(columns='target'))

rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train_scaled, y_train)

y_val_pred_rf = rf_model.predict(X_val_scaled)

accuracy_rf = accuracy_score(y_val, y_val_pred_rf)
print(f'Random Forest Validation Accuracy: {accuracy_rf}')

svc_model = SVC(random_state=42)
svc_model.fit(X_train_scaled, y_train)

y_val_pred_svc = svc_model.predict(X_val_scaled)

accuracy_svc = accuracy_score(y_val, y_val_pred_svc)
print(f'Support Vector Classifier Validation Accuracy: {accuracy_svc}')

y_test_pred_rf = rf_model.predict(X_test_scaled)
y_test_pred_rf = label_encoder.inverse_transform(y_test_pred_rf)

y_test_pred_svc = svc_model.predict(X_test_scaled)
y_test_pred_svc = label_encoder.inverse_transform(y_test_pred_svc)

test_predictions = pd.DataFrame({
    'Random Forest Predictions': y_test_pred_rf,
    'Support Vector Classifier Predictions': y_test_pred_svc
})

print(test_predictions.head())


