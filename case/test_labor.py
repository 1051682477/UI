import unittest
from base.base import Base
from page.labor_page import Loginpage
import random
import time,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class PetroleumProcess(unittest.TestCase):
    def setUp(self):
        self.driver = Base().initwebdriver("labor")
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def test_to_examine(self):
        '''审核工资单待确认脚本'''
        login_page = Loginpage(self.driver)
        login_page.login('16638660303', 'z12345')
        login_page.labor_sure_button('超时待确认')
        time.sleep(1)
        i = 1
        while i < 28:
            num = random.randint(0, 10)
            login_page.loop_labor_sure_button(str(num))
            i += 1
            time.sleep(1)
