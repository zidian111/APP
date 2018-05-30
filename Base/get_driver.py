from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['noReset'] = 'true'
    # app的信息
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

