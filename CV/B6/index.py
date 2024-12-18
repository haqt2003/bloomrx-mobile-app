import cv2
import os

cap = cv2.VideoCapture(0)
img_counter = 0
img_counterNB =0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break   
    cv2.imshow('Video', frame)
    key = cv2.waitKey(25) & 0xFF 
    if key == ord('1'):
        img_name = f"CVF21B21DCPT007HC{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        img_counter += 1
    elif key == ord('2'):
        img_name=f"CVF21B21DCPT007HN{img_counterNB}.jpg"
        cv2.imwrite(img_name, frame)
        img_counterNB +=1
    elif key == ord('e'):
        break
cap.release()
cv2.destroyAllWindows()