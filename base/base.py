from  selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import NoAlertPresentException as e
from selenium.webdriver.common.by import By
import time,os


class Base:
    def initwebdriver(self, projectname):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        if projectname == "petroleum":  # 成品油
            self.driver.get("http://192.168.0.52:8082/ent/#/login?type=1")
        elif projectname == "labor":  # 劳务
            self.driver.get("http://47.104.30.185/#/user/login")
        time.sleep(1)
        return self.driver


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        return "driver"

    # 等待元素定位，并返回传入元素
    def locator(self, loc):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((loc)))
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, value):
        self.locator(loc).send_keys(value)
        pass

    # 点击
    def click(self, loc):
        self.locator(loc).click()
        pass

    # 获取文本
    def text(self, loc):
        self.locator(loc).text()
        pass

    # 下拉框
    def select(self, loc, value):
        Select(self.locator(loc)).select_by_visible_text(value)
        pass

    # 键盘事件回车
    def key_name(self):
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        pass

    # 鼠标悬浮
    def action_chains(self, loc):
        ActionChains(self.driver).move_to_element(self.locator(loc)).perform()
