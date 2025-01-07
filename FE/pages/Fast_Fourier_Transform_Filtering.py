# Danh sách thuật toán
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from FE_func import *

st.set_page_config(page_title="LightForge", page_icon="https://img.icons8.com/fluency/100/crafty-fox.png", layout="wide")

logo = "https://img.icons8.com/fluency/100/crafty-fox.png"
name_brand = "image/large_lg.png"
name_brand2 = "image/large_logo.png"

st.logo( name_brand, size="large", icon_image=name_brand2)

tab1, tab2 = st.tabs(["Manual Processing", "OpenCV Processing"])

with tab1:
    st.title("Fast Fourier Transform Filtering")
    apply_frequency_filter()
    
with tab2:
    st.title("OpenCV Processing")
    
        # Hàm thresholding
    def thresholding(image, thresh):
        _, binary_image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
        return binary_image

    # Giao diện Streamlit
    st.header("Image Thresholding App")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh
        image = np.array(Image.open(uploaded_file, ).convert("L"))  # Chuyển ảnh sang grayscale
        
        col1, col2 = st.columns(2)

        with col1:
            st.header("A cat")

        
            
        
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Thanh trượt để chọn ngưỡng (threshold)
        threshold_value = st.slider("Select threshold value", min_value=0, max_value=255, value=127)

        # Áp dụng hàm thresholding
        binary_image = thresholding(image, threshold_value)
        
        with col2:
            st.header("A dog")

            # Hiển thị ảnh nhị phân kết quả
            st.image(binary_image, caption="Thresholded Image", width=500)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(binary_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Thresholded Image",
            data=byte_im,
            file_name="thresholded_image.png",
            mime="image/png"
        )




