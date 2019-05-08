#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-07 19:57:06
@LastEditTime: 2019-05-08 23:19:27
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as matimg
from PIL import Image
import os
from keras.utils import np_utils
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

class_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
train_dir = './project/Subscribe/dataset/train/'
test_dir = './project/Subscribe/dataset/test/'

def load_data(dir_path):
    x, y = None, None
    for i in range(len(class_name)):
        train_path = dir_path + class_name[i]
        files = os.listdir(train_path)
        for file in files:
            fullpath = os.path.join(train_path, file)
            im = Image.open(fullpath)
            #print(fullpath)
            im = im.convert('L')
            im = Image.fromarray(np.uint8(im))
            im = np.array(im)
            im = (np.expand_dims(im, 0))

            if x is None:
                x = im
            else:
                x = np.vstack((x, im))
            if y is None:
                y = i
            else:
                y = np.vstack((y, i))
    return x, y

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

if __name__ == '__main__':
    epoch = 10
    print('start loading data')
    

    x_train_capt, y_train_label = load_data(train_dir)
    X_Train = x_train_capt.reshape(3839, 784).astype('float32')
    X_Train_normalize = X_Train // 255

    x_test_capt, y_test_label = load_data(test_dir)
    X_Test = x_test_capt.reshape(1495, 784).astype('float32')
    X_Test_normalize = X_Test // 255

    Y_Train_OneHot = np_utils.to_categorical(y_train_label)
    Y_Test_OneHot = np_utils.to_categorical(y_test_label)

    print('start building model')
    model = Sequential()
    model.add(Dense(
        units=1024,
        input_dim=784,
        kernel_initializer='normal',
        activation='relu'
    ))

    #model.add(Dropout(0.5))

    model.add(Dense(
        units=10,
        kernel_initializer='normal',
        activation='softmax'
    ))
    print(model.summary())
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    print('strat training')
    train_history = model.fit(X_Train_normalize, Y_Train_OneHot, epochs=epoch, shuffle=True)

    print('get accuracy')
    test_loss, test_acc = model.evaluate(X_Test_normalize, Y_Test_OneHot)
    print('Test Loss: ', test_loss)
    print('Test Accuracy: ', test_acc)
    model.save('./project/Subscribe/model.cy')
