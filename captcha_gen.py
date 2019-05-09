#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-05-04 22:07:01
@LastEditTime: 2019-05-09 19:50:48
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
from PIL import Image

import my_dataset

class Captcha:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.local_time =datetime.datetime.now()
        self.day_time = str(self.local_time.year) + '-' + str(self.local_time.month) + '-' + str(self.local_time.day + 1)
        self.login_url = 'http://219.231.8.121/Home/Web/area?area=7&segment=' + '15125' + '&day=' + self.day_time + '&startTime=07:00&endTime=22:00'
        print(self.login_url)
        self.driver.get(self.login_url)
        time.sleep(2)
        self.elem_login = self.driver.find_element_by_class_name('login-btn')
        self.elem_login.click()   

    def image_process(self):
        self.driver.get_screenshot_as_file(my_dataset.screen_path)
        img = Image.open(my_dataset.screen_path)
        box = (659, 380, 738, 428)
        image = img.crop(box)
        image.save(my_dataset.verify_path)
        self.shutdown()

    def shutdown(self):
        self.driver.quit()

    def main(self):
        self.image_process()           


if __name__ == '__main__':
    Captcha().main()




