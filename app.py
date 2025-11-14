import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.set_page_config(page_title="🩺 Medical Billing Analyzer", layout="wide")
st.title("🩺 MediCloud - Medical Billing Analyzer")
st.write("Analyze patient bills, doctor performance, and revenue trends.")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("medical_billing_dataset.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("🔎 Filters")
doctor_filter = st.sidebar.multiselect("Select Doctor(s)", options=df["Doctor"].unique(), default=df["Doctor"].unique())
gender_filter = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
symptom_filter = st.sidebar.multiselect("Select Symptom(s)", options=df["Symptom"].unique(), default=df["Symptom"].unique())

# Apply filters
filtered_df = df[
    (df["Doctor"].isin(doctor_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["Symptom"].isin(symptom_filter))
]

# Show dataset
#st.subheader("📋 Patient Records")
#st.dataframe(filtered_df, use_container_width=True)

# Summary Stats
st.subheader("📊 Key Insights")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Patients", len(filtered_df))
with col2:
    st.metric("Total Revenue (₹)", int(filtered_df["TotalBill"].sum()))
with col3:
    st.metric("Avg Bill per Patient (₹)", int(filtered_df["TotalBill"].mean()))

# Visualization 1: Revenue by Doctor
st.subheader("💰 Revenue by Doctor")
revenue_doctor = filtered_df.groupby("Doctor")["TotalBill"].sum().sort_values(ascending=False)
fig1, ax1 = plt.subplots()
revenue_doctor.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Revenue (₹)")
st.pyplot(fig1)

# Visualization 2: Common Symptoms
st.subheader("🤒 Most Common Symptoms")
symptom_counts = filtered_df["Symptom"].value_counts()
fig2, ax2 = plt.subplots()
symptom_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# Visualization 3: Gender Distribution
st.subheader("👩‍⚕️ Patient Gender Distribution")
gender_counts = filtered_df["Gender"].value_counts()
fig3, ax3 = plt.subplots()
gender_counts.plot(kind="bar", color=["blue", "pink"], ax=ax3)
ax3.set_ylabel("Number of Patients")
st.pyplot(fig3)

# Download Option
st.subheader("📥 Download Filtered Data")
st.download_button("Download CSV", data=filtered_df.to_csv(index=False), file_name="filtered_medical_billing.csv", mime="text/csv")
