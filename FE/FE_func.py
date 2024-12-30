import streamlit as st
import requests
from PIL import Image
import zipfile
import io

def Bit_Plane_Slicing():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/bit-plane-slicing/"

    st.title("Bit Plane Slicing API")
    st.write("Upload an image to generate bit-plane sliced images and download them as a zip file.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"])

    if uploaded_file and st.button("Process Bit Plane Slicing"):
        try:
            # Đọc nội dung file
            file_bytes = uploaded_file.read()
            
            # Tạo payload và gửi request đến API
            files = {"image": (uploaded_file.name, file_bytes, "image/png")}
            response = requests.post(API_URL, files=files)
            
            if response.status_code == 200:
                # Lưu file zip từ API trả về
                zip_buffer = io.BytesIO(response.content)
                
                # Giải nén và hiển thị các ảnh bit-plane
                with zipfile.ZipFile(zip_buffer, "r") as zip_file:
                    st.success("Bit Plane Slicing Completed! Here are the bit-plane images:")
                    for name in zip_file.namelist():
                        with zip_file.open(name) as img_file:
                            image = Image.open(img_file)
                            st.image(image, caption=name, use_column_width=True)
                
                # Tải file zip về
                st.download_button(
                    label="Download Bit-Plane Images as Zip",
                    data=response.content,
                    file_name="bit_planes.zip",
                    mime="application/zip",
                )
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error connecting to the API: {e}")
#------------------------------------------
def negative_image():
    API_URL = "http://127.0.0.1:8000/negative-image/"

    st.title("Negative Image Transformation")
    st.write("Upload an image to generate its negative transformation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="negative_image_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        if st.button("Generate Negative Image"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Negative Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Negative Image", use_column_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Negative Image",
                        data=response.content,
                        file_name="negative_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#-------------------------------------------

def threshold_processing():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/threshold-processing/"

    st.title("Threshold Processing")
    st.write("Upload an image and set the threshold value to apply Threshold Processing.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="threshold_uploader")

    if uploaded_file:
        # Thiết lập giá trị ngưỡng
        threshold_value = st.slider("Threshold Value", min_value=0, max_value=255, value=50, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        if st.button("Apply Threshold Processing"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                data = {"threshold": threshold_value}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Thresholded Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Thresholded Image", use_column_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Thresholded Image",
                        data=response.content,
                        file_name="thresholded_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#-------------------------------------------

def logarithmic():
    API_URL = "http://127.0.0.1:8000/logarithmic/"

    st.title("Logarithmic Transformation")
    st.write("Upload an image to apply logarithmic transformation and enhance its details.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="logarithmic_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        if st.button("Apply Logarithmic Transformation"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Logarithmic Transformed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Logarithmic Transformed Image", use_column_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Transformed Image",
                        data=response.content,
                        file_name="logarithmic_transformed.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#--------------------------------------------

def powerlaw():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/powerlaw/"

    st.title("Power Law Transformation")
    st.write("Upload an image and set the gamma value to apply Power Law Transformation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="powerlaw_uploader")

    if uploaded_file:
        # Thiết lập giá trị gamma
        gamma = st.slider("Gamma Value", min_value=0.1, max_value=5.0, value=0.4, step=0.1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        if st.button("Apply Power Law Transformation"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                data = {"gamma": gamma}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Transformed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Transformed Image", use_column_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Transformed Image",
                        data=response.content,
                        file_name="powerlaw_transformed_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#-------------------------------------------

def piecewise_linear():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/piecewise-linear/"

    st.title("Piecewise Linear Transformation")
    st.write("Upload an image and set the parameters to apply Piecewise Linear Transformation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="piecewise_uploader")

    if uploaded_file:
         # Thiết lập các tham số piecewise linear
        st.subheader("Set Transformation Parameters")
        r1 = st.slider("R1 (Input Intensity)", min_value=0, max_value=255, value=90, step=1)
        s1 = st.slider("S1 (Output Intensity for R1)", min_value=0, max_value=255, value=40, step=1)
        r2 = st.slider("R2 (Input Intensity)", min_value=0, max_value=255, value=180, step=1)
        s2 = st.slider("S2 (Output Intensity for R2)", min_value=0, max_value=255, value=220, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        if st.button("Apply Piecewise Linear Transformation"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                data = {"r1": r1, "s1": s1, "r2": r2, "s2": s2}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Transformed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Transformed Image", use_column_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Transformed Image",
                        data=response.content,
                        file_name="piecewise_linear_transformed_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#-------------------------------------------