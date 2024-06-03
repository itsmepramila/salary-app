import pickle
file = open('model.pickle', 'rb')
model = pickle.load(file)
file.close()

import streamlit as st
yoe = st.number_input("Years of Experience", value=0)


options = ("Bachelor's", "Master's", 'PhD')
selected_option = st.selectbox("Education Level", options=options)
ed_level = options.index(selected_option)

if st.button("Submit"):
    y_pred = model.predict( [[yoe, ed_level]] )
    st.write("Your estimated salary is ", y_pred[0])