
# Danh sách thuật toán
import streamlit as st
from FE_func import *
from func_cv2 import *


st.set_page_config(page_title="LightForge", page_icon="https://img.icons8.com/fluency/100/crafty-fox.png", layout="wide")


logo = "https://img.icons8.com/fluency/100/crafty-fox.png"
name_brand = "image/large_lg.png"
name_brand2 = "image/large_logo.png"

st.logo( name_brand, size="large", icon_image=name_brand2)

tab1, tab2 = st.tabs(["Manual Processing", "OpenCV Processing"])

with tab1:
    st.title("Manual Processing")
    algorithms = {
    "Add Gaussian Noise": "Thêm nhiễu Gaussian vào ảnh với tham số mean và sigma.",
    "Add Uniform Noise": "Thêm nhiễu Uniform vào ảnh với các giá trị trong khoảng [low, high].",
    "Add Salt and Pepper Noise": "Thêm nhiễu Salt-and-Pepper vào ảnh để mô phỏng nhiễu ngẫu nhiên."
    }

    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()))

    if selected_algorithm == "Add Gaussian Noise":
        add_gaussian_noise()

    if selected_algorithm == "Add Uniform Noise":
        add_uniform_noise()

    if selected_algorithm == "Add Salt and Pepper Noise":
        add_salt_pepper_noise()
    
with tab2:
    st.title("OpenCV Processing")
    algorithms = {
    "Add Gaussian Noise": "Thêm nhiễu Gaussian vào ảnh với tham số mean và sigma.",
    "Add Uniform Noise": "Thêm nhiễu Uniform vào ảnh với các giá trị trong khoảng [low, high]."
    }

    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()))

    if selected_algorithm == "Add Gaussian Noise":
        gaussian_noise_cv2()

    if selected_algorithm == "Add Uniform Noise":
        Uniform_Noise_cv2()







