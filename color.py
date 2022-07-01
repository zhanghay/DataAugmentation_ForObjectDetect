import cv2
import math
import numpy as np
import os
import glob
import json
import shutil


def getColorImg(alpha, beta, img_path, img_write_path):
    img = cv2.imread(img_path)
    colored_img = np.uint8(np.clip((alpha * img + beta), 0, 255))
    cv2.imwrite(img_write_path, colored_img)


def getColorAnno(anno_path, anno_write_path):
    shutil.copy(anno_path,anno_write_path)

def color(alpha, beta, img_dir, anno_dir, img_write_dir, anno_write_dir):
    if not os.path.exists(img_write_dir):
        os.makedirs(img_write_dir)

    if not os.path.exists(anno_write_dir):
        os.makedirs(anno_write_dir)
    img_names = os.listdir(img_dir)
    for img_name in img_names:
        img_path = os.path.join(img_dir, img_name)
        img_write_path = os.path.join(img_write_dir, img_name.split('.')[0] + '_color' + str(int(alpha * 10)) + '.jpg')
        #
        anno_path = os.path.join(anno_dir, img_name.split('.')[0] + '.json')
        anno_write_path = os.path.join(anno_write_dir, img_name.split('.')[0] + '_color' + str(int(alpha * 10)) + '.json')
        #
        getColorImg(alpha, beta, img_path, img_write_path)
        getColorAnno(anno_path, anno_write_path)
        # 标注文件并没有变，只是换了个地方


alphas = [0.3, 0.5, 1.2, 1.6]
beta = 10
img_dir = '.'
anno_dir = '.'
img_write_dir = '.'
anno_write_dir = '.'
for alpha in alphas:
    color(alpha, beta, img_dir, anno_dir, img_write_dir, anno_write_dir)
