#EAEDF9
import json
import requests
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title='MFDPS', layout = 'wide', page_icon = '/Users/soumyadwipmondal/Downloads/logo.png', initial_sidebar_state = 'auto')
st.sidebar.image("/Users/soumyadwipmondal/Downloads/logo5.png", use_column_width=True)

diabetes_model = pickle.load(open('/Users/soumyadwipmondal/Downloads/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Users/soumyadwipmondal/Downloads/heart_disease_model.sav','rb'))


with st.sidebar:
    
    selected = option_menu('Multi Functionality Disorder Prediction System',
                            ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['heart','activity'],
                           default_index=0)
# Diabetes:-  

if (selected == 'Diabetes Prediction'):
    
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    def load_lottieurl(url: str):
        r =requests .get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tbjuenb2.json")
    st_lottie(
        lottie_hello,
        speed=3,
        reverse=False,
        loop=True,
        quality="high",
        height=500,
        width=500,
        key=None,
    )
    
    # page title
    st.title('Diabetes Prediction using Machine Learning')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        with st.spinner(text="Please Wait!! Calculating your inputs..."):
            time.sleep(5)
            st.snow()
        
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = st.error('The person is diabetic.',icon="❌")
        else:
          diab_diagnosis = st.success('The person is not diabetic.',icon="✅")
    
    
   
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    def load_lottieurl(url: str):
        r =requests .get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_pcqghvjn.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=500,
        width=500,
        key=None,
    )
    
    # page title
    st.title('Heart Disease Prediction using Machine Learning...')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    heart_diagnosis = ''
 
    if st.button('Heart Disease Test Result'):
        for i in range (100):
            st.spinner(text="Please Wait!!! We are Calculating your inputs....")
            time.sleep(5)
        st.snow()
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = st.error('The person is having heart disease',icon="❌")
        else:
          heart_diagnosis = st.success('The person does not have any heart disease',icon="✅")