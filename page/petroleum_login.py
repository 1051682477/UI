from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base import WebDriver
import time

class Loginpage(WebDriver):


    '''首页基础按键'''
    admin_login_icon=(By.XPATH,'//span[text()="政府端登录"]')#政府登录图标
    firm_login_icon=(By.XPATH,'//span[text()="企业端登录"]')#企业登录图标
    username_loc=(By.XPATH,'//input[@placeholder="请输入用户名"]')#账号
    password_loc=(By.XPATH ,'//input[@placeholder="请输入密码"]')#密码输入框
    remember_password=(By.CLASS_NAME,'el-checkbox__label')#记住密码
    forget_password=(By.PARTIAL_LINK_TEXT,'忘记密码？')#忘记密码
    login_button=(By.XPATH,'//span[text()="登录"]/..')#登录按钮
    business_button=(By.XPATH,'//div[@class="user"]/div/button')
    '''注册企业账号'''
    login_new=(By.XPATH,'//span[text()="注册"]')#注册按钮
    username_new=(By.XPATH,'//input[@placeholder="请输入用户名"]')#用户输入框
    password_new=(By.XPATH,'//input[@placeholder="请输入密码"]')#密码输入框
    again_password=(By.XPATH,'//input[@placeholder="请再次确认密码"]')#再次确认密码

    def admin_login(self,username,password):
        self.click(self.admin_login_icon)
        self.input(self.username_loc,username)
        self.input(self.password_loc,password)
        self.click(self.remember_password)
        self.click(self.login_button)
        time.sleep(2)
        self.click(self.business_button)
        time.sleep(3)
        pass
    def company_login(self,username,password):
        self.click(self.firm_login_icon)
        self.input(self.username_loc,username)
        self.input(self.password_loc,password)
        self.click(self.remember_password)
        self.click(self.login_button)
        time.sleep(2)
        self.click(self.business_button)
        time.sleep(3)
        pass






