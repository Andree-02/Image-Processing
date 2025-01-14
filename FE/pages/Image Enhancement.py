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
    "Negative Images": "Chuyển đổi ảnh thành dạng âm bản.",
    "Threshold Image": "Phân ngưỡng để chuyển đổi ảnh thành ảnh nhị phân dựa trên giá trị ngưỡng.",
    "Logarithmic": "Áp dụng phép biến đổi log để nén dải động của ảnh.",
    "PowerLaw": "Thay đổi độ sáng và độ tương phản của ảnh bằng phép biến đổi lũy thừa.",
    "Piecewise": "Áp dụng phép biến đổi tuyến tính theo từng đoạn để cải thiện độ tương phản.",
    "Bit plane Slicing": "Phân tích và hiển thị từng mặt phẳng bit của ảnh."
    }

    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()))

    if selected_algorithm == "Negative Images":
        negative_image()

    if selected_algorithm == "Threshold Image":
        threshold_processing()

    if selected_algorithm == "Logarithmic":
        logarithmic()

    if selected_algorithm == "PowerLaw":
        powerlaw()

    if selected_algorithm == "Piecewise":
        piecewise_linear()

    if selected_algorithm == "Bit plane Slicing":
        Bit_Plane_Slicing()
    
with tab2:
  
    algorithms = {
    "Threshold Image": "Phân ngưỡng để chuyển đổi ảnh thành ảnh nhị phân dựa trên giá trị ngưỡng.",
    "Bit plane Slicing": "Phân tích và hiển thị từng mặt phẳng bit của ảnh."
    }

    # Widget chọn thuật toán
    selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()))

    if selected_algorithm == "Threshold Image":
        thresholding_cv2()

    if selected_algorithm == "Bit plane Slicing":
        bit_plane_slicing_cv2()



