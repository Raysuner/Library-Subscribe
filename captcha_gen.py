#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-04 22:07:01
@LastEditTime: 2019-05-11 16:38:42
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
from PIL import Image

import my_dataset

def init():
    driver = webdriver.Firefox()
    driver.set_window_size(960, 1080)
    login_url = my_dataset.get_login_url()
    print(login_url)
    driver.get(login_url)
    time.sleep(2)
    elem_login = driver.find_element_by_class_name('login-btn')
    elem_login.click()
    return driver

def save(driver):
    driver.get_screenshot_as_file(my_dataset.screen_path)
    img = Image.open(my_dataset.screen_path)
    box = (502, 407, 579, 452)
    image = img.crop(box)
    image.save(my_dataset.verify_path)
    #shutdown()

def main():
    driver = init()
    save(driver)   
    driver.quit()        

if __name__ == '__main__':
    for i in range(1, 1001):
        main()




