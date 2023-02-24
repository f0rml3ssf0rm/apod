import requests
import streamlit as st


api = "37Uc7dEx13dDpsgR3WxFFSLViT7hEPsXztvBcaYF"
url = "https://api.nasa.gov/planetary/apod?api_key=37Uc7dEx13dDpsgR3WxFFSLViT7hEPsXztvBcaYF"

request = requests.get(url)
content = request.json()


st.header(content["title"])
st.image(content["url"])
st.write(content["explanation"])