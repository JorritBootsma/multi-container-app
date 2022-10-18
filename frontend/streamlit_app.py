import os
import requests
import streamlit as st

# PROD_URL = "https://docker-tutorial-python.azurewebsites.net/"
# DEV_URL = "127.0.0.1:8080"

# BASE_URL = "127.0.0.1:8080/"

# BASE_URL = "http://backend:2000/"  # Works with Docker compose
# BASE_URL = "http://127.0.0.1:8080/"
# BASE_URL = "https://docker-tutorial-python.azurewebsites.net/"

BASE_URL = os.environ["TARGET_BASE_URL"]

st.title("Fill in your details!")

if st.button("Give me the version number!"):
    url_suffix = "version_number"
    st.write(BASE_URL + url_suffix)
    response = requests.get(BASE_URL + url_suffix)
    with st.spinner("Requesting version number"):
        st.write(response)
        st.write(response.json())


name = st.text_input("Name")
age = st.text_input("Age")

if st.button("Greet me!"):
    url_suffix = "streamlit_greeting"
    st.write(BASE_URL + url_suffix)
    response = requests.get(BASE_URL + url_suffix, params={"name": name, "age": age})
    with st.spinner("Requesting version number"):
        st.write(response)
        st.write(response.json())

if st.button("Say me goodbye!"):
    url_suffix = "streamlit_goodbye"
    st.write(BASE_URL + url_suffix)
    response = requests.get(BASE_URL + url_suffix, params={"name": name, "age": age})
    with st.spinner("Requesting version number"):
        st.write(response)
        st.write(response.json())
