#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-04 22:07:01
@LastEditTime: 2019-05-09 21:03:00
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
from PIL import Image

import my_dataset

def init():
    driver = webdriver.Firefox()
    local_time =datetime.datetime.now()
    day_time = str(local_time.year) + '-' + str(local_time.month) + '-' + str(local_time.day + 1)
    login_url = 'http://219.231.8.121/Home/Web/area?area=7&segment=' + '15125' + '&day=' + day_time + '&startTime=07:00&endTime=22:00'
    print(login_url)
    driver.get(login_url)
    time.sleep(2)
    elem_login = driver.find_element_by_class_name('login-btn')
    elem_login.click()
    return driver

def save(driver):
    driver.get_screenshot_as_file(my_dataset.screen_path)
    img = Image.open(my_dataset.screen_path)
    box = (659, 380, 738, 428)
    image = img.crop(box)
    image.save(my_dataset.verify_path)
    #shutdown()

def main():
    driver = init()
    save(driver)           

if __name__ == '__main__':
    main()




