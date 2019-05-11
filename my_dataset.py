#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-09 19:14:40
@LastEditTime: 2019-05-11 15:46:53
'''

import datetime

train_dir = './project/Subscribe/dataset/train/'

test_dir = './project/Subscribe/dataset/test/'

sub_img_dir = './project/Subscribe/sub_img/'

captcha_dir = './project/Subscribe/dataset/images/'

verify_path = './project/Subscribe/img/verify.png'

screen_path = './project/Subscribe/img/screen.png'

model_path = './project/Subscribe/model/model.cy'

def get_login_url():
    local_time =datetime.datetime.now()
    day_time = str(local_time.year) + '-' + str(local_time.month) + '-' + str(local_time.day + 1)
    login_url = 'http://219.231.8.121/Home/Web/area?area=9&segment=' + '17319' + '&day=' + day_time + '&startTime=07:00&endTime=22:00'
    print(login_url)
    return login_url