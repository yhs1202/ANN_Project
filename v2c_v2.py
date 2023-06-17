import cv2
import mediapipe as mp
from keras.models import load_model
import time
import numpy as np

model = load_model('trained_Drop(0.5)_NM_model.h5')

def process_frames():
    cap = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    start_time = time.time()
    prediction_interval = 1.0  # 예측 간격 (1초)

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

        while True:
            success, image = cap.read()
            if not success:
                break

            image = cv2.flip(image, 1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    coordinates = []
                    for landmark in hand_landmarks.landmark:
                        coordinates.extend([landmark.x - hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,
                                            landmark.y - hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,
                                            landmark.z - hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z])
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    elapsed_time = time.time() - start_time
                    if elapsed_time >= prediction_interval:
                        pred = model.predict([coordinates])

                        ans = np.max(pred)
                        ans_arg = np.argmax(ans)

                        #threshold
                        if(ans >= 0.7):
                            #print('pred',ans, ans_arg)
                            print(pred)

                        start_time = time.time()

            cv2.imshow('Camera', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    process_frames()
