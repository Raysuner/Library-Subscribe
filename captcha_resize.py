#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-07 16:22:08
@LastEditTime: 2019-05-07 20:32:54
'''
import os
from PIL import Image

class_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def load_data(dir_path):
    for i in range(len(class_name)):
        train_path = dir_path + class_name[i]
        files = os.listdir(train_path)
        for file in files:
            fullpath = os.path.join(train_path, file)
            print(fullpath)
            im = Image.open(fullpath)
            im = im.resize((8, 48))
            region = im.copy()
            gray_img = Image.new('RGB', (28, 28), (255, 255, 255))
            gray_img.paste(region, (10, -5))
            gray_img.save(fullpath)

            
if __name__ == '__main__':
    train_dir = './project/Subscribe/dataset/train/'
    test_dir = './project/Subscribe/dataset/test/'
    load_data(train_dir)
    load_data(test_dir)