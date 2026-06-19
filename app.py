import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Job Salary Predictor",
    page_icon="💼",
    layout="wide"
)

# -------------------------
# LOAD DATA
# -------------------------

df = pd.read_csv("india_job_market_2024_2026.csv")

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("💼 Navigation")

page = st.sidebar.radio(
    "Choose Section",
    [
        "Salary Prediction",
        "Data Visualization"
    ]
)

# -------------------------
# MODEL FILES
# -------------------------

model_files = {
    "Random Forest":"random_forest.pkl",
    "XGBoost":"xgboost.pkl",
    "Extra Trees":"extra_trees.pkl",
    "Gradient Boosting":"gradient_boosting.pkl",
    "Decision Tree":"decision_tree.pkl"
}

# ==========================
# PREDICTION PAGE
# ==========================

if page == "Salary Prediction":

    st.title("💰 AI Job Salary Prediction System")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        model_choice = st.selectbox(
            "Select ML Model",
            list(model_files.keys())
        )

        Job_Title = st.selectbox(
            "Job Title",
            sorted(df["Job_Title"].unique())
        )
        Company = st.selectbox(
            "Company",
            sorted(df["Company"].unique())
        )

        Company_Type = st.selectbox(
            "Company Type",
            sorted(df["Company_Type"].unique())
        )

        Industry = st.selectbox(
            "Industry",
            sorted(df["Industry"].unique())
        )

        City = st.selectbox(
            "City",
            sorted(df["City"].unique())
        )

        Location_Tier = st.selectbox(
            "Location Tier",
            sorted(df["Location_Tier"].unique())
        )

        Experience_Level = st.selectbox(
            "Experience Level",
            sorted(df["Experience_Level"].unique())
        )

    with col2:

        Job_Type = st.selectbox(
            "Job Type",
            sorted(df["Job_Type"].unique())
        )

        Work_Mode = st.selectbox(
            "Work Mode",
            sorted(df["Work_Mode"].unique())
        )

        Skills_Required = st.selectbox(
            "Skills Required",
            sorted(df["Skills_Required"].unique())
        )

        Education_Required = st.selectbox(
            "Education Required",
            sorted(df["Education_Required"].unique())
        )

        Openings = st.number_input(
            "Openings",
            min_value=1,
            value=5
        )

        Applicants = st.number_input(
            "Applicants",
            min_value=0,
            value=100
        )

        Company_Rating = st.slider(
            "Company Rating",
            1.0,
            5.0,
            4.0
        )
        date_input = st.date_input(
        "Job Posted Date"
        )

        Day = date_input.day
        Month = date_input.month
        Year = date_input.year

    st.markdown("---")

    if st.button("🚀 Predict Salary"):

        model = joblib.load(
            model_files[model_choice]
        )

        input_data = pd.DataFrame({
            "Job_Title":[Job_Title],
            "Company_Type":[Company_Type],
            "Industry":[Industry],
            "City":[City],
            "Location_Tier":[Location_Tier],
            "Experience_Level":[Experience_Level],
            "Job_Type":[Job_Type],
            "Work_Mode":[Work_Mode],
            "Skills_Required":[Skills_Required],
            "Education_Required":[Education_Required],
            "Openings":[Openings],
            "Applicants":[Applicants],
            "Company_Rating":[Company_Rating],
            "Day":[Day],
            "Month":[Month],
            "Year":[Year]
        })
        st.write("Input Columns")
        st.write(input_data.columns.tolist())

        st.write("Model Features")
        st.write(model.feature_names_in_)
        prediction = model.predict(input_data)

        st.success(
            f"🎯 Predicted Salary : ₹ {prediction[0]:.2f} LPA"
        )

# ==========================
# VISUALIZATION PAGE
# ==========================

if page == "Data Visualization":

    st.title("📊 Job Market Dashboard")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Salary",
        "City",
        "Industry",
        "Work Mode"
    ])

    with tab1:

        fig, ax = plt.subplots(figsize=(8,4))

        sns.histplot(
            df["Salary_LPA"],
            kde=True,
            ax=ax
        )

        st.pyplot(fig)

    with tab2:

        fig, ax = plt.subplots(figsize=(10,5))

        df["City"].value_counts().head(10).plot(
            kind="bar",
            ax=ax
        )

        st.pyplot(fig)

    with tab3:

        fig, ax = plt.subplots(figsize=(10,5))

        sns.boxplot(
            data=df,
            x="Industry",
            y="Salary_LPA",
            ax=ax
        )

        plt.xticks(rotation=90)

        st.pyplot(fig)

    with tab4:

        fig, ax = plt.subplots(figsize=(8,4))

        sns.barplot(
            data=df,
            x="Work_Mode",
            y="Salary_LPA",
            ax=ax
        )

        st.pyplot(fig)
