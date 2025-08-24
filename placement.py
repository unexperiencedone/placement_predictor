import pickle
import streamlit as st
# Now we will use a quick deploy by using streamlit library

placement = pickle.load(open('placement_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Title of the web app
st.title('Placement Predictor')

# input fields for the user

cgpa = st.number_input('Enter your CGPA', min_value = 0.0, max_value = 10.0, step = 0.01)
iq = st.number_input('Enter your IQ', min_value = 0, max_value = 200, step = 1)

# predict button
if st.button('Predict Placement'):
    scaled_input = scaler.transform([[cgpa, iq]])
    prediction = placement.predict(scaled_input)

    if prediction[0] == 1:
        st.success('Congratulations! You are likely to get placed.')
    else:
        st.error('Unfortunately, you are unlikely to get placed. Keep improving your skills!')
        # C:\Users\kumar\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install streamlit