import face_recognition
import cv2
x = 10
print('Done!')

image = cv2.imread('images/my_image.jpg')
rgb = cv2.cvtColor(image, cv2.IMREAD_COLOR)
# cv2.imshow('image', cv2.resize(rgb, (1920, 1080)))
cv2.waitKey(0)
boxes = face_recognition.face_locations(rgb)
faceEnc = face_recognition.face_encodings(image,(boxes))
print(faceEnc)
