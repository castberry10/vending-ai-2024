import os
import shutil
import random

# 원본 데이터 경로
source_dir = "/home/aicompetition28/wychoi/testDatasets/1.competition_trainset/1_dataset"

# 목적지 디렉토리 경로
train_images_dir = "/home/aicompetition28/wychoi/yolo7Datasets/images/train"
val_images_dir = "/home/aicompetition28/wychoi/yolo7Datasets/images/val"
train_labels_dir = "/home/aicompetition28/wychoi/yolo7Datasets/labels/train"
val_labels_dir = "/home/aicompetition28/wychoi/yolo7Datasets/labels/val"

# 목적지 디렉토리가 존재하지 않으면 생성
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 파일 목록 가져오기
files = os.listdir(source_dir)

# 이미지 파일과 라벨 파일을 분리
image_files = [f for f in files if f.endswith(".jpg")]
label_files = [f for f in files if f.endswith(".txt")]

# 파일 목록을 셔플
combined_files = list(zip(image_files, label_files))
random.shuffle(combined_files)

# 학습 데이터와 검증 데이터로 나누기
train_split = int(len(combined_files) * 0.65)
train_files = combined_files[:train_split]
val_files = combined_files[train_split:]

# 파일 복사 함수
def copy_files(file_pairs, dest_images_dir, dest_labels_dir):
    for image_file, label_file in file_pairs:
        shutil.copy2(os.path.join(source_dir, image_file), dest_images_dir)
        shutil.copy2(os.path.join(source_dir, label_file), dest_labels_dir)

# 파일 복사
copy_files(train_files, train_images_dir, train_labels_dir)
copy_files(val_files, val_images_dir, val_labels_dir)

print("파일 복사가 완료되었습니다.")
