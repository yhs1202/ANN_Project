import shutil
import os

#source_path = "C:/Users/HELLO WORLD/Downloads/수어 영상/1.Training/[라벨]01_crowd_morpheme/morpheme/01"
#destination_path = "C:/Users/HELLO WORLD/Downloads/수어 영상/1.Training/label"

source_path = "C:/Users/HELLO WORLD/Downloads/수어 영상/1.Training/[원천]01_crowd_video/01_crowd_video/01"
destination_path = "C:/Users/HELLO WORLD/Downloads/수어 영상/1.Training/video"

for root, dirs, files in os.walk(source_path):
    for file_name in files:
        if "1_C" in file_name:
            file_path = os.path.join(root, file_name)  # 파일 경로
            destination_file = os.path.join(destination_path, file_name)  # 목적지 파일 경로
            shutil.copyfile(file_path, destination_file)  # 파일 복사

print("복사가 완료되었습니다.")
