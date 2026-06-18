import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(
    page_title="AI Job Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("india_job_market_2024_2026.csv")

# =========================
# LOAD MODELS
# =========================

models = {
    "Random Forest": joblib.load("random_forest.pkl"),
    "XGBoost": joblib.load("xgboost.pkl"),
    "Gradient Boosting": joblib.load("gradient_boosting.pkl"),
    "Decision Tree": joblib.load("decision_tree.pkl")
}

# =========================
# HEADER
# =========================

st.title("💼 AI Job Salary Prediction System")

st.markdown(
"""
Predict Salary Packages using Multiple Machine Learning Models.
"""
)

# =========================
# SIDEBAR
# =========================

st.sidebar.header("Model Selection")

model_name = st.sidebar.selectbox(
    "Choose Model",
    list(models.keys())
)

model = models[model_name]

# =========================
# USER INPUTS
# =========================

st.subheader("📋 Enter Job Details")

col1, col2 = st.columns(2)

with col1:

    company_type = st.selectbox(
        "Company Type",
        sorted(df["Company_Type"].unique())
    )

    industry = st.selectbox(
        "Industry",
        sorted(df["Industry"].unique())
    )

    city = st.selectbox(
        "City",
        sorted(df["City"].unique())
    )

    location_tier = st.selectbox(
        "Location Tier",
        sorted(df["Location_Tier"].unique())
    )

    experience = st.selectbox(
        "Experience Level",
        sorted(df["Experience_Level"].unique())
    )

with col2:

    job_type = st.selectbox(
        "Job Type",
        sorted(df["Job_Type"].unique())
    )

    work_mode = st.selectbox(
        "Work Mode",
        sorted(df["Work_Mode"].unique())
    )

    education = st.selectbox(
        "Education Required",
        sorted(df["Education_Required"].unique())
    )

    company_rating = st.slider(
        "Company Rating",
        1.0,
        5.0,
        4.0
    )

    openings = st.number_input(
        "Openings",
        min_value=1,
        value=5
    )

# =========================
# ADDITIONAL INPUTS
# =========================

job_title = st.selectbox(
    "Job Title",
    sorted(df["Job_Title"].unique())
)

company = st.selectbox(
    "Company",
    sorted(df["Company"].unique())
)

skills = st.selectbox(
    "Skills Required",
    sorted(df["Skills_Required"].unique())
)

applicants = st.number_input(
    "Applicants",
    min_value=0,
    value=100
)

# =========================
# PREDICT BUTTON
# =========================

if st.button("🚀 Predict Salary"):

    input_df = pd.DataFrame({

        "Job_Title":[job_title],
        "Company":[company],
        "Company_Type":[company_type],
        "Industry":[industry],
        "City":[city],
        "Location_Tier":[location_tier],
        "Experience_Level":[experience],
        "Job_Type":[job_type],
        "Work_Mode":[work_mode],
        "Skills_Required":[skills],
        "Education_Required":[education],
        "Openings":[openings],
        "Applicants":[applicants],
        "Company_Rating":[company_rating]

    })
    try:
    prediction = model.predict(input_df)
    st.success(f"💰 Predicted Salary: ₹ {prediction[0]:.2f} LPA")

    except Exception as e:
    st.error(str(e))
    st.write("Input Columns:", list(input_df.columns))
    st.stop()
    prediction = model.predict(input_df)

    st.success(
        f"💰 Predicted Salary: ₹ {prediction[0]:.2f} LPA"
    )

    # =========================
    # VISUALIZATION
    # =========================

    st.subheader("📊 Dataset Insights")

    c1, c2 = st.columns(2)

    with c1:

        fig = px.box(
            df,
            x="Experience_Level",
            y="Salary_LPA",
            title="Salary by Experience"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig2 = px.bar(
            df.groupby("Work_Mode")["Salary_LPA"]
            .mean()
            .reset_index(),
            x="Work_Mode",
            y="Salary_LPA",
            title="Average Salary by Work Mode"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.subheader("🏙️ City Wise Salary")

    fig3 = px.bar(
        df.groupby("City")["Salary_LPA"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(),
        x="City",
        y="Salary_LPA"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.subheader("🏢 Company Type Salary")

    fig4 = px.pie(
        df,
        names="Company_Type",
        title="Company Type Distribution"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )
