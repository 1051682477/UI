from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base import WebDriver
import time

class Loginpage(WebDriver):
    '''登录界面定位'''
    object_button=(By.XPATH,'//span[text()="项目"]')#项目tab
    username_input=(By.XPATH,'//input[@placeholder="请输入账号管理员手机号码"]')
    password_input=(By.XPATH,'//input[@placeholder="请输入密码"]')
    login_button=(By.XPATH,'//button[@type="submit"]')#登录
    salary_button=(By.XPATH,'//span[text()="代发工资管理"]')#代发工资管理
    labor_sure=(By.XPATH,'//li[contains(text(),"工人确认")]')#工人确认
    view_details=(By.XPATH,'//div[@class="ant-table-body-inner"]/table/tbody/tr[1]/td/button')#查看详情
    to_be_confirmed=(By.XPATH,'//div[@class="ant-table-fixed-right"]/div[2]/div/table/tbody/tr[1]/td/button')#待确认
    reason_input=(By.XPATH,'//textarea[@placeholder="请输入代确认原因"]')#输入待确认原因
    sure_button=(By.XPATH,'//div[@class="ant-modal-footer"]/div/button[2]')#确认




    def login(self,username,password):
        self.click(self.object_button)
        self.input(self.username_input,username)
        self.input(self.password_input,password)
        time.sleep(1)
        self.click(self.login_button)

    def labor_sure_button(self,reason):
        self.click(self.salary_button)
        self.click(self.labor_sure)
        time.sleep(1)
        self.click(self.view_details)
        time.sleep(1)
        self.click(self.to_be_confirmed)
        time.sleep(1)
        self.input(self.reason_input,reason)
        time.sleep(1)
        self.click(self.sure_button)

    def loop_labor_sure_button(self,reason):
        self.click(self.to_be_confirmed)
        time.sleep(1)
        self.input(self.reason_input,reason)
        time.sleep(1)
        self.click(self.sure_button)




