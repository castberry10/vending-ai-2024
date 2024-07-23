# 랜덤 

"""
this script is imgage processing 
img directory -> get pwd and file 
img pre processing -> save change image

"""

# 가정 -> 
# foreground image 디렉토리가 존재한다.
# background image 디렉토리가 존재한다.
# makelabeling image 디렉토리가 존재한다.
# foreground image와 background image 디렉토리에는 target.txt파일이 있고 그 안에는 이미지 파일들의 이름나열이 있다.
# 원하는 개수만큼 makelabeling image 디렉토리에 이미지 파일이 생성된다.


import cv2
import os
import sys
import numpy as np
import random


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def save_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# foreground_image_path = '/home/aicompetition28/wychoi/testDatasets/3.backsub_images_100/target.txt'
# background_image_path = '/home/aicompetition28/wychoi/testDatasets/3.Background_Images/target.txt'
# makelabeling_image_path = '/home/aicompetition28/colorfilteroneimage'

# foreground_image_list = read_file(foreground_image_path).split('\n')
# background_image_list = read_file(background_image_path).split('\n')

# foreground_image_list_cnt = len(foreground_image_list)
# background_image_list_cnt = len(background_image_list)

for i in range(30000):
    # foreground_image_path = foreground_image_list[random.randint(0, foreground_image_list_cnt - 1)]
    # background_image_path = background_image_list[random.randint(0, background_image_list_cnt - 1)]
    

    ### test code
    foreground_image_path = os.path.join(os.getcwd(), 'data', 'object', 'act_ii_butter_lovers_popcorn_11605.jpg')
    background_image_path = os.path.join(os.getcwd(), 'data', 'background', 'top', '20230823_185335_4.jpg')
    makelabeling_image_path = os.path.join(os.getcwd(), 'data', 'edit_image')
    ### test code


    background_image = cv2.imread(background_image_path)  # background image
    class_image = cv2.imread(foreground_image_path)  # class image

    # class image processing
    color_range = (0, 40)
    random_color_rgb = random.randint(*color_range), random.randint(*color_range), random.randint(*color_range)
    rgb_str = str(random_color_rgb[0]) + '_' + str(random_color_rgb[1]) + '_' + str(random_color_rgb[2])
    red_filter = np.full_like(class_image, random_color_rgb)

    mask = cv2.inRange(class_image, np.array([4, 4, 4]), np.array([255, 255, 255]))
    class_image = cv2.add(class_image, red_filter, mask=mask)
    background_image = cv2.bitwise_and(background_image, background_image, mask=cv2.bitwise_not(mask))
    image = cv2.add(background_image, class_image)

    print(type(image))
    cv2.imshow("image", image)

    # # 이미지 저장
    foreground_image_path_split = foreground_image_path.split(os.sep)
    background_image_path_split = background_image_path.split(os.sep)
    outputfilename = foreground_image_path_split[-1].split('.')[0] + '_' + background_image_path_split[-1].split('.')[0] + '_' + rgb_str + '.jpg'
    makelabeling_image_file_path = os.path.join(makelabeling_image_path, outputfilename)
    cv2.imwrite(makelabeling_image_file_path, image)
    print(f"Image saved to {makelabeling_image_file_path}")

    # 욜로 파일 생성
    content = read_file(foreground_image_path[:-3]+'txt')
    save_file(makelabeling_image_file_path[:-3]+'txt', content)
    print(f"YOLO file saved to {makelabeling_image_file_path[:-3]+'txt'}")

cv2.waitKey(0)
cv2.destroyAllWindows()