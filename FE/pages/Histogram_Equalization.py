# Danh sách thuật toán
import streamlit as st
from FE_func import *
st.set_page_config( page_icon="https://img.icons8.com/fluency/100/crafty-fox.png", layout="wide")

logo = "https://img.icons8.com/fluency/100/crafty-fox.png"
name_brand = "image/large_lg.png"
name_brand2 = "image/large_logo.png"

st.logo( name_brand, size="large", icon_image=name_brand2)

algorithms = {
    "Histogram Equalization": "Cải thiện độ tương phản của ảnh thông qua phân bổ lại histogram.",
    "Histogram Matching": "Điều chỉnh histogram của ảnh để phù hợp với ảnh tham chiếu."
}

# Widget chọn thuật toán
selected_algorithm = st.selectbox("Selected Algorithm:", list(algorithms.keys()))


if selected_algorithm == "Histogram Equalization":
    Histogram_Equalization()
if selected_algorithm == "Histogram Matching":
    histogram_matching()
 
