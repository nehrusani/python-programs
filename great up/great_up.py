import cv2

# SystemExit is a built-in exception raised to stop the program and return an
# exit code. Raising SystemExit terminates execution unless the exception is
# caught by an except block (it's what sys.exit() raises internally).

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit('Cannot open webcam')

ret, frame = cap.read()
cap.release()
if not ret:
    raise SystemExit('Failed to capture image')

cv2.imwrite('foto.jpg', frame)
print('Saved foto.jpg')
