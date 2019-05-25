#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-08 22:09:14
@LastEditTime: 2019-05-25 18:14:48
'''
import keras
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

import captcha_process
import captcha_train
import my_dataset
import captcha_resize


def process(image):
    gray_img = captcha_process.rgb2gray(image)
    bin_img = captcha_process.binarizing(gray_img)
    boxs = captcha_process.vertical(bin_img)
    cnt = 1
    print(boxs)
    captcha_process.get_sub_img(boxs, bin_img, cnt)

def plot_image_label_predict(captcha, label, predict, idx, num=10):
    figure = plt.gcf()
    figure.set_size_inches(12, 14)
    if num > 20:
        num = 20
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(captcha[idx], cmap='binary')
        title = "label = " + str(predict[idx])
        if len(predict) > 0:
            title += ", predict = " + str(predict[idx])
        ax.set_title(title, fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        idx += 1
    plt.show()

def main():
    model = keras.models.load_model(my_dataset.model_path)
    image = Image.open(my_dataset.verify_path)
    process(image)
    captcha_resize.resize(my_dataset.sub_img_dir)
    x, y = None, None
    for i in range(1, 5):
        fullpath = my_dataset.sub_img_dir + str(i) + '.png'
        x, y = captcha_train.get_capt_and_label(fullpath, i, x, y)
    test_capt, test_label = x, y
    X_Test = test_capt.reshape(4, 784).astype('float32') // 255
    predict = model.predict_classes(X_Test)
    #plot_image_label_predict(test_capt, test_label, predict, 0, 4)
    verify = str(predict[0]) + str(predict[1]) + str(predict[2]) + str(predict[3])
    return verify

if __name__ == '__main__':
    print(main())