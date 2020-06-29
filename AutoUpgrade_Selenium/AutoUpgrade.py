'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-29 13:46:06
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-29 17:53:37
@FilePath: /SetofAutomatedScripts/AutoUpgrade_Selenium/AutoUpgrade.py
'''

from pynput import keyboard
from pynput.keyboard import Key, Controller
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

class Upgrade:
    '''
    @description: 初始化函数
    @param {type} 
    @return: 
    '''
    

    def __init__(self):
        self.driver = driver
        
        self.URL = "http://tplinkdeco.net"
        self.Time2Sleep = 3
        self.DutName = "\"X60\""

        self.keyboard = Controller()
        self.reboottime = 100

    '''
    @description: 登陆功能
    @param {type} 
    @return: 
    '''
    def Login(self):
        self.driver.get("http://tplinkdeco.net")
        time.sleep(self.Time2Sleep)
        driver.find_element_by_xpath("//*[@id=\"local-login-pwd\"]/div[2]/div[1]/span[2]/input[1]").send_keys("1234567890")
        time.sleep(self.Time2Sleep)
        driver.find_element_by_id("local-login-button").click()
        time.sleep(self.Time2Sleep)
    
    '''
    @description: 登陆之后到上传固件之前的一些跳转操作
    @param {type} 
    @return: 
    '''
    def PrepareUpgrade(self):
        driver.find_element_by_xpath("//*[@id=\"main-menu\"]/div/div/ul/li[2]/a/span[1]").click()
        time.sleep(self.Time2Sleep)
        driver.find_element_by_xpath("//*[@id=\"navigator\"]/div[1]/div/ul/li[2]/a/span[2]").click()
        time.sleep(self.Time2Sleep)
        driver.find_element_by_xpath("//*[@id=\"navigator\"]/div[1]/div/ul/li[2]/ul/li[1]/a/span[2]").click()
        time.sleep(self.Time2Sleep)
        driver.find_element_by_xpath("//*[@id=\"manual-upgrade-file\"]/div[2]/div[1]/div[1]/span[2]/label").click()
        time.sleep(self.Time2Sleep)

    '''
    @description: 通过Pynput进行固件选择
    @param {type} 
    @return: 
    '''
    def ChooseFileAndUpgrade(self):
        #自定义选择升级固件的操作
        self.keyboard.press(Key.right)
        self.keyboard.release(Key.right)
        time.sleep(self.Time2Sleep)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        time.sleep(self.Time2Sleep)

    '''
    @description: 选中固件之后，对下拉框进行操作，并开始升级
    @param {type} 
    @return: 
    '''
    def ConfirmUpgrade(self):
        a = self.driver.find_element_by_xpath("//*[@value=\"- Please Select -\"]")
        a.click()
        time.sleep(self.Time2Sleep)
        self.driver.find_element_by_xpath("//*[@id=\"global-combobox-options\"]/div/div[3]/div/div/ul/li").click()
        time.sleep(self.Time2Sleep)
        self.driver.find_element_by_xpath("//*[@id=\"local-upgrade-btn\"]/div[2]/div[1]/a/span[2]").click()
        time.sleep(self.Time2Sleep)
        self.driver.find_element_by_id("firmware-upgrade-msg-btn-ok").click()
    
    '''
    @description: 等待重启
    @param {type} 
    @return: 
    '''
    def WaitingReboot(self):
        time.sleep(self.reboottime)

a=Upgrade()

for i in range(100):

    try:
        a.Login()
        a.PrepareUpgrade()
        a.ChooseFileAndUpgrade()
        a.ConfirmUpgrade()
        a.WaitingReboot()
    except Exception:
        pass