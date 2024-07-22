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


file_path = 'example.txt'
new_file_path = 'example_modified.txt'

# # 파일 읽기
# content = read_file(file_path)
# print("Original content:")
# print(content)

# # 수정된 내용 저장
# save_file(new_file_path, content)
# print(f"Modified content saved to {new_file_path}")

path = "img"
image_name = "20230823_185335_4.jpg"
dir_path = os.getcwd()



image_path = os.path.join(dir_path, "AI", "img")
print('image_path',  image_path)

image_list: list = os.listdir(image_path)

print(image_list)


background_image = cv2.imread(os.path.join(image_path, image_list[3]), 1)  # background image
class_image = cv2.imread(os.path.join(image_path, image_list[4]), 1)  # class image

# class image processing
color_range = (0, 40)
red_filter = np.full_like(class_image, (random.randint(*color_range), random.randint(*color_range), random.randint(*color_range)))

mask = cv2.inRange(class_image, np.array([4, 4, 4]), np.array([255, 255, 255]))
class_image = cv2.add(class_image, red_filter, mask=mask)
background_image = cv2.bitwise_and(background_image, background_image, mask=cv2.bitwise_not(mask))
# image = cv2.add(image, cv2.bitwise_or(class_image, class_image, mask=cv2.bitwise_not(mask)))

image = cv2.add(background_image, class_image)

print(type(image))
cv2.imshow("image", image)
# cv2.imshow("test", cv2.bitwise_and(class_image, class_image, mask=mask))

# # 이미지 저장
# output_path = os.path.join(image_path, 'output_image.jpg')
# cv2.imwrite(output_path, image)

cv2.waitKey(0)
cv2.destroyAllWindows()