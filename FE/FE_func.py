import streamlit as st
import requests
from PIL import Image
import zipfile
import io

def Bit_Plane_Slicing():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/bit-plane-slicing/"

    st.header("Bit Plane Slicing API")
    st.write("Upload an image to generate bit-plane sliced images and download them as a zip file.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"])

    if uploaded_file and st.button("Process Bit Plane Slicing"):
        try:
            # Đọc nội dung file
            file_bytes = uploaded_file.read()
            
            # Tạo payload và gửi request đến API
            #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
            uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
            files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
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
                            st.image(image, caption=name, use_container_width=True)
                
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

    st.header("Negative Image Transformation")
    st.write("Upload an image to generate its negative transformation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="negative_image_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Generate Negative Image"):
            try:
                # Đọc nội dung file
                #file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Negative Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Negative Image", use_container_width=True)

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

    st.header("Threshold Processing")
    st.write("Upload an image and set the threshold value to apply Threshold Processing.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="threshold_uploader")

    if uploaded_file:
        # Thiết lập giá trị ngưỡng
        threshold_value = st.slider("Threshold Value", min_value=0, max_value=255, value=50, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Threshold Processing"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"threshold": threshold_value}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Thresholded Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Thresholded Image", use_container_width=True)

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

    st.header("Logarithmic Transformation")
    st.write("Upload an image to apply logarithmic transformation and enhance its details.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="logarithmic_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Logarithmic Transformation"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Logarithmic Transformed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Logarithmic Transformed Image", use_container_width=True)

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

    st.header("Power Law Transformation")
    st.write("Upload an image and set the gamma value to apply Power Law Transformation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="powerlaw_uploader")

    if uploaded_file:
        # Thiết lập giá trị gamma
        gamma = st.slider("Gamma Value", min_value=0.1, max_value=5.0, value=0.4, step=0.1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Power Law Transformation"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"gamma": gamma}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Transformed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Transformed Image", use_container_width=True)

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

    st.header("Piecewise Linear Transformation")
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
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Piecewise Linear Transformation"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"r1": r1, "s1": s1, "r2": r2, "s2": s2}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Transformed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Transformed Image", use_container_width=True)

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

def Histogram_Equalization():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/histogram-equalization/"

    st.header("Histogram Equalization")
    st.write("Upload an image to apply histogram equalization and enhance its contrast.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="unique_key_2")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Process Histogram Equalization"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Equalized Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Histogram Equalized Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Equalized Image",
                        data=response.content,
                        file_name="equalized_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#----------------------------------------------

def morphological_erosion():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/morphological/erosion/"

    st.header("Morphological Erosion")
    st.write("Upload an image and set the kernel size to apply morphological erosion.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="erosion_uploader")



    if uploaded_file:
        # Cài đặt kích thước kernel
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=3, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Morphological Erosion"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"kernel_size": kernel_size}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Eroded Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Eroded Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Eroded Image",
                        data=response.content,
                        file_name="eroded_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#-----------------------------------------------------------------
def morphological_dilation():

    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/morphological/dilation/"

    st.header("Morphological Dilation")
    st.write("Upload an image and set the kernel size to apply morphological dilation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="dilation_uploader")



    if uploaded_file:
        # Cài đặt kích thước kernel
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=3, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Morphological Dilation"):
            try:

                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"kernel_size": kernel_size}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Dilated Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Dilated Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Dilated Image",
                        data=response.content,
                        file_name="dilated_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#---------------------------------------------------------
def morphological_opening():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/morphological/opening/"

    st.header("Morphological Opening")
    st.write("Upload an image and set the kernel size to apply morphological opening.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="opening_uploader")



    if uploaded_file:
        # Cài đặt kích thước kernel
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=3, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Morphological Opening"):
            try:
                

                # Tạo payload và gửi request đến API
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"kernel_size": kernel_size}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Opened Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Opened Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Opened Image",
                        data=response.content,
                        file_name="opened_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#---------------------------------------------------------
def morphological_closing():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/morphological/closing/"

    st.header("Morphological Closing")
    st.write("Upload an image and set the kernel size to apply morphological closing.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="closing_uploader")



    if uploaded_file:
        # Cài đặt kích thước kernel
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=3, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Morphological Closing"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"kernel_size": kernel_size}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Closed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Closed Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Closed Image",
                        data=response.content,
                        file_name="closed_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#-------------------------------
def otsu_threshold():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/otsu-threshold/"

    st.header("Otsu's Thresholding")
    st.write("Upload an image to apply Otsu's Thresholding for automatic binary segmentation.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="otsu_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Otsu's Thresholding"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Thresholded Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Thresholded Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Thresholded Image",
                        data=response.content,
                        file_name="otsu_thresholded_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#--------------------------------------------------------------

#----------------------------------------------------------------
def mean_filter():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/mean-filter-manual/"

    st.header("Mean Filter")
    st.write("Upload an image and set the kernel size to apply Mean Filter.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="mean_filter_uploader")

    if uploaded_file:
        # Thiết lập kích thước bộ lọc
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=3, step=1)
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Mean Filter"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"size": kernel_size}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Filtered Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Filtered Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Filtered Image",
                        data=response.content,
                        file_name="mean_filter_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#-------------------------------------------------------------
#-------------------------------------------------------------------------
def median_filter():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/median-filter-manual/"

    st.header("Median Filter")
    st.write("Upload an image and set the kernel size to apply Median Filter.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="median_filter_uploader")

    # Thiết lập kích thước bộ lọc
   

    if uploaded_file:
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=3, step=1, key="kernel_size_slider")
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Median Filter"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"size": kernel_size}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Filtered Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Filtered Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Filtered Image",
                        data=response.content,
                        file_name="median_filter_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#-------------------------------------------
def normalized_correlation():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/normalized-correlation-manual/"

    st.header("Normalized Correlation")
    st.write("Upload an image and a template image to apply Normalized Correlation.")

    # Tải ảnh gốc lên
    uploaded_file = st.file_uploader("Upload the main image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="main_image_uploader")

    if uploaded_file:
        # Tải ảnh template lên
        uploaded_template = st.file_uploader("Upload the template image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="template_image_uploader")
        # Hiển thị ảnh gốc và template
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            original_image = Image.open(uploaded_file)
            st.image(original_image, caption="Original Image", use_container_width=True)
        with col2:
            st.subheader("Template Image")
            template_image = Image.open(uploaded_template)
            st.image(template_image, caption="Template Image", use_container_width=True)

        if st.button("Apply Normalized Correlation"):
            try:
                # Đảm bảo con trỏ file ở đầu
                uploaded_file.seek(0) 
                uploaded_template.seek(0) 
                # Tạo payload và gửi request đến API
                files = {
                    "image": (uploaded_file.name, uploaded_file, uploaded_file.type),
                    "template": (uploaded_template.name, uploaded_template, uploaded_template.type),
                }
                
                 
            
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Resulting Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Resulting Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Resulting Image",
                        data=response.content,
                        file_name="normalized_correlation_result.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#--------------------------------------------------
def sharpening_laplacian():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/sharpening-laplacian/"

    st.header("Sharpening with Laplacian")
    st.write("Upload an image to apply Laplacian sharpening.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="sharpening_laplacian_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Laplacian Sharpening"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Sharpened Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Sharpened Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Sharpened Image",
                        data=response.content,
                        file_name="sharpened_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#------------------------------------------------------------

def apply_frequency_filter():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/apply-frequency-filter/"
    
   # Chọn loại bộ lọc
    filter_type = st.selectbox(
        "Select Filter Type:",
        options=["ideal", "butterworth", "gaussian"],
        index=2,  # Default to "gaussian"
        key="filter_type_selectbox"
    )

    st.header("Apply Frequency Filter")
    st.write("Upload an image and set filter parameters to apply frequency-based filtering.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload a grayscale image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="frequency_filter_uploader")

 
    if uploaded_file:
        # Thiết lập tham số cutoff
        cutoff = st.slider(
        "Cutoff Frequency:",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        key="cutoff_slider"
        )

        # Thiết lập tham số order (chỉ hiển thị nếu loại bộ lọc là Butterworth)
        order = 2
        if filter_type == "butterworth":
            order = st.slider(
                "Filter Order (Butterworth):",
                min_value=1,
                max_value=10,
                value=2,
                step=1,
                key="order_slider"
            )
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Apply Frequency Filter"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {
                    "filter_type": filter_type,
                    "cutoff": cutoff,
                    "order": order,
                }
                
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Filtered Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Filtered Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Filtered Image",
                        data=response.content,
                        file_name=f"{filter_type}_frequency_filtered_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#-----------------------------------------------------------
def add_gaussian_noise():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/add-gaussian-noise/"

    st.header("Add Gaussian Noise")
    st.write("Upload an image and set mean and sigma values to add Gaussian noise.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="gaussian_noise_uploader")


    if uploaded_file:
        # Thiết lập giá trị mean và sigma
        mean = st.slider("Mean (μ)", min_value=-100.0, max_value=100.0, value=0.0, step=1.0, key="mean_slider")
        sigma = st.slider("Sigma (σ)", min_value=1.0, max_value=100.0, value=25.0, step=1.0, key="sigma_slider")

        
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Add Gaussian Noise"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"mean": mean, "sigma": sigma}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Noisy Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Noisy Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Noisy Image",
                        data=response.content,
                        file_name="gaussian_noisy_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#----------------------------------------------------

def add_uniform_noise():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/add-uniform-noise/"  # Đảm bảo URL API là chính xác

    # Tiêu đề ứng dụng
    st.header("Add Uniform Noise to Image")
    st.write("Tải ảnh lên và thêm nhiễu Uniform (Uniform Noise) vào ảnh.")

    # Widget tải ảnh
    uploaded_file = st.file_uploader("Tải ảnh lên (JPG/PNG):", type=["jpg", "jpeg", "png"])

    

    # Nút thực hiện
    if uploaded_file and st.button("Thêm Uniform Noise"):
        # Tham số nhiễu
        low = st.slider("Nhập giá trị thấp của nhiễu (Low):", min_value=-100, max_value=0, value=-50, step=1)
        high = st.slider("Nhập giá trị cao của nhiễu (High):", min_value=0, max_value=100, value=50, step=1)
        
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)
        
        try:
            # Đọc nội dung file
            file_bytes = uploaded_file.read()
            
            # Tạo payload và gửi request tới API
            #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
            uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
            files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            data = {"low": low, "high": high}
            response = requests.post(API_URL, files=files, data=data)
            
            if response.status_code == 200:
                # Hiển thị ảnh kết quả
                result_image = Image.open(io.BytesIO(response.content))
                st.image(result_image, caption="Ảnh đã thêm Uniform Noise", use_container_width=True)

                # Nút tải ảnh kết quả
                st.download_button(
                    label="Tải ảnh kết quả",
                    data=response.content,
                    file_name="noisy_image.png",
                    mime="image/png",
                )
            else:
                st.error(f"Lỗi API: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Lỗi kết nối API: {e}")

#----------------------------------------------------
def add_salt_pepper_noise():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/add-salt-pepper-noise/"

    st.header("Add Salt-and-Pepper Noise")
    st.write("Upload an image and set the salt and pepper probabilities to add Salt-and-Pepper noise.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="salt_pepper_noise_uploader")

    

    if uploaded_file:
        # Thiết lập xác suất Salt và Pepper
        salt_prob = st.slider("Salt Probability:", min_value=0.0, max_value=1.0, value=0.01, step=0.01, key="salt_prob_slider")
        pepper_prob = st.slider("Pepper Probability:", min_value=0.0, max_value=1.0, value=0.01, step=0.01, key="pepper_prob_slider")
        
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_container_width=True)

        if st.button("Add Salt-and-Pepper Noise"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {"salt_prob": salt_prob, "pepper_prob": pepper_prob}
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Noisy Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Noisy Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Noisy Image",
                        data=response.content,
                        file_name="salt_pepper_noisy_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

#-----------------------------------------------------------------
def histogram_matching():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/histogram-matching/"

    st.header("Histogram Matching")
    st.write("Upload a source image and a reference image to perform Histogram Matching.")

    # Tải ảnh nguồn (source image) lên
    uploaded_source_image = st.file_uploader(
        "Upload the source image (JPG/PNG):",
        type=["jpg", "jpeg", "png"],
        key="source_image_uploader",
    )

    # Tải ảnh tham chiếu (reference image) lên
    uploaded_reference_image = st.file_uploader(
        "Upload the reference image (JPG/PNG):",
        type=["jpg", "jpeg", "png"],
        key="reference_image_uploader",
    )

    if uploaded_source_image and uploaded_reference_image:
        col1, col2 = st.columns(2)
        with col1:
            # Hiển thị ảnh nguồn và ảnh tham chiếu
            st.subheader("Source Image")
            source_image = Image.open(uploaded_source_image)
            st.image(source_image, caption="Source Image", use_container_width=True)
        with col2:
            st.subheader("Reference Image")
            reference_image = Image.open(uploaded_reference_image)
            st.image(reference_image, caption="Reference Image", use_container_width=True)

        if st.button("Perform Histogram Matching"):
            try:
                # Đọc nội dung file
                #source_image_bytes = uploaded_source_image.read()
                #reference_image_bytes = uploaded_reference_image.read()

                uploaded_source_image.seek(0)  # Đảm bảo con trỏ file ở đầu
                uploaded_reference_image.seek(0)
                # Tạo payload và gửi request đến API
                files = {
                    "source_image": (uploaded_source_image.name, uploaded_source_image, uploaded_source_image.type),
                    "reference_image": (uploaded_reference_image.name, uploaded_reference_image, uploaded_reference_image.type),
                }
                
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Matched Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Matched Image", use_container_width=True)

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Matched Image",
                        data=response.content,
                        file_name="histogram_matched_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#---------------------------------------------------------
def compression_rle():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/compression-rle/"

    st.header("RLE Compression and Decompression")
    st.write("Upload an image to perform RLE compression and decompression. The system will display the decompressed image and the RMS value.")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG):", type=["jpg", "jpeg", "png"], key="rle_uploader")

    if uploaded_file:
        # Hiển thị ảnh gốc
        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        if st.button("Compress and Decompress"):
            try:
                # Đọc nội dung file
                file_bytes = uploaded_file.read()

                # Tạo payload và gửi request đến API
                #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
                uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
                files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    # Hiển thị ảnh kết quả
                    st.subheader("Decompressed Image")
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption="Decompressed Image", use_column_width=True)

                    # Hiển thị giá trị RMS (giả định RMS được in trong API response)
                    if "rms" in response.headers:
                        rms_value = response.headers["rms"]
                        st.write(f"RMS Value: {rms_value}")

                    # Nút tải ảnh về
                    st.download_button(
                        label="Download Decompressed Image",
                        data=response.content,
                        file_name="rle_decompressed_image.png",
                        mime="image/png",
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
#-----------------------------------------------------------
def jpeg_process():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/jpeg-process/"  # Đảm bảo đường dẫn API là chính xác

    # Tiêu đề ứng dụng
    st.header("JPEG Process")
    st.write("Tải ảnh lên để thực hiện nén và giải nén JPEG.")

    # Widget để tải ảnh
    uploaded_file = st.file_uploader("Tải ảnh lên:", type=["dng", "nef", "cr2", "arw", "orf"])

    # Nút xử lý
    if uploaded_file and st.button("Thực hiện JPEG Process"):
        try:
            # Đọc nội dung file
            file_bytes = uploaded_file.read()
            
            # Tạo payload và gửi request tới API
            #files = {"image": (uploaded_file.name, file_bytes, "image/jpeg")}
            uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
            files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(API_URL, files=files)
            
            if response.status_code == 200:
                # Hiển thị ảnh kết quả
                result_image = Image.open(io.BytesIO(response.content))
                st.image(result_image, caption="Ảnh đã xử lý (JPEG)", use_container_width=True)

                # Nút tải ảnh kết quả
                st.download_button(
                    label="Tải ảnh kết quả",
                    data=response.content,
                    file_name="processed_image.jpg",
                    mime="image/jpeg",
                )
            else:
                st.error(f"Lỗi API: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Lỗi kết nối API: {e}")

#------------------------------------------------
def hamonic():
    # Địa chỉ API
    API_URL = "http://127.0.0.1:8000/contra-harmonic-filter/"  # Đảm bảo URL API chính xác

    # Tiêu đề ứng dụng
    st.header("Contra-Harmonic Mean Filter")
    st.write("Tải ảnh lên và áp dụng bộ lọc trung bình nghịch đảo (Contra-Harmonic Mean Filter).")

    # Widget tải ảnh
    uploaded_file = st.file_uploader("Tải ảnh lên (JPG/PNG):", type=["jpg", "jpeg", "png"])

    

    # Nút thực hiện
    if uploaded_file and st.button("Áp dụng Contra-Harmonic Filter"):
        # Tham số bộ lọc
        size = st.slider("Chọn kích thước bộ lọc (size):", min_value=3, max_value=15, value=3, step=2)
        Q = st.number_input("Nhập giá trị Q (hệ số nghịch đảo):", value=-1.0, step=0.1)
        try:
            # Đọc nội dung file
            file_bytes = uploaded_file.read()
            
            # Tạo payload và gửi request tới API
            #files = {"image": (uploaded_file.name, file_bytes, "image/png")}
            uploaded_file.seek(0)  # Đảm bảo con trỏ file ở đầu
            files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            data = {"size": size, "Q": Q}
            response = requests.post(API_URL, files=files, data=data)
            
            if response.status_code == 200:
                # Hiển thị ảnh kết quả
                result_image = Image.open(io.BytesIO(response.content))
                st.image(result_image, caption="Ảnh đã xử lý (Contra-Harmonic Filter)", use_container_width=True)

                # Nút tải ảnh kết quả
                st.download_button(
                    label="Tải ảnh kết quả",
                    data=response.content,
                    file_name="filtered_image.png",
                    mime="image/png",
                )
            else:
                st.error(f"Lỗi API: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Lỗi kết nối API: {e}")