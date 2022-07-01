# -*- coding:utf-8 -*-
# author: zhanghay
# Create Time: 2022/7/1  17:51
# File Name: showImgFromJson.py
# Description: 根据json文件画框和点
#              json判断对不对

import cv2 as cv
import numpy as np
import os
import json
import mirror
if __name__ == '__main__':
    file='003_v'
    img = cv.imread(file+'.jpg')
    with open(file+'.json', 'r', encoding='utf8') as js:
        data = json.load(js)
        js.close()
    # 横着是imageWidth
    # 竖着是imageHeight

    for i in range(8):
        point = (int(data['shapes'][i + 1]['points'][0][0]), int(data['shapes'][i + 1]['points'][0][1]))
        cv.circle(img, point, 5, (255, 255, 255), -1)
    # 点  (int(data['shapes'][1]['points'][0][0]),int(data['shapes'][1]['points'][0][1])) # x , y

    bboxPoint1 = (int(data['shapes'][0]['points'][0][0]), int(data['shapes'][0]['points'][0][1]))
    # bbox 左上
    bboxPoint2 = (int(data['shapes'][0]['points'][1][0]), int(data['shapes'][0]['points'][1][1]))
    # bbox 右下
    cv.rectangle(img, bboxPoint1, bboxPoint2, (0, 255, 255), 4)
    cv.imshow('img', img)
    key = cv.waitKey(0)
    if key == "a":
        cv.destroyAllWindows()