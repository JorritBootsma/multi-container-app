import os
import requests
import streamlit as st

# This environment variable is set in the frontend Dockerfile. It should correspond with
# the port set in the backend Dockerfile.
BASE_URL = os.environ["TARGET_BASE_URL"]

st.title("Fill in your details & Be Greeted!")
st.write('---')

name = st.text_input("Name")
age = st.text_input("Age")

if st.button("Greet me!"):
    url_suffix = "streamlit_greeting"
    response = requests.get(BASE_URL + url_suffix, params={"name": name, "age": age})
    with st.spinner("Requesting version number"):
        st.write(response.json())

if st.button("Say me goodbye!"):
    url_suffix = "streamlit_goodbye"
    response = requests.get(BASE_URL + url_suffix, params={"name": name, "age": age})
    with st.spinner("Requesting version number"):
        st.write(response.json())

st.write('---')

if st.button("Give me the version number!"):
    url_suffix = "version_number"
    st.write(f"Request sent to: {BASE_URL + url_suffix}")
    response = requests.get(BASE_URL + url_suffix)
    with st.spinner("Requesting version number"):
        st.write("Headers:")
        st.write(dict(response.headers))
        st.write("JSON Response:")
        st.write(response.json())

st.write('---')

if st.button("Persist my details in the database!"):
    url_suffix = "persist_in_db"
    response = requests.post(BASE_URL+url_suffix, params={"name": name, "age": age})
    st.write(response.json())
    if response.json()["response"] is True:
        st.success("Persisted in database!")
    else:
        st.error("Something went wrong!")

if st.button("Request information from database!"):
    url_suffix = "get_all_users"
    response = requests.get(BASE_URL+url_suffix)
    st.write(response.json())
