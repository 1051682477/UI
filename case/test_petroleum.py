import unittest
from base.base import Base
from page.petroleum_login import  Loginpage
import random
import time,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
class PetroleumProcess(unittest.TestCase):
    def setUp(self):
        self.driver=Base().initwebdriver("petroleum")
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def test_admin_login(self):
        '''验证政府登录状态断言角色名'''
        login_page = Loginpage(self.driver)
        login_page.admin_login(username='henan',password='123456')
        text=self.driver.find_element(By.XPATH,'//div[contains(text(),"省级商务厅")]').text#断言获取登录后角色文本
        self.assertIn('商务厅',text,msg=print(text))
    def test_company_login(self):
        '''验证企业登录状态断言角色名'''
        login_page = Loginpage(self.driver)
        login_page.company_login('limaodu','yao5458926')
        text = self.driver.find_element(By.XPATH, '//div[text()="limaodu"]').text  # 断言获取登录后角色文本
        self.assertEqual('limaodu',text,msg=print(text))




