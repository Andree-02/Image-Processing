# Danh sách thuật toán
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from FE_func import *
from func_cv2 import *

st.set_page_config(page_title="LightForge", page_icon="https://img.icons8.com/fluency/100/crafty-fox.png", layout="wide")

logo = "https://img.icons8.com/fluency/100/crafty-fox.png"
name_brand = "image/large_lg.png"
name_brand2 = "image/large_logo.png"

st.logo( name_brand, size="large", icon_image=name_brand2)

tab1, tab2 = st.tabs(["Manual Processing", "OpenCV Processing"])

with tab1:

    apply_frequency_filter()
    

with tab2:
    st.subheader("Coming Soon!")
    



