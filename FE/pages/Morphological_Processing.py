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
  
    algorithms = {
    "Morphological Erosion": "Áp dụng phép co ảnh (erosion) để loại bỏ các chi tiết nhỏ hoặc làm mỏng đường biên.",
    "Morphological Dilation": "Áp dụng phép giãn ảnh (dilation) để mở rộng các chi tiết hoặc làm dày đường biên.",
    "Morphological Opening": "Áp dụng phép mở ảnh (opening) để loại bỏ nhiễu nhỏ và giữ lại cấu trúc chính.",
    "Morphological Closing": "Áp dụng phép đóng ảnh (closing) để lấp đầy lỗ hổng nhỏ và làm mịn đường biên."
    }


    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()))

    if selected_algorithm == "Morphological Erosion":
        morphological_erosion()

    if selected_algorithm == "Morphological Dilation":
        morphological_dilation()

    if selected_algorithm == "Morphological Opening":
        morphological_opening()

    if selected_algorithm == "Morphological Closing":
        morphological_closing()

    
with tab2:
    
    algorithms = {
    "Morphological Erosion": "Áp dụng phép co ảnh (erosion) để loại bỏ các chi tiết nhỏ hoặc làm mỏng đường biên.",
    "Morphological Dilation": "Áp dụng phép giãn ảnh (dilation) để mở rộng các chi tiết hoặc làm dày đường biên.",
    "Morphological Opening": "Áp dụng phép mở ảnh (opening) để loại bỏ nhiễu nhỏ và giữ lại cấu trúc chính.",
    "Morphological Closing": "Áp dụng phép đóng ảnh (closing) để lấp đầy lỗ hổng nhỏ và làm mịn đường biên."
    }


    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()), key="hello")

    if selected_algorithm == "Morphological Erosion":
        Erosion_cv2()
        
    if selected_algorithm == "Morphological Dilation":
        Dilation_cv2()
    if selected_algorithm == "Morphological Opening":
        opening_cv2()

    if selected_algorithm == "Morphological Closing":
        clossing_cv2()



