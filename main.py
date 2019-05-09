#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-04-17 21:55:08
@LastEditTime: 2019-05-09 20:08:32
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
from PIL import Image
import keras

import captcha_predict

class Subscribe:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.local_time =datetime.datetime.now()
        self.day_time = str(self.local_time.year) + '-' + str(self.local_time.month) + '-' + str(self.local_time.day + 1)
        self.login_url = 'http://219.231.8.121/Home/Web/area?area=7&segment=' + '17303' + '&day=' + self.day_time + '&startTime=07:00&endTime=22:00'
        self.driver.get(self.login_url)
        print(self.login_url)
        time.sleep(2)
        self.elem_login = self.driver.find_element_by_class_name('login-btn')
        self.elem_login.click()
        self.elem_user = self.driver.find_element_by_name('username')
        self.elem_verify = self.driver.find_element_by_name('verify')
        self.elem_pwd = self.driver.find_element_by_name('password')
        self.element = self.driver.find_element_by_id('checkpic')
        self.elem_confirm = self.driver.find_element_by_class_name('ui-dialog-autofocus')

        self.verify = ''               
        self.email = '17775306795@163.com'
    
    def get_verify(self):
        self.verify = captcha_predict.main()


    def push(self):
        self.elem_user.send_keys("15205150438")
        self.elem_pwd.send_keys("227278")
        self.elem_verify.send_keys(self.verify)
        self.elem_confirm.click()

    def select(self):
        elem_number = self.driver.find_element_by_css_selector('li.seat:nth-child(145)')  
        elem_number.click()
        elem_number.send_keys(Keys.RETURN)

    def shutdown(self):
        self.driver.quit()

    def main(self):
        self.get_verify()
        self.push()
        self.select()

    #def send_email(self):               


if __name__ == '__main__':
    Subscribe().main()




