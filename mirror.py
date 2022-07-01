import cv2
import math
import numpy as np
import os
import glob
import json
import shutil


# 翻转图片后保存图片
# h 水平
# v 垂直
# a 水平+垂直
def h_MirrorImg(img_path, img_write_path):
    img = cv2.imread(img_path)
    mirror_img = cv2.flip(img, 1)  # 1 水平翻转， 0 垂直 -1 水平+垂直
    cv2.imwrite(img_write_path, mirror_img)


def v_MirrorImg(img_path, img_write_path):
    img = cv2.imread(img_path)
    mirror_img = cv2.flip(img, 0)  #
    cv2.imwrite(img_write_path, mirror_img)


def a_MirrorImg(img_path, img_write_path):
    img = cv2.imread(img_path)
    mirror_img = cv2.flip(img, -1)  #
    cv2.imwrite(img_write_path, mirror_img)


# 翻转注释
def h_MirrorAnno(anno_path, anno_write_path):
    with open(anno_path, 'r', encoding='utf8') as js:
        data = json.load(js)
        js.close()
    bbox = data['shapes'][0]['points']

    x1 = bbox[0][0]
    x2 = bbox[1][0]
    w = data['imageWidth']

    x1 = w - x1 + 1  # 坐标操作
    x2 = w - x2 + 1

    assert x1 > 0  # 非负数
    assert x2 > 0

    bbox[0][0] = int(x2)
    bbox[1][0] = int(x1)

    for i in range(8):
        point_x = data['shapes'][i + 1]['points'][0][0]
        point_x = w - point_x + 1
        assert point_x > 0
        data['shapes'][i + 1]['points'][0][0] = point_x
        
    with open(anno_write_path, "w") as f:
        json.dump(data, f)
        f.close()


def v_MirrorAnno(anno_path, anno_write_path):
    with open(anno_path, 'r', encoding='utf8') as js:
        data = json.load(js)
        js.close()
    bbox = data['shapes'][0]['points']

    y1 = bbox[0][1]
    y2 = bbox[1][1]
    h = data['imageHeight']

    y1 = h - y1 + 1  # 坐标操作
    y2 = h - y2 + 1

    assert y1 > 0  # 非负数
    assert y2 > 0
    bbox[0][1] = int(y2)
    bbox[1][1] = int(y1)

    for i in range(8):
        point_y = data['shapes'][i + 1]['points'][0][1]
        point_y = h - point_y + 1
        assert point_y > 0
        data['shapes'][i + 1]['points'][0][1] = point_y


    with open(anno_write_path, "w") as f:
        json.dump(data, f)
        f.close()


def a_MirrorAnno(anno_path, anno_write_path):
    with open(anno_path, 'r', encoding='utf8') as js:
        data = json.load(js)
        js.close()
    bbox = data['shapes'][0]['points']

    x1 = bbox[0][0]
    x2 = bbox[1][0]
    y1 = bbox[0][1]
    y2 = bbox[1][1]
    h = data['imageHeight']
    w = data['imageWidth']

    x1 = w - x1 + 1
    x2 = w - x2 + 1

    y1 = h - y1 + 1
    y2 = h - y2 + 1

    assert x1 > 0
    assert x2 > 0
    assert y1 > 0
    assert y2 > 0

    bbox[0][0] = int(x2)
    bbox[1][0] = int(x1)
    bbox[0][1] = int(y2)
    bbox[1][1] = int(y1)

    for i in range(8):

        point_x = data['shapes'][i + 1]['points'][0][0]
        point_x = w - point_x + 1
        assert point_x > 0
        data['shapes'][i + 1]['points'][0][0] = point_x

        point_y = data['shapes'][i + 1]['points'][0][1]
        point_y = h - point_y + 1
        assert point_y > 0
        data['shapes'][i + 1]['points'][0][1] = point_y

    with open(anno_write_path, "w") as f:
        json.dump(data, f)
        f.close()


def mirror(img_dir, anno_dir, img_write_dir, anno_write_dir):
    if not os.path.exists(img_write_dir):
        os.makedirs(img_write_dir)

    if not os.path.exists(anno_write_dir):
        os.makedirs(anno_write_dir)

    img_names = os.listdir(img_dir)
    # 所有图片文件
    for img_name in img_names:
        if img_name.split('.')[-1] == 'jpg' or img_name.split('.')[-1] == 'png':
            img_path = os.path.join(img_dir, img_name)
            # 重命名
            h_img_write_path = os.path.join(img_write_dir, img_name.split('.')[0] + '_h' + '.jpg')
            anno_path = os.path.join(anno_dir, img_name.split('.')[0] + '.json')
            h_anno_write_path = os.path.join(anno_write_dir, img_name.split('.')[0] + '_h' + '.json')
            #
            v_img_write_path = os.path.join(img_write_dir, img_name.split('.')[0] + '_v' + '.jpg')
            v_anno_write_path = os.path.join(anno_write_dir, img_name.split('.')[0] + '_v' + '.json')
            #
            a_img_write_path = os.path.join(img_write_dir, img_name.split('.')[0] + '_a' + '.jpg')
            a_anno_write_path = os.path.join(anno_write_dir, img_name.split('.')[0] + '_a' + '.json')
            #
            h_MirrorImg(img_path, h_img_write_path)
            v_MirrorImg(img_path, v_img_write_path)
            a_MirrorImg(img_path, a_img_write_path)
            h_MirrorAnno(anno_path, h_anno_write_path)
            v_MirrorAnno(anno_path, v_anno_write_path)
            a_MirrorAnno(anno_path, a_anno_write_path)


if __name__ == '__main__':
    img_dir = '.'
    anno_dir = '.'
    img_write_dir = '.'
    anno_write_dir = '.'
    mirror(img_dir, anno_dir, img_write_dir, anno_write_dir)


