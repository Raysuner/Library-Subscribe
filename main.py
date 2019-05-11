#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-04-17 21:55:08
@LastEditTime: 2019-05-11 16:47:41
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from PIL import Image
import keras

import captcha_predict
from captcha_gen import save
import my_dataset

class Subscribe:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(960, 1080)
        self.login_url = my_dataset.get_login_url()
        self.driver.get(self.login_url)
        time.sleep(1)
        self.elem_login = self.driver.find_element_by_class_name('login-btn')
        self.elem_login.click()
        self.elem_user = self.driver.find_element_by_name('username')
        self.elem_verify = self.driver.find_element_by_name('verify')
        self.elem_pwd = self.driver.find_element_by_name('password')
        self.element = self.driver.find_element_by_id('checkpic')
        self.confirm1 = self.driver.find_element_by_class_name('ui-dialog-autofocus')

        self.verify = ''               
        self.email = '17775306795@163.com'
    
    def get_verify(self):
        self.verify = captcha_predict.main()

    def push(self):
        self.elem_user.send_keys("15205150438")
        self.elem_pwd.send_keys("227278")
        self.elem_verify.send_keys(self.verify)
        self.confirm1.click()
        time.sleep(5)
        

    def select(self):
        confirm1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr[3]/td/div[2]/button') ###预约规则确定键
        print('11111\n')
        time.sleep(2)
        confirm1.click()
        number = self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[36]')  #座位位置
        print('22222\n')
        time.sleep(2)
        number.click()
        confirm2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr[3]/td/div[2]/button[2]')#座位位置确定键
        time.sleep(2)
        print('33333\n')
        confirm3 = self.driver.find_element_by_class_name('ui-dialog-autofocus')
        confirm3.click()
        time.sleep(2)
        print('44444\n')
        confirm4 = self.driver.find_element_by_class_name('ui-dialog-autofocus')
        confirm4.click()
        time.sleep(20)
        
    def main(self):
        save(self.driver)
        self.get_verify()
        self.push()
        self.select()
        

    #def send_email(self):               


if __name__ == '__main__':
    Subscribe().main()




