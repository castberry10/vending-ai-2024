# fitting image and write result text to csv file

# 각 카메라별 이미지 결과 도출
# 도출된 데이터에서 다음 프레임 이미지에 변동된 물품 확인
# 변동사항 list로 누적
# 결과 csv 파일로 저장
# ├── cam0
# │   ├── testset_event_10001_0.jpg

# 1. 아무 camN 들어가서 사진 총 개수 구하기 <- 차피 다른 cam들도 사진 개수 같을 듯
# 2. 사진 개수 구하면 


import os
import cv2
import numpy as np
import re
import csv

import subprocess


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def save_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def compare_sets(set1, set2)->tuple[str, str]:
    # set1에 없고 set2에 있는 요소들 -> 추가된 요소들
    added = set2 - set1
    
    # set1에 있고 set2에 없는 요소들 -> 삭제된 요소들
    removed = set1 - set2

    # 한개의 요소만
    for i in added:
        added = i
        break
    
    for i in removed:
        removed = i
        break

    return added, removed


MODEL_PATH = "./yolov3.weights"
MODEL_CFG = "./cfg/yolov3.cfg"
CSV_PATH = "./ai_result/result.csv"

vending_result_csv = []
# [
#     ["1", "판매", "nature_vally_fruit_and_nut"],
#     ["2", "반환", "nature_vally_fruit_and_nut"],
# ]

#
# vending_result_csv_file_path = 
testimg_path = "/home/aicompetition28/testset"
frame_cnt = len(os.listdir(testimg_path+"/cam0"))

# testimg_path = "/home/aicompetition28/testset"

before_img_object_set = set()
for i in range(frame_cnt):
    event_img_object_set = set()
    event_img_object_set_list = list()
    for camcnt in range(5):
        result = subprocess.run(["./darknet", "detect", MODEL_CFG, MODEL_PATH, f"{testimg_path}/cam{camcnt}/testset_event_{10001+i}_{camcnt}.jpg"], capture_output=True, text=True)
        image_result_stdout = result.stdout
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

                # 여기에 다 모여있음
                event_img_object_set.add(object_name)
                event_img_object_set_list.append(object_name)
    
    if frame_cnt == 0:
        before_img_object_set = event_img_object_set
    
    
    else:
        dump_list = [i]
        add, remove = compare_sets(before_img_object_set, event_img_object_set)
        
        if add:
            dump_list.extend("반환", add)
        else:
            dump_list.extend("판매", remove)
        
        vending_result_csv.append(dump_list)
        
        before_img_object_set = event_img_object_set    
        event_img_object_set = set()
    


##########################
# get testset image path #
##########################


#############
# fit image #
#############
# TODO: 카메라별 이미지 도출 반복문 필요



# run의 stdout값은 result.stdout에 저장
# image_result_stdout = result.stdout.split("\n")


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
csvdata = """
"""
csvdata += "Event No., 판매/반환, Item\n"
for i in vending_result_csv:
    csvdata += ", ".join(i)
    csvdata +="\n"

save_file(CSV_PATH, csvdata)


