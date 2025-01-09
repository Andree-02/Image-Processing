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
    "Histogram Equalization": "Cải thiện độ tương phản của ảnh thông qua phân bổ lại histogram.",
    "Histogram Matching": "Điều chỉnh histogram của ảnh để phù hợp với ảnh tham chiếu."
    }

    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()),key="algorithm1")


    if selected_algorithm == "Histogram Equalization":
        Histogram_Equalization()
    if selected_algorithm == "Histogram Matching":
        histogram_matching()
    
    
    
with tab2:

    
    algorithms2 = {
    "Histogram Equalization": "Cải thiện độ tương phản của ảnh thông qua phân bổ lại histogram.",
    "Histogram Matching": "Điều chỉnh histogram của ảnh để phù hợp với ảnh tham chiếu."
    }

    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms2.keys()), key="algorithm2")


    if selected_algorithm == "Histogram Equalization":
        histogram_equalcv2()
    if selected_algorithm == "Histogram Matching":
        histo_matching_cv2()
    


 
