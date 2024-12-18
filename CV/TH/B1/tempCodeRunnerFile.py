import cv2

# Ảnh tĩnh
image = cv2.imread('D:\\PTIT\\CV\\TH\\B1\\anh1.jpg') # Đọc ảnh
cv2.imshow('Anh', image) # Hiển thị ảnh
cv2.imwrite('D:\\PTIT\\CV\\TH\\B1\\anh_sau_ghi.jpg', image) # Ghi ảnh
cv2.waitKey(0) 
cv2.destroyAllWindows()