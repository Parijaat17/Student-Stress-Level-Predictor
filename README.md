# 🎓 Student Stress Level Predictor

This is a **Streamlit web application** that predicts the stress level of students based on their lifestyle details. The application uses a pre-trained machine learning model (`student_stress_model.pkl`) and a scaler (`scaler.pkl`) to preprocess the input data and make predictions.


---

[Streamlit](https://studentstresslevelprediction-es8zgtjxhweuqqfaxzrkid.streamlit.app/)

## Features

- Predicts **stress levels** (High Stress or Low Stress) based on:
  - Student Type (School, College, Working Student)
  - Sleep Hours
  - Study Hours
  - Social Media Hours
  - Attendance Percentage
  - Exam Pressure
  - Family Support
- User-friendly interface built with **Streamlit**.
- Scales input data using a pre-trained scaler to ensure consistency with the training phase.

---

## Requirements

- Python 3.8 or higher
- Libraries:
  - `streamlit`
  - `pandas`
  - `joblib`
  - `scikit-learn`

---

## Installation

1. Clone the repository or download the project files:
   ```bash
   git clone https://github.com/your-repo/student-stress-predictor.git
   cd student-stress-predictor
2. python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. pip install -r requirements.txt
4. streamlit run student_stress_model.py


---

### How to Use:
1. Save the above content as `README.md` in your project directory.
2. Update the `git clone` URL in the **Installation** section if you plan to host the project on GitHub.
3. Add a `requirements.txt` file with the following content:
