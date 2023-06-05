import os

folder_path = r"D:\project_res"
tot = 0

# 해당 경로의 모든 폴더와 파일을 순회합니다.
for root, dirs, files in os.walk(folder_path):
    file_count = len([file for file in files if file.endswith(".jpg")])
    print(f"{root}: 파일 개수 - {file_count}")
    tot += file_count

print(tot)