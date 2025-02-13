import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    data = pd.read_csv('student_data.csv')

    data['gender'] = data['gender'].map({'M': 0, 'F': 1})
    data['extracurricular'] = data['extracurricular'].map({'no': 0, 'yes': 1})
    data['socioeconomic_status'] = data['socioeconomic_status'].map({'low': 0, 'medium': 1, 'high': 2})
    data['parental_involvement'] = data['parental_involvement'].map({'low': 0, 'medium': 1, 'high': 2})
    data['learning_resources'] = data['learning_resources'].map({'low': 0, 'medium': 1, 'high': 2})

    X = data.drop(columns=['student_id', 'final_grade'])
    y = data['final_grade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)

    joblib.dump(model, 'model.joblib')
    joblib.dump(scaler, 'scaler.joblib')

if __name__ == '__main__':
    train_model()
    print("Model and scaler saved successfully.")
