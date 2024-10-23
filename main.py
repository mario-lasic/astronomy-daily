import requests
import streamlit as st
from datetime import date, timedelta
from api_key import api_key

st.set_page_config(layout="wide")

today = date.today()
yesterday = today - timedelta(days = 1)
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={yesterday}"

response = requests.get(url=url).json()

st.html(
    "<div style='text-align: center; margin: auto; width:60%'>"
        f"<h1 style='margin-bottom: 1rem'>{response["title"]}</h1>"
        f"<img src='{response["url"]}' style='object-fit: contain; width: 100%;'></img>"
        f"<p style='margin-top: 20px; text-align: center;'>{response["explanation"]}</p>"
    "</div>"
)