# 🛒 Social Network Ads Purchase Prediction

A Machine Learning project that predicts whether a user is likely to purchase a product based on their **Age** and **Estimated Salary**.

The project consists of:

- A **Random Forest Classifier** trained using Scikit-Learn
- A **Flask REST API** for serving predictions
- A **Streamlit Web Application** for user interaction

---

## 🚀 Project Workflow

```text
User Input (Age, Salary)
            │
            ▼
     Streamlit App
            │
     HTTP POST Request
            │
            ▼
        Flask API
            │
            ▼
   Random Forest Model
            │
            ▼
       Prediction
            │
            ▼
    Streamlit Output
```

---

## 📂 Project Structure

```text
Social-Network-Ads-Prediction/
│
├── app.py                 # Flask API
├── model_training.py      # Model training script
├── streamlit_app.py       # Streamlit frontend
├── rf_model.pkl           # Saved trained model
├── Social_Network_Ads.csv # Dataset
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Model Training

The model is trained using:

- Pandas
- NumPy
- Scikit-Learn
- Random Forest Classifier

### Steps

1. Load dataset
2. Remove unnecessary columns
3. Split data into training and testing sets
4. Train Random Forest Classifier
5. Save model using Joblib

---

## ⚙️ Flask API

The Flask API loads the trained model and exposes a prediction endpoint.

### Endpoint

```http
POST /predict
```

### Request Body

```json
{
    "input": [35, 50000]
}
```

### Response

```json
{
    "prediction": 1
}
```

Where:

- `1` = User is likely to purchase
- `0` = User is unlikely to purchase

---

## 🎨 Streamlit Frontend

The Streamlit application allows users to:

- Enter Age
- Enter Estimated Salary
- Get real-time predictions

The frontend sends user input to the Flask API and displays the prediction result.

---

## 🛠️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Social-Network-Ads-Prediction.git
cd Social-Network-Ads-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Step 1: Start Flask Server

```bash
python app.py
```

Flask will run on:

```text
http://127.0.0.1:5000
```

### Step 2: Launch Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📊 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Flask
- Streamlit
- Requests

---

## 📚 What I Learned

- Training machine learning models using Scikit-Learn
- Saving and loading models with Joblib
- Building REST APIs using Flask
- Sending HTTP requests using Requests
- Connecting a machine learning model to a web application
- Creating interactive user interfaces with Streamlit

---

## 📌 Future Improvements

- Deploy the Flask API to the cloud
- Deploy the Streamlit application
- Add model evaluation metrics
- Improve UI design
- Add input validation and error handling

---

## 📄 License

This project is created for learning and educational purposes.