import cv2
import numpy as np
from skimage.exposure import match_histograms
from scipy.ndimage import convolve

def thresholding(image, thresh):
    _, binary_image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
    return binary_image

def negative_processing(image):
    return 255 - image


# Hàm xử lý ảnh Negative Processing
'''def negative_processing(image):
    if len(image.shape) == 3:  # Nếu ảnh là ảnh màu (3 kênh)
        negative_image = cv2.bitwise_not(image)
    else:  # Nếu ảnh là ảnh grayscale (1 kênh)
        negative_image = 255 - image
    return negative_image'''




def bit_plane_slicing(image, bit):
    return ((image >> bit) & 1) * 255

def histogram_equalization(image):
    return cv2.equalizeHist(image)

def histogram_matching(source, reference):
    return match_histograms(source, reference, channel_axis=-1).astype(np.uint8)

def contra_harmonic_mean_filter(image, kernel_size, Q):
    kernel = np.ones((kernel_size, kernel_size))
    numerator = convolve(image.astype(np.float64)**(Q + 1), kernel)
    denominator = convolve(image.astype(np.float64)**Q, kernel)
    with np.errstate(divide='ignore', invalid='ignore'):
        result = numerator / denominator
        result[np.isnan(result)] = 0
    return np.clip(result, 0, 255).astype(np.uint8)

def gaussian_noise(image, mean, var):
    noise = np.random.normal(mean, np.sqrt(var), image.shape)
    noisy_image = image + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# 14. Uniform Noise
def uniform_noise(image, low, high):
    noise = np.random.uniform(low, high, image.shape)
    noisy_image = image + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def erosion(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


def dilation(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


def closing(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

def opening(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def otsu_thresholding(image):
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary_image

def compress_raw(image_array, quality=95):
    # Step 1: Encode the image to JPEG format using OpenCV
    success, encoded_image = cv2.imencode('.jpg', image_array, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    if not success:
        raise ValueError("Failed to encode image to JPEG format.")

    # Step 2: Convert the encoded image to a NumPy array
    compressed_image = np.frombuffer(encoded_image, dtype=np.uint8)

    return compressed_image