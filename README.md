# Stroke-Prediction

**# Stroke Prediction App**

**## Overview**

This application harnesses a machine learning model to estimate an individual's risk of stroke based on various health factors. It's built with Python and Streamlit, offering a user-friendly interface for exploration.

**## Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maskedwolf4/Stroke-Prediction.git
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # (Linux/macOS)
   venv\Scripts\activate.bat  # (Windows)
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

**## Usage**

1. **Run the app:**

   ```bash
   streamlit run spapp.py
   ```

2. **Enter patient information:**
   - Gender
   - Age
   - Hypertension (Yes/No)
   - Heart Disease (Yes/No)
   - Residence Type (Urban/Rural)
   - Average Glucose Level
   - BMI
   - Smoking Status (formerly smoked/never smoked/smokes/Unknown)

3. **Click "Predict Stroke Risk" to generate the prediction.**

**## Model Details**

- **Model type:** XG BOOST
- **Features:**
-  - Gender
   - Age
   - Hypertension 
   - Heart Disease 
   - Residence Type 
   - Average Glucose Level
   - BMI
   - Smoking Status 

**## Disclaimer**

- **Limitations:** Acknowledge that the app provides estimates and shouldn't replace professional medical advice.
- **Medical guidance:** Strongly encourage users to consult healthcare professionals for diagnosis and treatment.

**## Contribute**

- Feel free to contribute to this project by submitting issues or pull requests.

**## License**

- This app is licensed under  MIT License.
