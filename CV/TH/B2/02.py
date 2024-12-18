import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('ll.jpg')


# Thay đổi độ tương phản
contrast = 3  # Hệ số tương phản
contrast_image = cv2.multiply(image, np.array([contrast]))

# Hiển thị ảnh
cv2.imshow('Contrast Adjusted Image', contrast_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Thay đổi độ sáng
brightness = 100  # Giá trị cộng vào
bright_image = cv2.add(image, (brightness, brightness, brightness, 0))

# Hiển thị ảnh
cv2.imshow('Brightened Image', bright_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Chuyển sang ảnh xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Hiển thị ảnh
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Thay đổi màu sắc cho một vùng
image[100:200, 100:200] = [0, 255, 0]  # Thay đổi thành màu xanh lá cây

# Hiển thị ảnh
cv2.imshow('Color Changed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Thay đổi độ trong suốt
alpha = 0.1  # Hệ số trong suốt
overlay = image.copy()
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Hiển thị ảnh
cv2.imshow('Blended Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


