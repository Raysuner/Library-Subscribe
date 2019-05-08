#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-08 22:09:14
@LastEditTime: 2019-05-08 22:55:04
'''
import keras
import captcha_train

model_path = './project/Subscribe/model.cy'
model = keras.models.load_model(model_path)
test_capt, test_label = captcha_train.load_data(captcha_train.test_dir)
X_Test = test_capt.reshape(1495, 784).astype('float32')
predict = model.predict_classes(X_Test)
captcha_train.plot_image_label_predict(test_capt, test_label, predict, idx=450)
