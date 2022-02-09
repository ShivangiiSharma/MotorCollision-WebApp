import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = (
    "./HospitalBedsIndia.csv"
)

st.title("Analyzing the data of COVID-19")
st.markdown("This was done in order to get the results"
            " for the research paper.")


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)

    return data


data = load_data(37)

if st.checkbox("Show Raw Data", False):
    st.subheader("Raw Data")
    st.write(data)
