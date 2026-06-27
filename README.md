# 💼 AI-Powered Job Salary Prediction System

---

🌐 Live Demo

Experience the application online without any local setup:

🚀 Live Application:
https://jobsmarketprediction24-to-26.streamlit.app/

---

# 📌 Project Overview

The **AI-Powered Job Salary Prediction System** is a Machine Learning web application that predicts the expected salary (LPA) of job opportunities using real-world job market features.

The system has been developed using multiple regression algorithms and deployed with **Streamlit**, allowing users to compare different Machine Learning models and predict salaries through an interactive interface.

The project also provides a complete **Job Market Analytics Dashboard** that helps users understand hiring trends, salary distribution, work modes, industries, and city-wise opportunities.

---

# 🎯 Objectives

* Predict salary using Machine Learning
* Compare multiple regression algorithms
* Analyze Indian Job Market trends
* Build an interactive web application
* Visualize recruitment insights
* Deploy a real-world ML project

---

# ✨ Key Features

✔ Salary Prediction

✔ Multiple ML Model Selection

✔ Interactive Streamlit Dashboard

✔ Job Market Analytics

✔ Company-wise Analysis

✔ Industry-wise Salary Analysis

✔ Work Mode Analysis

✔ City-wise Hiring Analysis

✔ Easy-to-use Interface

✔ Model Comparison

---

# 📊 Dataset

The dataset represents Indian Job Market information from **2024–2026**.

### Features

| Feature            | Description                      |
| ------------------ | -------------------------------- |
| Job_Title          | Job Position                     |
| Company            | Company Name                     |
| Company_Type       | Startup, MNC, PSU/Govt, Unicorn  |
| Industry           | Industry Sector                  |
| City               | Job Location                     |
| Location_Tier      | Tier 1 / Tier 2 / Tier 3         |
| Experience_Level   | Fresher / Junior / Mid / Senior  |
| Job_Type           | Full-Time / Part-Time / Contract |
| Work_Mode          | Remote / Hybrid / Onsite         |
| Skills_Required    | Required Technical Skills        |
| Education_Required | Required Qualification           |
| Openings           | Number of Vacancies              |
| Applicants         | Total Applicants                 |
| Company_Rating     | Company Rating                   |
| Date_Posted        | Job Posting Date                 |
| Salary_LPA         | Target Variable                  |

---

# ⚙ Machine Learning Workflow

```text
Data Collection
       │
       ▼
Data Cleaning
       │
       ▼
Feature Engineering
       │
       ▼
Label Encoding
       │
       ▼
Feature Scaling
       │
       ▼
Train-Test Split
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Model Saving (.pkl)
       │
       ▼
Streamlit Deployment
```

---

# 🔍 Data Preprocessing

* Missing Value Handling
* Duplicate Removal
* Label Encoding
* Feature Scaling
* Feature Engineering
* Date Transformation
* Train-Test Split

### Feature Engineering

`Date_Posted`

↓

* Day
* Month
* Year

---

# 🤖 Machine Learning Models

| Model                       |      R² Score |
| --------------------------- | ------------: |
| Random Forest Regressor     | **0.9337** 🏆 |
| XGBoost Regressor           |        0.9302 |
| Extra Trees Regressor       |        0.9259 |
| Gradient Boosting Regressor |        0.9051 |
| Decision Tree Regressor     |        0.8581 |

### 🏆 Best Performing Model

**Random Forest Regressor**

* Highest Accuracy
* Lowest Prediction Error
* Best Generalization Performance

---

# 📈 Evaluation Metrics

The following metrics were used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

# 🖥 Streamlit Application

## Salary Prediction

Users can choose

* ML Model
* Job Title
* Company
* Company Type
* Industry
* City
* Location Tier
* Experience Level
* Job Type
* Work Mode
* Skills Required
* Education Required
* Openings
* Applicants
* Company Rating
* Date Posted

↓

**Predicted Salary (LPA)**

---

## Analytics Dashboard

The dashboard includes:

* Salary Distribution
* Top Hiring Cities
* Industry-wise Salary
* Work Mode Analysis
* Company Type Distribution
* Hiring Trends

---

# 📁 Project Structure

```text
AI_Job_Salary_Prediction
│
├── app.py
├── requirements.txt
├── README.md
├── india_job_market_2024_2026.csv
│
├── Models
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   ├── extra_trees.pkl
│   ├── gradient_boosting.pkl
│   ├── decision_tree.pkl
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
├── notebooks
│   └── model_training.ipynb
│
└── images
    ├── dashboard.png
    ├── prediction.png
    └── workflow.png
```

---

# 🚀 Installation

```bash
git clone <repository-url>

cd AI_Job_Salary_Prediction

pip install -r requirements.txt

streamlit run app.py
```

---

# 💻 Technologies Used

### Programming

* Python

### Machine Learning

* Scikit-Learn
* XGBoost

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

### Tools

* VS Code
* Jupyter Notebook
* GitHub

---

# 📊 Results

The proposed system achieved excellent performance for salary prediction.

✔ Best R² Score: **0.9337**

✔ Five Machine Learning models compared

✔ Interactive Web Application

✔ Real-time Salary Prediction

✔ Comprehensive Job Market Analytics

---

# 🚀 Future Scope

* Deep Learning Models
* Salary Recommendation Engine
* Resume-based Salary Prediction
* Explainable AI (SHAP/LIME)
* REST API using FastAPI
* Cloud Deployment
* Live Job Market Integration
* Auto Model Retraining

---

# 👨‍💻 Author

**Rishu Gurjar**

🎓 B.Tech Computer Science

🐍 Python Developer

🤖 Machine Learning Enthusiast

📊 Data Science Learner

---

# ⭐ If you found this project useful, don't forget to Star this repository!

---

## 📌 Conclusion

The **AI-Powered Job Salary Prediction System** is an end-to-end Machine Learning project that predicts job salaries based on various job-related features such as job title, company, industry, experience level, work mode, and education. Multiple regression models were trained and compared to identify the best-performing algorithm. Among them, the **Random Forest Regressor** achieved the highest accuracy with an **R² Score of 0.9337**. The project also includes an interactive **Streamlit web application** that enables real-time salary prediction and provides insightful data visualizations of the job market. Overall, this project demonstrates practical skills in data preprocessing, feature engineering, model evaluation, deployment, and building user-friendly AI applications for real-world use cases.

---

# 📜 License

This project is developed for educational, research, and learning purposes. Salary predictions are generated using Machine Learning models and should not be considered exact salary offers. Actual compensation may vary depending on company policies, candidate skills, market demand, and economic conditions.
