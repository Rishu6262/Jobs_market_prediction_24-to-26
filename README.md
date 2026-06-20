# 💼 AI-Powered Job Salary Prediction System

## 📌 Project Overview

The AI-Powered Job Salary Prediction System is a Machine Learning project designed to predict the expected salary (LPA) of a job posting based on multiple job-related factors such as job title, company, industry, location, experience level, work mode, education requirements, company rating, and more.

This project compares multiple Machine Learning algorithms and allows users to select different models for salary prediction through an interactive Streamlit web application.

---

## 🚀 Features

* Predict Job Salary in LPA
* Multiple Machine Learning Models
* Interactive Streamlit User Interface
* Real-Time Salary Prediction
* Job Market Data Visualization Dashboard
* Model Comparison and Evaluation
* User-Friendly Input Selection
* Industry-wise Salary Analysis
* City-wise Job Analysis
* Work Mode Analysis
* Company Type Analysis

---

## 📊 Dataset Information

The dataset contains Indian job market information collected from various sectors between 2024 and 2026.

### Dataset Features

| Feature            | Description                     |
| ------------------ | ------------------------------- |
| Job_Title          | Job Position Name               |
| Company            | Company Name                    |
| Company_Type       | Startup, MNC, PSU/Govt, Unicorn |
| Industry           | Industry Category               |
| City               | Job Location                    |
| Location_Tier      | Tier 1, Tier 2, Tier 3 Cities   |
| Experience_Level   | Fresher, Junior, Mid, Senior    |
| Job_Type           | Full-Time, Part-Time, Contract  |
| Work_Mode          | Remote, Hybrid, Onsite          |
| Skills_Required    | Required Skills                 |
| Education_Required | Educational Qualification       |
| Openings           | Number of Vacancies             |
| Applicants         | Number of Applicants            |
| Company_Rating     | Company Rating                  |
| Date_Posted        | Job Posting Date                |
| Salary_LPA         | Target Variable                 |

---

## ⚙️ Machine Learning Workflow

### Data Preprocessing

* Handling Missing Values
* Label Encoding
* Date Feature Engineering
* Feature Selection
* Data Transformation
* Feature Scaling using StandardScaler

### Feature Engineering

Date Posted column was transformed into:

* Day
* Month
* Year

for improved model performance.

---

## 🤖 Machine Learning Models Used

### 1. Decision Tree Regressor

* R² Score: 0.8581

### 2. Gradient Boosting Regressor

* R² Score: 0.9051

### 3. Extra Trees Regressor

* R² Score: 0.9259

### 4. XGBoost Regressor

* R² Score: 0.9302

### 5. Random Forest Regressor

* R² Score: 0.9337

### Best Model

🏆 Random Forest Regressor

R² Score: 0.9337

---

## 📈 Model Evaluation Metrics

The following evaluation metrics were used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 🖥️ Streamlit Application

The Streamlit application provides:

### Salary Prediction Page

Users can select:

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
* Company Rating
* Openings
* Applicants
* Date Posted

and receive an instant salary prediction.

### Data Visualization Dashboard

Interactive visualizations include:

* Salary Distribution
* Top Hiring Cities
* Industry-wise Salary Analysis
* Work Mode Analysis
* Company Type Analysis

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* GitHub
* Streamlit Cloud

---

## 📂 Project Structure

```bash
AI_Job_Salary_Prediction/
│
├── app.py
├── india_job_market_2024_2026.csv
├── random_forest.pkl
├── xgboost.pkl
├── extra_trees.pkl
├── gradient_boosting.pkl
├── decision_tree.pkl
├── scaler.pkl
├── label_encoders.pkl
├── requirements.txt
├── README.md
│
└── notebooks/
    └── model_training.ipynb
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📊 Results

The project achieved excellent performance in salary prediction.

| Model             | R² Score |
| ----------------- | -------- |
| Random Forest     | 0.9337   |
| XGBoost           | 0.9302   |
| Extra Trees       | 0.9259   |
| Gradient Boosting | 0.9051   |
| Decision Tree     | 0.8581   |

Random Forest Regressor delivered the highest prediction accuracy and was selected as the best-performing model.

---

## 🎯 Future Improvements

* Deep Learning Integration
* Salary Recommendation Engine
* Resume-Based Salary Prediction
* Job Recommendation System
* Explainable AI (XAI)
* Real-Time Job Market Analysis
* Cloud Deployment
* API Integration using FastAPI

---

## 👨‍💻 Author

Rishu Gurjar

B.Tech Student | Python Developer | Machine Learning Enthusiast | Data Science Learner

---

## 📌 Conclusion

The AI-Powered Job Salary Prediction System successfully demonstrates the application of Machine Learning techniques to predict job salaries based on various job-related attributes such as job title, company type, industry, location, experience level, work mode, skills required, and company ratings.

Multiple regression models were trained and evaluated, including Decision Tree, Gradient Boosting, Extra Trees, XGBoost, and Random Forest Regressors. Among all models, the Random Forest Regressor achieved the highest performance with an R² Score of 0.9337, making it the most accurate model for salary prediction.

The project not only provides reliable salary predictions but also offers an interactive Streamlit dashboard for data visualization and model comparison. Through this project, valuable insights into the Indian job market were obtained, helping users understand salary trends across different industries, cities, and job roles.

Overall, this project showcases the practical implementation of Data Science, Machine Learning, Data Visualization, and Web Application Development, making it a comprehensive real-world solution for salary prediction and job market analysis.

---

## 📜 Disclaimer

This project is developed for educational, research, and learning purposes. Salary predictions generated by the system are based on historical job market data and machine learning models. Actual salary offerings may vary depending on company policies, market trends, candidate skills, and economic conditions.
