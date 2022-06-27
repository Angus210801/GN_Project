import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_Configure import renameAndclose,borwserConfigure,getLocation,getLocation

#Jabra Direct Diagnostic Report plug-in version and s/n verification [19903]（配置设置项为default）
def testcase3961():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = getLocation() +lastingDevicename
    # print(file)
    options=borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Common.function_Basic import windowsPage
    windowsPage = windowsPage(driver)
    # 进入到选择device页
    windowsPage.clickNextButton()
    #输入Device
    windowsPage.chooseDevice()
    #选择FW

    #配置设置项为Default并选择protect=protect
    driver.find_element_by_xpath("//input[@value='SET ALL TO DEFAULT VALUES']").click()
    setting = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("1")
    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #勾选下载JD
    driver.find_element_by_xpath("//input[@value='true']").click()
    #跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\3961.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase3961 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\3961.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\3961.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    #调用重命名函数
    renameAndclose(driver,summary,renamesummary)
    print(lastingDevicename+ ' testcase3961 download successful')
    print('\n')
