import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = (
    "./Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This is a Streamit dashboard that can be used"
            "to analyze the motor vehicle collision in NYC 🗽💥🚗")


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[
                       ['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)

    return data


data = load_data(100000)

st.header("Where are the most people injured in NYC?")


if st.checkbox("Show Raw Data", False):
    st.subheader("Raw Data")
    st.write(data)

injured_people = st.slider("", 0, 19)
