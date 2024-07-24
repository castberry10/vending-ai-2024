# fitting image and write result text to csv file

# 각 카메라별 이미지 결과 도출
# 도출된 데이터에서 다음 프레임 이미지에 변동된 물품 확인
# 변동사항 list로 누적
# 결과 csv 파일로 저장
# ├── cam0
# │   ├── testset_event_10001_0.jpg

import os
import cv2
import numpy as np
import re

import subprocess


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def save_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


MODEL_PATH = "yolov3.weights"
MODEL_CFG = "cfg/yolov3.cfg"

vending_result_csv = ""
vending_result_csv_file_path = "./ai_result/result.csv"
testimg_path = "/home/aicompetition28/testset"


##########################
# get testset image path #
##########################
# test_file_paths = {cam0: [img_1.jpg, img_2.jpg, img_3.jpg], cam1: [...], cam2: [...], ...}
# test_file_paths = {}
subfolders: list = [f.name for f in os.scandir(testimg_path) if f.is_dir()]

#############
# fit image #
#############
# TODO: 카메라별 이미지 도출 반복문 필요

## test code
# result = subprocess.run(["./darknet", "detect", "cfg/yolov3.cfg", "yolov3.weights", "data/dog.jpg"], capture_output=True, text=True)
cnt = 10001
for folder_name in subfolders:
    result = subprocess.run(["./darknet", "detect", MODEL_CFG, MODEL_PATH, f"{folder_name}/testset_event_{cnt}_{folder_name[:-1]}.jpg"], capture_output=True, text=True)
    if result == 0:
        print(f"run command: {folder_name} image fit successes")
    else:
        print("false")

# run의 stdout값은 result.stdout에 저장
image_result_stdout = result.stdout.split("\n")


############## 
# local test #
##############

# image_result_stdout = """
# honey_bunches_of_oats_with_almonds: 34% (left_x:  277   top_y:   -1   width:  196   height:  191)
# quaker_big_chewy_chocolate_chip: 32%    (left_x:  354   top_y:  145   width:  132   height:   96)
# chewy_dips_chocolate_chip: 30%  (left_x:  354   top_y:  145   width:  132   height:   96)
# """
# image_result_stdout = image_result_stdout.split("\n")


###################
# get object info #
###################
# 정규 표현식을 사용하여 객체 이름과 각 값을 추출
for i in range(1):
    for text in image_result_stdout:
        if "%" in text: # 물체탐지가 된 경우
            object_match = re.match(r'(\w+):', text)
            coords_match = re.findall(r'(\w+):\s*(-?\d+)', text)

            # 객체 이름과 좌표 및 크기 값을 딕셔너리에 저장
            if object_match:
                object_name = object_match.group(1)
            else:
                object_name = None

            variables = {key: int(value) for key, value in coords_match}

            # 결과 출력
            print("Object name:", object_name)
            print("Coordinates and dimensions:", variables)

            # 개별 변수로 사용
            left_x = variables.get('left_x')
            top_y = variables.get('top_y')
            width = variables.get('width')
            height = variables.get('height')

            print(f"left_x = {left_x}, top_y = {top_y}, width = {width}, height = {height}")


########################
# split object for cam #
########################
# cam0 - left
# cam1 - top
# cam2 - right
# cam3 - 




#########################
# get add - loss object #
#########################



######################
# save change object #
######################

save_file(vending_result_csv_file_path, vending_result_csv)


