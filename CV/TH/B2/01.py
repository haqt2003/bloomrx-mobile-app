import cv2

# Đọc ảnh
image = cv2.imread('ll.jpg')

# Chuyển đổi không gian màu
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Tách các mặt phẳng màu
h, s, v = cv2.split(image_hsv)
l, a, b = cv2.split(image_lab)

# Hiển thị ảnh gốc
cv2.imshow('Original Image', image)

# Hiển thị các mặt phẳng màu HSV
cv2.imshow('Hue Channel (HSV)', h)
cv2.imshow('Saturation Channel (HSV)', s)
cv2.imshow('Value Channel (HSV)', v)

# Hiển thị các mặt phẳng màu LAB
cv2.imshow('Lightness Channel (LAB)', l)
cv2.imshow('A Channel (LAB)', a)
cv2.imshow('B Channel (LAB)', b)

# Đợi phím bấm để đóng các cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()
