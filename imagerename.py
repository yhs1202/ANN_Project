import os

folder_path = r"C:\test\result_img"

# 해당 경로의 모든 폴더와 파일을 순회합니다.
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        print(files)
        if file_name.endswith(".jpg"):
            # 파일 이름과 확장자를 분리합니다.
            base_name, extension = os.path.splitext(file_name)

            # 상위 폴더의 이름을 가져옵니다.
            parent_folder = os.path.basename(root)

            # 새로운 파일 이름을 생성합니다.
            new_file_name = f"{parent_folder}_{base_name}{extension}"

            # 파일의 이전 경로와 새로운 경로를 생성합니다.
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)

            # 파일 이름을 변경합니다.
            os.rename(old_file_path, new_file_path)

            print(f"파일 이름 변경: {file_name} -> {new_file_name}")
