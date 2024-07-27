import os
import cv2
import numpy as np
import re
import csv
import copy
import subprocess
DATA_PATH = "./yolov3.data"
MODEL_PATH = "./backup/yolov3_last.weights"
MODEL_CFG = "./cfg/yolov3.cfg"
CSV_PATH = "./ai_result/result.csv"
testimg_path = "/home/aicompetition28/Datasets/4.testset_sample"
frame_cnt = len(os.listdir(testimg_path+"/cam0"))
result = subprocess.run(["./darknet", "detector", "test", DATA_PATH, MODEL_CFG, MODEL_PATH, f"{testimg_path}/cam{0}/testset_event_{10001}_{0}.jpg", "-dont_show"], capture_output=True, text=True)
image_result_stdout = result.stdout
print(image_result_stdout)