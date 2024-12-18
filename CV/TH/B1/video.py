import cv2

# Đường dẫn video đầu vào và đầu ra
input_video_path = 'D:\\PTIT\\CV\\TH\\B1\\video_input.mp4'
output_video_path = 'D:\\PTIT\\CV\\TH\\B1\\video_output.mp4'

# Đường dẫn đến IP webcam
ip_camera_url = 'http://10.21.204.209:8080/video'

# Mở video và kiểm tra
cap = cv2.VideoCapture(ip_camera_url)
if not cap.isOpened():
    print("Lỗi: Không thể mở video.")
    exit()

# Lấy thông tin video
frame_width, frame_height = int(cap.get(3)), int(cap.get(4))  # 3: width, 4: height
fps = cap.get(cv2.CAP_PROP_FPS)

# Tạo VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()  # Đọc frame
    if not ret:
        break
    cv2.imshow('Video', frame)  # Hiển thị frame
    out.write(frame)  # Ghi frame vào video

    # Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
out.release()
cv2.destroyAllWindows()
