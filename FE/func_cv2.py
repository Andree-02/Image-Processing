import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from ImageProcessingCV2 import *
from ImageProcessingCV2 import compress_raw
import io

def display_image_info(image, label):
    """Hiển thị thông tin ảnh: shape, channels, dtype"""
    st.markdown(f"{label} Information:")
    st.write(f"- Shape: {image.shape}")
    st.write(f"- Channels: {image.shape[2] if len(image.shape) > 2 else 1}")
    st.write(f"- Data type: {image.dtype}")
#-------------------------------------

def thresholding_cv2():
    # Giao diện Streamlit
    st.header("Thresholding Image Processing ")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale và chuyển đổi nếu cần
        if len(image.shape) == 3:
    
            # Chuyển ảnh sang Grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            grayscale_image = image

        # Thanh trượt để chọn ngưỡng (threshold)
        thresh_value = st.slider("Select Threshold Value", min_value=0, max_value=255, value=127)

        # Áp dụng Thresholding
        binary_image = thresholding(grayscale_image, thresh_value)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Grayscale Image")
            st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)
        with col2:
            st.header("Binary Image")
            st.image(binary_image, caption=f"Thresholded Image (Threshold: {thresh_value})", use_container_width=True)

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
        

#-----------------------------------------------------------------------------

