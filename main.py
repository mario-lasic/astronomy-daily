import requests
import streamlit as st
from datetime import date, timedelta
from api_key import api_key

st.set_page_config(layout="wide")

today = date.today()
yesterday = today - timedelta(days = 1)
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={yesterday}"

response = requests.get(url=url).text
print(response)