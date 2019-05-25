#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-07 16:22:08
@LastEditTime: 2019-05-25 17:18:04
'''
import os
from PIL import Image
import my_dataset
import captcha_process

class_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def resize(train_path):
    files = os.listdir(train_path)
    for file in files:
        fullpath = os.path.join(train_path, file)
        im = Image.open(fullpath)
        gray_img = captcha_process.rgb2gray(im)
        bin_img = captcha_process.binarizing(gray_img)
        region = bin_img.copy()
        img = Image.new('RGB', (28, 28), (255, 255, 255))
        img.paste(region, (10, -5))
        img.save(fullpath)
        

def resizeall(dir_path):
    for i in range(len(class_name)):
        train_path = dir_path + class_name[i]
        resize(train_path)

            
if __name__ == '__main__':
    resizeall(my_dataset.train_dir)
