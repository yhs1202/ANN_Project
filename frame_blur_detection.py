import cv2
import numpy
import numpy as np
import os

def estimate_blur(image, threshold=100):
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur_map = cv2.Laplacian(image, cv2.CV_64F)
    score = np.var(blur_map)
    return score

def calculate_blur_scores(directory):
    blur_scores = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(directory, filename)
            image = cv2.imread(image_path)
            if image is not None:
                blur_score = estimate_blur(image)
                blur_scores.append(blur_score)

    return blur_scores

# 이미지 파일이 저장된 디렉토리 경로 설정
image_directory = './NIA_SL_FS0001_CROWD18_F/res'

# 블러 점수 계산
blur_scores = calculate_blur_scores(image_directory)

# 10*n 배열로 출력
n = len(blur_scores)
k = n%60
r = 60-k
output_array = np.array(blur_scores)
if r > 0:
    zeros = np.zeros(r)
    output_array = np.concatenate((output_array, zeros), axis=0)

print(len(output_array))
output_array = np.reshape(output_array, (int(len(output_array)/60),60))

print(output_array)
