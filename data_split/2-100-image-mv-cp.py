#!/usr/bin/env python3
import os
import shutil

# 원본 데이터 경로
source_dir = "/home/aicompetition28/wychoi/testDatasets/3.backsub_images_100"

# 이미지와 라벨 파일을 저장할 목적지 디렉토리
train_images_dir = "/home/aicompetition28/wychoi/yolo7Datasets/images/train"
train_labels_dir = "/home/aicompetition28/wychoi/yolo7Datasets/labels/train"

# 목적지 디렉토리가 존재하지 않으면 생성
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)

# 클래스 디렉토리 목록을 가져오기
class_dirs = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]

for class_dir in class_dirs:
    class_path = os.path.join(source_dir, class_dir)

    # 파일 목록 가져오기
    files = os.listdir(class_path)
    for file_name in files:
        src_file_path = os.path.join(class_path, file_name)

        if file_name.endswith(".jpg"):
            dst_file_path = os.path.join(train_images_dir, file_name)
        elif file_name.endswith(".txt"):
            dst_file_path = os.path.join(train_labels_dir, file_name)
        else:
            continue  # .jpg 또는 .txt 파일이 아니면 무시
        
        # 파일 복사
        shutil.copy2(src_file_path, dst_file_path)
print("파일 복사가 완료되었습니다.")     
