import os
import cv2
import mediapipe as mp
import numpy as np


def extract_hand_landmarks(image_path):
    # 이미지 불러오기
    image = cv2.imread(image_path)

    # MediaPipe를 사용하여 손 부분의 관절 추출
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1) # 손 하나만 인식
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # 추출한 관절 데이터를 배열로 변환
    landmarks = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 손목 좌표 가져오기
            wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
            wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
            wrist_z = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z

            for landmark in hand_landmarks.landmark:
                # 손목을 기준으로 상대 좌표 계산
                relative_x = landmark.x - wrist_x
                relative_y = landmark.y - wrist_y
                relative_z = landmark.z - wrist_z

                landmarks.append(relative_x)
                landmarks.append(relative_y)
                landmarks.append(relative_z)
    else:
        print(image_path, ": None Landmark")
        return None

    return landmarks


def process_images_in_folder(folder_path):
    # 폴더 내의 이미지 파일들을 순회하며 관절 데이터 추출
    all_landmarks = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
            image_path = os.path.join(folder_path, filename)
            landmarks = extract_hand_landmarks(image_path)
            if landmarks is not None:
                all_landmarks.append(landmarks)

    # 추출한 관절 데이터를 배열로 변환하고 CSV 파일에 연결
    data_array = np.array(all_landmarks)
    csv_path = os.path.join(folder_path, folder_path + "_hand_landmarks.csv")

    if os.path.exists(csv_path):
        # 이미 CSV 파일이 존재하면 기존 파일에 데이터를 추가
        existing_data = np.genfromtxt(csv_path, delimiter=",", skip_header=1)
        combined_data = np.concatenate((existing_data, data_array), axis=0)
        # header = "x_0,y_0,z_0,x_1,y_1,z_1,...,x_20,y_20,z_20"  # 열 이름을 적절히 수정해주세요
        np.savetxt(csv_path, combined_data, delimiter=",", comments="")
    else:
        # CSV 파일이 존재하지 않으면 새로 파일을 생성
        # header = "x_0,y_0,z_0,x_1,y_1,z_1,...,x_20,y_20,z_20"  # 열 이름을 적절히 수정해주세요
        np.savetxt(csv_path, data_array, delimiter=",", comments="")

    print("손 부분 관절 데이터가 성공적으로 저장되었습니다.")


if __name__ == '__main__':    
    # folder_path = "/Users/hsyoon/Downloads/img/"
    # process_images_in_folder(folder_path)
    # path = '/Users/hsyoon/Downloads/img/hand_landmarks.csv'
    # csv = np.loadtxt(path, delimiter=",")
    # print(csv.shape)


    dataset_dir = '/Users/hsyoon/Downloads/dataset2/'
    print(os.listdir(dataset_dir))
    for dir in os.listdir(dataset_dir):
        path = os.path.join(dataset_dir, dir)
        print(path)
        process_images_in_folder(path)
