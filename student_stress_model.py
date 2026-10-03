import os
import streamlit as st
import pandas as pd
import joblib

# Get the absolute path of the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "student_stress_model.pkl")
scaler_path = os.path.join(script_dir, "scaler.pkl")

# Load the saved assets
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

st.title("🎓 Student Stress Level Predictor")
st.markdown("Enter the metrics below to predict the current stress level status.")
st.write("---")

# 2. Get RAW user inputs from Streamlit widgets
student_type_str = st.selectbox("Student Type", ["School", "College", "Working Student"])
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)
study_hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, value=4.0)
social_hours = st.number_input("Social Media Hours", min_value=0.0, max_value=24.0, value=2.0)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=85.0)
exam_pressure = st.slider("Exam Pressure (1-10)", 1, 10, 5)
family_support = st.slider("Family Support (1-10)", 1, 10, 5)

# 3. Map the categorical text to the training integer
mapping = {"School": 0, "College": 1, "Working Student": 2}
student_type_encoded = mapping[student_type_str]

# 4. Create a DataFrame with the correct feature names (matching training)
raw_inputs = pd.DataFrame([{
    "Student_Type": student_type_encoded,
    "Sleep_Hours": sleep_hours,
    "Study_Hours": study_hours,
    "Social_Media_Hours": social_hours,
    "Attendance": attendance,
    "Exam_Pressure": exam_pressure,
    "Family_Support": family_support
}])

# 5. Scale the raw inputs and predict
scaled_inputs = scaler.transform(raw_inputs)
prediction = model.predict(scaled_inputs)

# 6. Display output
if st.button("Predict Stress Level", type="primary"):
    
    # Place your model inference or calculation logic here
    # e.g., prediction = model.predict([[...]])
    
    # For now, displaying your default predicted status:
    st.success("Low Stress Level Predicted")
   
