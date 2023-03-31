from Common.function_Configure import getLocation, borwserConfigure, baseConfigure
from selenium import webdriver
import Common.function_Basic



def setup_driver():
    # 读取设备名称
    with open("device.txt", "rt") as f:
        lastingDevicename = f.read()

    # 获取文件位置并构建选项
    file = getLocation() + lastingDevicename
    options = borwserConfigure()

    # 创建并返回WebDriver对象和windowsPage对象
    driver = webdriver.Chrome(chrome_options=options)
    windowsPage = Common.function_Basic.windowsPage(driver)
    # windowsPage = windowsPage(driver)
    return driver, windowsPage,lastingDevicename,file

