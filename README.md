# Heart Disease Prediction App

A machine learning web application that predicts whether a person has a high or low chance of heart disease based on medical health details.

This project is built using **Python**, **Machine Learning**, and **Streamlit**.  
The final deployed application uses a trained **K-Nearest Neighbors (KNN)** classification model.

## Live Demo

Try the deployed app here:

[Heart Disease Prediction App](https://heartstrokepredictor-app.streamlit.app/)

---

## Project Overview

Heart disease is one of the most common health problems worldwide. This project uses machine learning to predict the possibility of heart disease based on different medical features such as age, cholesterol level, chest pain type, resting blood pressure, maximum heart rate, exercise-induced angina, and ST slope.

The user enters the required health details through a simple Streamlit web interface. The trained model then predicts whether the person has a high or low chance of heart disease.

The output shown by the app is:

- High chance of heart disease
- Low chance of heart disease

---

## Dataset

The dataset used for this project is a heart disease dataset containing medical information of patients.

The target column is:

```text
HeartDisease
```

Target values:

```text
0 = Low chance of heart disease
1 = High chance of heart disease
```

The dataset contains both numerical and categorical features.

---

## Features Used

The following features are used for prediction:

| Feature | Description |
|---|---|
| Age | Age of the person |
| Sex | Gender of the person |
| ChestPainType | Type of chest pain |
| RestingBP | Resting blood pressure |
| Cholesterol | Cholesterol level |
| FastingBS | Fasting blood sugar greater than 120 mg/dL |
| RestingECG | Resting electrocardiogram result |
| MaxHR | Maximum heart rate achieved |
| ExerciseAngina | Exercise-induced angina |
| Oldpeak | ST depression value |
| ST_Slope | Slope of the ST segment |

---

## Data Preprocessing

The following preprocessing steps were performed:

- Loaded and explored the dataset
- Checked dataset information and missing values
- Performed basic data analysis
- Visualized target column distribution
- Compared different features with the target column
- Encoded categorical columns using one-hot encoding
- Scaled the data using `StandardScaler`
- Split the dataset into training and testing data
- Trained multiple machine learning models
- Selected the best-performing model
- Saved the final model using `joblib`

---

## Models Used

The following machine learning models were tested:

| Model |
|---|
| Logistic Regression |
| K-Nearest Neighbors |
| Decision Tree |
| Support Vector Machine |
| Naive Bayes |

The final selected model was:

```text
K-Nearest Neighbors Classifier
```

---

## Final Model Performance

The best-performing model was **K-Nearest Neighbors**.

```text
Accuracy: 88.04%
F1 Score: 89.10%
```

KNN was selected because it gave the best overall performance among the tested models.

---

## Tech Stack

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---


## Future Improvements

- Improve the user interface
- Add prediction probability score
- Add more graphs and visualizations
- Add feature importance analysis
- Compare more machine learning models
- Try Random Forest and XGBoost
- Improve model accuracy further
- Add explanation for each input field

---

## Disclaimer

This project is made for educational and learning purposes only.  
It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---
