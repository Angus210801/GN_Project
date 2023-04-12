import sys
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_configure import renameMsiFile, getLocation, renameMsiFile, setup_driver, renameSummary
from Common.function_basic import borwserConfigure, getLocation


# Device settings configuration with all setings and FW as LEAVE UNCHANGED but Protected.
def testcase3965_32b():
    #Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    #Configure driver
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # 进入到选择device页
    windowsTrack.clickNextButton()
    #输入Device
    windowsTrack.chooseDevice()

    #选择protect=protect
    setting = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("1")
    print(testDeviceName+' '+sys._getframe().f_code.co_name+' Configure finish')
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
    renameSummary(currentTestcaseName, file, testDeviceName)
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download32bit').click()
    #调用重命名函数
    renameMsiFile(driver, file, currentTestcaseName)
    print(testDeviceName+ ' testcase3965_32bit download successful')
    print('\n')