from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
from PIL import Image


class Captcha:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.local_time =datetime.datetime.now()
        self.day_time = str(self.local_time.year) + '-' + str(self.local_time.month) + '-' + str(self.local_time.day + 1)
        self.login_url = 'http://219.231.8.121/Home/Web/area?area=7&segment=' + '15119' + '&day=' + self.day_time + '&startTime=07:00&endTime=22:00'
        self.driver.get(self.login_url)
        time.sleep(2)
        self.elem_login = self.driver.find_element_by_class_name('login-btn')
        self.elem_login.click()   

    def image_process(self, filename):
        self.driver.get_screenshot_as_file('./project/Subscribe/gen_' + filename)
        img = Image.open('./project/Subscribe/gen_' + filename)
        box = (659, 380, 738, 428)
        image = img.crop(box)
        image.save('./project/Subscribe/dataset/images/' + filename)
        self.shutdown()

    def shutdown(self):
        self.driver.quit()

    def main(self, filename):
        self.image_process(filename)           


if __name__ == '__main__':
    for i in range(580, 1000):
        filename = str(i) + '.png'
        Captcha().main(filename)




