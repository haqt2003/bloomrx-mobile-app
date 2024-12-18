import cv2
import matplotlib.pyplot as plt

# Hàm để phát hiện khuôn mặt
def detect_faces(image_path):
    # Tải mô hình Haar Cascade cho khuôn mặt
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Đọc ảnh
    image = cv2.imread(image_path)

    # Chuyển đổi ảnh sang xám để xử lý
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt trong ảnh
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Vẽ hộp giới hạn quanh khuôn mặt được phát hiện
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image, faces

# Hàm để hiển thị ảnh và hộp giới hạn
def display_image_with_faces(image, faces):
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f'Detected Faces: {len(faces)}')
    plt.axis('off')
    plt.show()

# Hàm để lưu ảnh có hộp giới hạn
def save_detected_faces_image(image, output_path):
    cv2.imwrite(output_path, image)
    print(f'Image saved as {output_path}')

# Hàm chính cho phép chọn chức năng dựa trên phím nhấn
def main():
    image_path = 'people.jpg'  # Đường dẫn đến ảnh của bạn
    output_path = 'detected_faces_image.jpg'  # Đường dẫn để lưu ảnh đã xử lý

    # Phát hiện khuôn mặt
    detected_image, faces = detect_faces(image_path)

    # Hiển thị ảnh có khuôn mặt được phát hiện
    display_image_with_faces(detected_image, faces)

    # Lưu ảnh với khuôn mặt được phát hiện
    save_detected_faces_image(detected_image, output_path)

# Gọi hàm main
if __name__ == '__main__':
    main()
