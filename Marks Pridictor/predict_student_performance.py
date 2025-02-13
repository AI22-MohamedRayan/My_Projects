import numpy as np
import pandas as pd
import joblib

def predict_performance(age, gender, socioeconomic_status, previous_grades, attendance, extracurricular, parental_involvement, learning_resources):
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib')

    features = pd.DataFrame([[
        age,
        gender,
        socioeconomic_status,
        previous_grades,
        attendance,
        extracurricular,
        parental_involvement,
        learning_resources
    ]], columns=['age', 'gender', 'socioeconomic_status', 'previous_grades', 'attendance', 'extracurricular', 'parental_involvement', 'learning_resources'])

    features = scaler.transform(features)

    prediction = model.predict(features)
    
    return prediction[0]

if __name__ == '__main__':
    age = int(input("Enter age: "))
    gender = int(input("Enter gender (0 for M, 1 for F): "))
    socioeconomic_status = int(input("Enter socioeconomic status (0 for low, 1 for medium, 2 for high): "))
    previous_grades = float(input("Enter previous grades: "))
    attendance = float(input("Enter attendance: "))
    extracurricular = int(input("Enter extracurricular (0 for no, 1 for yes): "))
    parental_involvement = int(input("Enter parental involvement (0 for low, 1 for medium, 2 for high): "))
    learning_resources = int(input("Enter learning resources (0 for low, 1 for medium, 2 for high): "))

    final_grade = predict_performance(age, gender, socioeconomic_status, previous_grades, attendance, extracurricular, parental_involvement, learning_resources)

    print(f'The predicted final grade is: {final_grade}')
