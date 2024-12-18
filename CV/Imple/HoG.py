import cv2
import numpy as np
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

# Hàm để hiển thị đặc trưng HoG
def display_hog_features(image):
    # Chuyển đổi ảnh màu sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Tính toán HoG và trực quan hóa các đặc trưng HoG
    hog_features, hog_image = hog(gray_image, orientations=9, pixels_per_cell=(8, 8),
                                  cells_per_block=(2, 2), block_norm='L2-Hys',
                                  visualize=True)

    # Tăng cường độ tương phản của ảnh HoG để hiển thị rõ hơn
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

    # Hiển thị ảnh gốc và ảnh HoG
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Chuyển đổi ảnh màu BGR sang RGB
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(hog_image_rescaled, cmap='gray')  # Hiển thị ảnh HoG bằng cmap gray
    plt.title('HoG Features')

    plt.show()

# Hàm để nhận diện người bằng HoG detector
def detect_people(image_path):
    # Khởi tạo HOG descriptor với SVM đã được huấn luyện sẵn cho việc nhận diện người
    hog_detector = cv2.HOGDescriptor()
    hog_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Đọc ảnh màu để hiển thị kết quả nhận diện
    image_color = cv2.imread(image_path)

    # Phát hiện người trong ảnh
    boxes, weights = hog_detector.detectMultiScale(image_color, winStride=(8, 8))

    # Vẽ các hộp giới hạn (bounding boxes) quanh người được phát hiện
    for (x, y, w, h) in boxes:
        cv2.rectangle(image_color, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị ảnh kết quả với người được phát hiện
    cv2.imshow('Detected People', image_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Hàm để lưu ảnh HoG và ảnh nhận diện người vào file
def save_hog_and_detection(image, image_path):
    # Chuyển đổi ảnh màu sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Tính toán HOG và trực quan hóa các đặc trưng HoG
    hog_features, hog_image = hog(gray_image, orientations=9, pixels_per_cell=(8, 8),
                                  cells_per_block=(2, 2), block_norm='L2-Hys',
                                  visualize=True)

    # Tăng cường độ tương phản của ảnh HoG để hiển thị rõ hơn
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

    # Lưu ảnh HoG
    plt.imsave('hog_features_image.png', hog_image_rescaled, cmap='gray')

    # Nhận diện người và lưu ảnh
    hog_detector = cv2.HOGDescriptor()
    hog_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image_color = cv2.imread(image_path)
    boxes, _ = hog_detector.detectMultiScale(image_color, winStride=(8, 8))

    for (x, y, w, h) in boxes:
        cv2.rectangle(image_color, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Lưu ảnh nhận diện người
    cv2.imwrite('detected_people_image.jpg', image_color)

    print("Đã lưu ảnh HoG và ảnh nhận diện người vào file.")

# Hàm chính cho phép chọn chức năng dựa trên phím nhấn
def main():
    image_path = 'people.jpg'  # Đường dẫn đến ảnh của bạn
    image_color = cv2.imread(image_path)  # Đọc ảnh màu

    if image_color is None:
        print("Không thể mở file ảnh. Vui lòng kiểm tra đường dẫn.")
        return

    print("Chọn chức năng:")
    print("1: Trích xuất và hiển thị HoG")
    print("2: Nhận diện người đi bộ bằng HoG detector")
    print("3: Lưu ảnh HoG và ảnh nhận diện người vào file")
    
    choice = input("Nhấn 1, 2 hoặc 3 để chọn chức năng: ")

    if choice == '1':
        display_hog_features(image_color)  # Sử dụng ảnh màu
    elif choice == '2':
        detect_people(image_path)
    elif choice == '3':
        save_hog_and_detection(image_color, image_path)  # Sử dụng ảnh màu
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Gọi hàm main
if __name__ == '__main__':
    main()
