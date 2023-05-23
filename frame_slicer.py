import cv2
import shutil
import os

def save_frames(video_path, output_dir):
    
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
        os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Failed to open video file.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    success, frame = cap.read()
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    frame_num = 0
    while success:
        if frame_num % int(fps / 24) == 0:  # 24프레임으로 잘라서 저장
            frame_path = f"{output_dir}/frame_{frame_num}.jpg"
            cv2.imwrite(frame_path, frame)

        success, frame = cap.read()
        frame_num += 1
    cap.release()
    print(f"Frames saved to {output_dir}.")


if __name__ == '__main__':
    # 동영상 파일 경로 설정
    video_path = '/Users/hsyoon/Downloads/mov/KakaoTalk_Video_2023-05-22-22-30-01.mp4'

    # 이미지 프레임 저장할 디렉토리 경로 설정
    output_dir = '/Users/hsyoon/Downloads/img/'

    # 디렉토리 생성
    os.makedirs(output_dir, exist_ok=True)

    # 동영상 프레임 저장
    save_frames(video_path, output_dir)
