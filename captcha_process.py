#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-07 20:16:06
@LastEditTime: 2019-05-09 20:01:44
'''
import os
from PIL import Image
import my_dataset

def rgb2gray(img):
    img = img.convert('L')
    return img


def binarizing(img):
    threshold = 200
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


def vertical(img):
    """传入二值化后的图片进行垂直投影"""
    pixdata = img.load()
    w,h = img.size
    capt_list = []
    # 开始投影
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x,y] == 0:
                black += 1
        capt_list.append(black)
    # 判断边界
    l,r = 0,0
    flag = False
    boxs = []
    for i,count in enumerate(capt_list):
        # 阈值这里为0
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i-1
            flag = False
            boxs.append((l,r))
    return boxs

def get_sub_img(boxs, bin_img, cnt):
    for subbox in boxs:
        subbox = (subbox[0], 0, subbox[1], 48)
        img = bin_img.crop(subbox)
        width = img.size[0] 
        if width >= 15:
            mid = img.size[0] // 2 + 1
            print('mid = %d' % mid)
            img1 = img.crop((0, 0, mid, 48))
            img1.save(my_dataset.sub_img_dir + str(cnt) + '.png')
            cnt += 1
            img2 = img.crop((mid, 0, width, 48))
            img2.save(my_dataset.sub_img_dir + str(cnt) + '.png')
            cnt += 1
        else:
            img.save(my_dataset.sub_img_dir + str(cnt) + '.png')
            cnt += 1

def capt_process(captcha_dir, train_dir):
    cnt = 1
    files = os.listdir(captcha_dir)
    for file in files:
        captcha_path = captcha_dir + file
        image = Image.open(captcha_path)
        gray_img = rgb2gray(image)
        bin_img = binarizing(gray_img)
        boxs = vertical(bin_img)
        get_sub_img(boxs, bin_img, cnt)
    

if __name__ == '__main__':
    capt_process(my_dataset.captcha_dir, my_dataset.train_dir)