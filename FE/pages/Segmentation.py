# Danh sách thuật toán
import streamlit as st
from FE_func import *

st.set_page_config(page_title="LightForge", page_icon="https://img.icons8.com/fluency/100/crafty-fox.png", layout="wide")


logo = "https://img.icons8.com/fluency/100/crafty-fox.png"
name_brand = "image/large_lg.png"
name_brand2 = "image/large_logo.png"

st.logo( name_brand, size="large", icon_image=name_brand2)

tab1, tab2 = st.tabs(["Manual Processing", "OpenCV Processing"])

with tab1:
    st.title("Manual Processing")
    otsu_threshold()
    
with tab2:
    st.title("OpenCV Processing")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


