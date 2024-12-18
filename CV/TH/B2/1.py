import cv2
import numpy as np

# Bước 1: Đọc ảnh và hiển thị ảnh gốc
image = cv2.imread('D:\\PTIT\\CV\\TH\\B2\\ll.jpg')
cv2.imshow('Original Image', image)

# Bước 3: Phân tích từng kênh màu
B, G, R = cv2.split(image)

# Tạo các ảnh mới cho từng kênh với hai kênh còn lại có giá trị bằng 0
zero_channel = np.zeros_like(B)

# Kênh xanh dương (Blue)
Blue_channel = cv2.merge([B, zero_channel, zero_channel])
cv2.imshow('Blue Channel (Blue)', Blue_channel)
cv2.imwrite('D:\\PTIT\\CV\\TH\\B2\\blue_channel.jpg', Blue_channel)  # Lưu ảnh kênh xanh dương

# Kênh xanh lá (Green)
Green_channel = cv2.merge([zero_channel, G, zero_channel])
cv2.imshow('Green Channel (Green)', Green_channel)
cv2.imwrite('D:\\PTIT\\CV\\TH\\B2\\green_channel.jpg', Green_channel)  # Lưu ảnh kênh xanh lá

# Kênh đỏ (Red)
Red_channel = cv2.merge([zero_channel, zero_channel, R])
cv2.imshow('Red Channel (Red)', Red_channel)
cv2.imwrite('D:\\PTIT\\CV\\TH\\B2\\red_channel.jpg', Red_channel)  # Lưu ảnh kênh đỏ

# Bước 4: Tăng hoặc giảm một kênh màu
R_mod = cv2.add(R, 50)

# Bước 5: Gộp các kênh màu lại và hiển thị ảnh đã thay đổi
image_modified = cv2.merge([B, G, R_mod])
cv2.imshow('Modified Image', image_modified)
cv2.imwrite('D:\\PTIT\\CV\\TH\\B2\\modified_image.jpg', image_modified)  # Lưu ảnh đã chỉnh sửa

# Đợi người dùng nhấn phím bất kỳ để đóng tất cả cửa sổ hiển thị
cv2.waitKey(0)
cv2.destroyAllWindows()
