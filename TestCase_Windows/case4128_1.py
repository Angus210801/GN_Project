import sys
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.configure import renameAndclose,borwserConfigure


# All settings in the device can be change with installation of an MS file at the end user PC
def testcase4128_1():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = "C:\\download\\" +lastingDevicename
    options=borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Page.indexPage import windowsPage
    windowsPage = windowsPage(driver)
    # 进入到选择device页
    windowsPage.clickNextButton()
    #输入Device
    windowsPage.chooseDevice()

    driver.find_element_by_xpath("//input[@value='SET ALL TO DEFAULT VALUES']").click()
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #勾选下载JD
    driver.find_element_by_xpath("//input[@value='true']").click()
     ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    #跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\4128_1.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase4128_1 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\4128_1.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\4128_1.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    #调用重命名函数
    renameAndclose(driver,summary,renamesummary)
    print(lastingDevicename+ ' testcase4128_1 download successful')
    print('\n')