import cv2
import mediapipe as mp
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def fingers_up(lm):
    # Landmark numbers:
    # Index tip = 8
    # Middle tip = 12
    # Compare each tip with its lower joint (PIP)
    index_up = lm[8].y < lm[6].y
    middle_up = lm[12].y < lm[10].y
    return index_up and middle_up

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]

        h, w, c = frame.shape
        lm_list = []
        for id, lm in enumerate(hand.landmark):
            lm_list.append(lm)

        # Check gesture (index + middle finger up)
        if fingers_up(lm_list):
            gesture = "Delete Photo"
        else:
            gesture = "Save Photo"

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        cv2.putText(frame, gesture, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    # Press SPACE to take action
    if key == 32:
        ret, photo = cap.read()
        if fingers_up(lm_list):
            # Delete photo → do nothing
            print("Gesture: delete → photo NOT saved")
        else:
            cv2.imwrite("photo.jpg", photo)
            print("Gesture: save → photo saved")

    # ESC to quit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()