"""
fitting image and write result text to csv file
각 카메라별 이미지 결과 도출
도출된 데이터에서 다음 프레임 이미지에 변동된 물품 확인
변동사항 list로 누적
결과 csv 파일로 저장
"""

import os
import cv2
import numpy as np



