#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Raysuner
@Github: https://github.com/Raysuner
@LastEditors: Raysuner
@Email: 17775306795@163.com
@Date: 2019-04-17 21:55:08
@LastEditTime: 2019-05-25 18:16:02
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from PIL import Image
import keras

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

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
        self.confirm = self.driver.find_element_by_class_name('ui-dialog-autofocus')
        self.success = False

    def get_verify(self):
        self.verify = captcha_predict.main()
        print(self.verify)

    def push(self):
        self.elem_user.send_keys("15205150438")
        self.elem_pwd.send_keys("227278")
        self.elem_verify.send_keys(self.verify)
        self.confirm.click()
        time.sleep(5)
        

    def select(self):
        confirm1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr[3]/td/div[2]/button') ###预约规则确定键
        confirm1.send_keys(Keys.ENTER)

        number = self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[94]')  #座位位置
        number.send_keys(Keys.ENTER)

        confirm3 = self.driver.find_element_by_class_name('ui-dialog-autofocus')
        confirm3.send_keys(Keys.ENTER)

        confirm4 = self.driver.find_element_by_class_name('ui-dialog-autofocus')
        confirm4.click()
        
        self.success = True
        time.sleep(10)
    
    def format_addr(self, str):
        name, addr = parseaddr(str)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_email(self):  
        from_addr = '1669232805@qq.com'
        password = 'lkccrpaitcnobabi'
        to_addr = '17775306795@163.com'
        smtp_server = 'smtp.qq.com'
        msg1 = MIMEText('订阅成功', 'plain', 'utf-8')
        msg2 = MIMEText('订阅失败', 'plain', 'utf-8')
        if self.success is True:
            msg = msg1
        else:
            msg = msg2
        msg['From'] = self.format_addr('python爱好者 <%s>' % from_addr)
        msg['To'] = self.format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def main(self):
        save(self.driver)
        self.get_verify()
        self.push()
        # self.select()             
        # self.send_email()

if __name__ == '__main__':
    Subscribe().main()