def negative_processingcv2():
    # Giao diện Streamlit
    st.title("Negative Processing App")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale và hiển thị
        if len(image.shape) == 3:
            st.image(image, caption="Original Image (RGB)", use_container_width=True)
            is_rgb = True
        else:
            st.image(image, caption="Original Image (Grayscale)", use_container_width=True)
            is_rgb = False

        # Áp dụng Negative Processing
        negative_image = negative_processing(image)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Negative Image")
            st.image(negative_image, caption="Negative Processed Image", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(negative_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Negative Image",
            data=byte_im,
            file_name="negative_image.png",
            mime="image/png"
        )
#-----------------------------------------------------------------------------------
def bit_plane_slicing_cv2():
    # Giao diện Streamlit
    st.header("Bit Plane Slicing ")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale và chuyển đổi nếu cần
        if len(image.shape) == 3:
           
            # Chuyển ảnh sang Grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            grayscale_image = image

        # Thanh trượt để chọn bit-plane
        bit_plane = st.slider("Select Bit-Plane (0 to 7)", min_value=0, max_value=7, value=0)

        # Áp dụng Bit Plane Slicing
        bit_plane_image = bit_plane_slicing(grayscale_image, bit_plane)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Grayscale Image")
            st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)
        with col2:
            st.header(f"Bit-Plane {bit_plane} Image")
            st.image(bit_plane_image, caption=f"Bit-Plane {bit_plane} Extracted", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(bit_plane_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Bit-Plane Image",
            data=byte_im,
            file_name=f"bit_plane_{bit_plane}_image.png",
            mime="image/png"
        )

#-------------------------------------------------------------------------------------
def histogram_equalcv2():
    # Giao diện Streamlit
    st.header("Histogram Equalization ")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale và chuyển đổi nếu cần
        if len(image.shape) == 3:
        
            # Chuyển ảnh sang Grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
          
            grayscale_image = image

        # Áp dụng Histogram Equalization
        equalized_image = histogram_equalization(grayscale_image)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)
        with col2:
            st.header("Equalized Image")
            st.image(equalized_image, caption="Histogram Equalized Image", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(equalized_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Equalized Image",
            data=byte_im,
            file_name="equalized_image.png",
            mime="image/png"
        )

#----------------------------------------------------

def histo_matching_cv2():
    # Giao diện Streamlit
    st.header("Histogram Matching ")

    # Tải ảnh nguồn (Source Image) và ảnh tham chiếu (Reference Image)
    uploaded_source = st.file_uploader("Upload the Source Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
    uploaded_reference = st.file_uploader("Upload the Reference Image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_source and uploaded_reference:
        # Đọc ảnh nguồn và ảnh tham chiếu
        source_image = np.array(Image.open(uploaded_source))
        reference_image = np.array(Image.open(uploaded_reference))

        # Kiểm tra xem ảnh là RGB hay Grayscale và hiển thị
        if len(source_image.shape) == 3:
            st.image(source_image, caption="Source Image (RGB)", use_container_width=True)
        else:
            st.image(source_image, caption="Source Image (Grayscale)", use_container_width=True)

        if len(reference_image.shape) == 3:
            st.image(reference_image, caption="Reference Image (RGB)", use_container_width=True)
        else:
            st.image(reference_image, caption="Reference Image (Grayscale)", use_container_width=True)

        # Áp dụng Histogram Matching
        matched_image = histogram_matching(source_image, reference_image)

        # Hiển thị ảnh sau xử lý
        st.header("Matched Image")
        st.image(matched_image, caption="Histogram Matched Image", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(matched_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Matched Image",
            data=byte_im,
            file_name="matched_image.png",
            mime="image/png"
        )
#---------------------------------

def Contra_Harmonic_Mean_Filter_cv2():
    # Giao diện Streamlit
    st.header("Contra-Harmonic Mean Filter")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            # Ảnh Grayscale
            is_rgb = False
        else:
            # Ảnh RGB
            is_rgb = True

        # Thanh trượt để chọn kích thước kernel và tham số Q
        kernel_size = st.slider("Select Kernel Size", min_value=3, max_value=15, step=2, value=3)
        Q = st.slider("Select Q Parameter", min_value=-5.0, max_value=5.0, step=0.1, value=1.0)

        # Áp dụng Contra-Harmonic Mean Filter
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [contra_harmonic_mean_filter(image[:, :, i], kernel_size, Q) for i in range(image.shape[2])]
            filtered_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            filtered_image = contra_harmonic_mean_filter(image, kernel_size, Q)

        # Hiển thị ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            
            with st.container(border=True):
                st.header("Original Image")
                st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            with st.container(border=True):
                st.header("Filtered Image")
                st.image(filtered_image, caption=f"Filtered Image (Kernel Size: {kernel_size}, Q: {Q})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(filtered_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Filtered Image",
            data=byte_im,
            file_name="filtered_image.png",
            mime="image/png"
        )

#------------------------------------

def gaussian_noise_cv2():

    # Giao diện Streamlit
    st.header("Gaussian Noise Addition App")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            is_rgb = False
        else:
            is_rgb = True

        # Thanh trượt để chọn các tham số mean và variance
        mean = st.slider("Select Mean", min_value=0.0, max_value=50.0, step=0.1, value=0.0)
        var = st.slider("Select Variance", min_value=0.0, max_value=1000.0, step=1.0, value=10.0)

        # Áp dụng Gaussian Noise
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [gaussian_noise(image[:, :, i], mean, var) for i in range(image.shape[2])]
            noisy_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            noisy_image = gaussian_noise(image, mean, var)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Noisy Image")
            st.image(noisy_image, caption=f"Noisy Image (Mean: {mean}, Variance: {var})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(noisy_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Noisy Image",
            data=byte_im,
            file_name="noisy_image.png",
            mime="image/png"
        )
        
        
#-------------------------------

def Uniform_Noise_cv2():

    # Giao diện Streamlit
    st.header("Uniform Noise Addition")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            is_rgb = False
            
        else:
            is_rgb = True
    

        # Thanh trượt để chọn các tham số low và high
        low = st.slider("Select Low Value", min_value=-100.0, max_value=0.0, step=1.0, value=-10.0)
        high = st.slider("Select High Value", min_value=0.0, max_value=100.0, step=1.0, value=10.0)

        # Áp dụng Uniform Noise
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [uniform_noise(image[:, :, i], low, high) for i in range(image.shape[2])]
            noisy_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            noisy_image = uniform_noise(image, low, high)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Noisy Image")
            st.image(noisy_image, caption=f"Noisy Image (Low: {low}, High: {high})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(noisy_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Noisy Image",
            data=byte_im,
            file_name="noisy_image.png",
            mime="image/png"
        )

#-----------------------------------------------------------------

def Erosion_cv2():
    # Giao diện Streamlit
    st.header("Erosion Image Processing ")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            is_rgb = False
        else:
            is_rgb = True

        # Thanh trượt để chọn kích thước kernel
        kernel_size = st.slider("Select Kernel Size", min_value=3, max_value=15, step=2, value=3)

        # Áp dụng Erosion
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [erosion(image[:, :, i], kernel_size) for i in range(image.shape[2])]
            eroded_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            eroded_image = erosion(image, kernel_size)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Eroded Image")
            st.image(eroded_image, caption=f"Eroded Image (Kernel Size: {kernel_size}x{kernel_size})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(eroded_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Eroded Image",
            data=byte_im,
            file_name="eroded_image.png",
            mime="image/png"
        )

#--------------------------------------------------------------------------


def Dilation_cv2():
    # Giao diện Streamlit
    st.header("Dilation Image Processing ")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            is_rgb = False
            
        else:
            is_rgb = True
            

        # Thanh trượt để chọn kích thước kernel
        kernel_size = st.slider("Select Kernel Size", min_value=3, max_value=15, step=2, value=3)

        # Áp dụng Dilation
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [dilation(image[:, :, i], kernel_size) for i in range(image.shape[2])]
            dilated_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            dilated_image = dilation(image, kernel_size)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Dilated Image")
            st.image(dilated_image, caption=f"Dilated Image (Kernel Size: {kernel_size}x{kernel_size})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(dilated_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Dilated Image",
            data=byte_im,
            file_name="dilated_image.png",
            mime="image/png"
        )
#-------------------------------------------------------------

def clossing_cv2():

    # Giao diện Streamlit
    st.header("Closing Image Processing")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            is_rgb = False

        else:
            is_rgb = True

        # Thanh trượt để chọn kích thước kernel
        kernel_size = st.slider("Select Kernel Size", min_value=3, max_value=15, step=2, value=3)

        # Áp dụng Closing
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [closing(image[:, :, i], kernel_size) for i in range(image.shape[2])]
            closed_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            closed_image = closing(image, kernel_size)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Closed Image")
            st.image(closed_image, caption=f"Closed Image (Kernel Size: {kernel_size}x{kernel_size})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(closed_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Closed Image",
            data=byte_im,
            file_name="closed_image.png",
            mime="image/png"
        )


#--------------------------------------------

def opening_cv2():
    # Giao diện Streamlit
    st.header("Opening Image Processing ")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 2:
            is_rgb = False
            
        else:
            is_rgb = True

        # Thanh trượt để chọn kích thước kernel
        kernel_size = st.slider("Select Kernel Size", min_value=3, max_value=15, step=2, value=3)

        # Áp dụng Opening
        if is_rgb:
            # Xử lý từng kênh màu cho ảnh RGB
            channels = [opening(image[:, :, i], kernel_size) for i in range(image.shape[2])]
            opened_image = np.stack(channels, axis=2)  # Ghép các kênh lại thành ảnh RGB
        else:
            # Xử lý ảnh Grayscale
            opened_image = opening(image, kernel_size)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Opened Image")
            st.image(opened_image, caption=f"Opened Image (Kernel Size: {kernel_size}x{kernel_size})", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(opened_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Opened Image",
            data=byte_im,
            file_name="opened_image.png",
            mime="image/png"
        )
    
#-----------------------------------------------------
def otsu_cv2():
    # Giao diện Streamlit
    st.header("Otsu's Thresholding")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Kiểm tra xem ảnh là RGB hay Grayscale
        if len(image.shape) == 3:
            
            # Chuyển ảnh sang Grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:

            grayscale_image = image

        # Áp dụng Otsu's Thresholding
        binary_image = otsu_thresholding(grayscale_image)

        # Hiển thị ảnh gốc và ảnh sau xử lý trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)
        with col2:
            st.header("Otsu's Thresholding")
            st.image(binary_image, caption="Binary Image", use_container_width=True)

        # Nút tải về ảnh kết quả
        result_image = Image.fromarray(binary_image)
        buf = BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Binary Image",
            data=byte_im,
            file_name="binary_image.png",
            mime="image/png"
        )
        

#------------------------------------------------------------
def rawcompresscv2():
    # Giao diện Streamlit
    st.header("RAW to JPEG Compression")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["dng", "nef", "cr2", "arw", "orf"])

    if uploaded_file is not None:
        # Đọc ảnh gốc
        image = np.array(Image.open(uploaded_file))

        # Hiển thị ảnh gốc

        # Thanh trượt để chọn chất lượng nén JPEG
        qualityy = st.slider("Select JPEG Quality", min_value=0, max_value=100, value=95)

        # Áp dụng nén ảnh
        compressed_image = compress_raw(image, qualityy)

        # Giải mã ảnh JPEG từ mảng NumPy để hiển thị
        decoded_image = cv2.imdecode(compressed_image, cv2.IMREAD_UNCHANGED)

        # Hiển thị ảnh gốc và ảnh sau khi nén trong 2 cột
        col1, col2 = st.columns(2)
        with col1:
            st.header("Original Image")
            st.image(image, caption="Original Image", use_container_width=True)
        with col2:
            st.header("Compressed Image")
            st.image(decoded_image, caption=f"JPEG Image (Quality: {qualityy})", use_container_width=True)

        # Nút tải về ảnh nén
        buf = BytesIO(compressed_image.tobytes())
        st.download_button(
            label="Download Compressed Image",
            data=buf,
            file_name="compressed_image.jpg",
            mime="image/jpeg"
            
        )