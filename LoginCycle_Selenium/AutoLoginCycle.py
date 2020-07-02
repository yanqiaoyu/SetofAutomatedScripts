'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-07-02 11:22:30
@LastEditors: YanQiaoYu
@LastEditTime: 2020-07-02 17:34:52
@FilePath: /SetofAutomatedScripts/LoginCycle/AutoLoginCycle.py
'''
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
@description: 装饰器
@param {type} 
@return: 
'''
def logdeco(func):
    def wrapper(*args, **kw):
        
        if func(*args, **kw):
            print("[{}]Pass".format(func.__qualname__))
        else:
            print("[{}]Fail".format(func.__qualname__))

    return wrapper

class LoginCycle:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = "http://tplinkdeco.net"
        self.Time2Sleep = 3
    '''
    @description: 登陆功能
    @param {type} 
    @return: 
    '''
    @logdeco
    def Login(self):
        self.driver.get(self.URL)

        try:
            #输入框是否存在
            if WebDriverWait(self.driver, 5).until(
                #located后面的括号里的参数需要用一个括号全部括起来
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
                ):
                #输入密码
                self.driver.find_element_by_css_selector('input[type="password"]').send_keys("1234567890")
                
                #登陆按钮是否存在
                if WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '[title="LOG IN"]'))
                    ):
                    #登陆
                    self.driver.find_element_by_css_selector('[title="LOG IN"]').click()

                    #登出按钮是否存在
                    if WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, '[title="Log Out"]'))
                        ):

                        self.driver.find_element_by_css_selector('[title="Log Out"]').click()
                        #OK按钮是否存在
                        '''
                        if WebDriverWait(self.driver, 5).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, '[title="OK"]'))
                            ):'''

                        self.driver.find_elements_by_class_name("button-button")[-1].click()
        
            return True
        except Exception as e:
            # 访问异常的错误编号和详细信息
            print(str(e))
            print('行号', e.__traceback__.tb_lineno)
            a,b,c = sys.exc_info()
            print(a)
            print(b)
            print(c)
            return False

    def Close(self):
        self.driver.close()

a=LoginCycle()
for i in range(1,101):
    a.Login()
    time.sleep(1)
    print("This is the {} times".format(i))
a.Close()