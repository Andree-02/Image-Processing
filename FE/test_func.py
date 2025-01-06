from FE_func import *
import streamlit as st
import requests
from PIL import Image
import zipfile
import io
import base64
import os




# Logo URL và tên thương hiệu
logo = "https://img.icons8.com/fluency/100/crafty-fox.png"
brand_name = "LightForge"

# Hiển thị logo và tên thương hiệu
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="{logo}" alt="Logo" style="width: 50px; height: 50px; margin-right: 15px;">
        <h1 style="display: inline; font-size: 32px; color: #333;">{brand_name}</h1>
    </div>
    """,
    unsafe_allow_html=True
)
