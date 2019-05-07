#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-04-17 21:55:08
@LastEditTime: 2019-05-07 20:32:18
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
from PIL import Image
import captcha_process
import keras

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

        self.verify_number = ''               
        self.email = '17775306795@163.com'
    
    def resize(self, fullpath):
        im = Image.open(fullpath)
        im = im.resize((8, 48))
        region = im.copy()
        gray_img = Image.new('RGB', (28, 28), (255, 255, 255))
        gray_img.paste(region, (10, -5))
        gray_img.save(fullpath)

    def image_process(self):
        screen_path = './project/Subscribe/'
        captcha_path = './project/Subscribe/'
        sub_captcha_path = './project/Subscribe/img/'
        model_path = './project/Subscribe/model.cy'
        self.driver.get_screenshot_as_file(screen_path + 'screen.png')
        img = Image.open(screen_path + 'screen.png')
        box = (659, 380, 738, 428)
        image = img.crop(box)
        image.save(captcha_path + 'cptacha.png')
        capt_img = Image.open(captcha_path + 'cptacha.png')
        gray_img = captcha_process.rgb2gray(capt_img)
        bin_img = captcha_process.binarizing(gray_img)
        boxs = captcha_process.vertical(bin_img)
        cnt = 1
        for subbox in boxs:
            subbox = (subbox[0], 0, subbox[1], 48)
            img = bin_img.crop(subbox)
            width = img.size[0] 
            if width >= 15:
                mid = img.size[0] // 2 + 1
                print('mid = %d' % mid)
                img1 = img.crop((0, 0, mid, 48))
                img1.save(sub_captcha_path + str(cnt) + '.png')
                cnt += 1
                img2 = img.crop((mid, 0, width, 48))
                img2.save(sub_captcha_path + str(cnt) + '.png')
                cnt += 1
            else:
                img.save(sub_captcha_path + str(cnt) + '.png')
                cnt += 1
        files = os.listdir(sub_captcha_path)
        for file in files:
            fullpath = sub_captcha_path + file
            self.resize(fullpath)
            keras.models.load_model(model_path)


    def push(self):
        self.elem_user.send_keys("15205150438")
        self.elem_pwd.send_keys("227278")
        self.elem_verify.send_keys(self.verify_number)
        #self.elem_confirm.click()

    def select_number(self):
        elem_number = self.driver.find_element_by_css_selector('li.seat:nth-child(145)')  
        elem_number.click()
        elem_number.send_keys(Keys.RETURN)

    def shutdown(self):
        self.driver.quit()

    def main(self):
        self.image_process()
        self.push()

    #def send_email(self):               


if __name__ == '__main__':
    Subscribe().main()




