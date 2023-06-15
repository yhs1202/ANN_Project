import cv2
from multiprocessing import Process, Pipe, Queue
import mediapipe as mp
import time

def camera_process(conn):
    cap = cv2.VideoCapture(0)

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

        while True:
            success, image = cap.read()
            if not success:
                break

            #image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            #image.flags.writeable = False
            #results = hands.process(image)
            image = cv2.flip(image,1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    coordinates = []
                    for landmark in hand_landmarks.landmark:
                        coordinates.extend([landmark.x, landmark.y, landmark.z])
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    conn.send(coordinates)

            cv2.imshow('Camera', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def bridge_process(conn,que):
    last_time = time.time()
    while True:
        coordinates = conn.recv()
        current_time = time.time()
        elapsed_time = current_time - last_time

        if elapsed_time >=1.0:
            que.put(coordinates)
            last_time = current_time
            #print("Put coordinates:", coordinates)

def pred_process(que):
    while True:
        coordinates = que.get()
        print("Recieved coord : ", coordinates)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    queue = Queue()

    p1 = Process(target=camera_process, args=(parent_conn,))
    p1.start()

    p2 = Process(target=bridge_process, args=(child_conn,queue))
    p2.start()

    p3 = Process(target=pred_process, args=(queue,))
    p3.start()

    p1.join()
    p2.join()
    p3.join()