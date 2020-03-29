import cv2

face_cascade = cv2.CascadeClassifier('/home/thyanmol/College/MOSIP/venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('/home/thyanmol/Downloads/SmallFaces1966.png')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output

print('Number of faces are : ')
print(len(faces))
cv2.imshow('img', img)
cv2.waitKey()