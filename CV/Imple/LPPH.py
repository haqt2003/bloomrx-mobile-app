import cv2
import numpy as np
import matplotlib.pyplot as plt

# Hàm tạo bộ lọc Gabor
def build_gabor_filter(ksize, sigma, theta, lambd, gamma, psi):
    return cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)

# Đọc ảnh với OpenCV
image = cv2.imread('people.jpg', cv2.IMREAD_GRAYSCALE)

# Các tham số của bộ lọc Gabor
ksize = 31  # Kích thước bộ lọc Gabor
sigma = 4.0  # Độ lệch chuẩn của bộ lọc
theta = np.pi / 4  # Hướng của bộ lọc
lambd = 10.0  # Bước sóng của hàm cosinus
gamma = 0.5  # Tỉ lệ không gian (tỉ lệ phương vị)
psi = 0  # Pha của hàm cosinus

# Tạo bộ lọc Gabor
gabor_filter = build_gabor_filter(ksize, sigma, theta, lambd, gamma, psi)

# Áp dụng bộ lọc Gabor vào ảnh
filtered_image = cv2.filter2D(image, cv2.CV_8UC3, gabor_filter)

# Hiển thị ảnh sau khi áp dụng bộ lọc Gabor
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Gabor Filtered Image')

plt.show()
