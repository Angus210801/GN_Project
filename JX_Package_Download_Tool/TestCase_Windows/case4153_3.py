import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_Configure import renameAndclose,borwserConfigure,getLocation



def testcase4153_3():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = getLocation() +lastingDevicename
    options=borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Common.function_Basic import windowsPage
    windowsPage = windowsPage(driver)
    # 进入到选择device页
    windowsPage.clickNextButton()
    #输入Device
    windowsPage.chooseDevice()

    #选择Fw
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList=Select(fw_select)
    fwNum=len(fwList.options)
    i=3
    if i != fwNum-1 :
        Select(fw_select).select_by_index(i)
        selectedFW=Select(fw_select).first_selected_option.text
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()
        print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
        # #进入softphone配置页
        driver.find_element_by_xpath("//input[@value='NEXT >']").click()
        #跳转到.msi下载页面
        driver.find_element_by_xpath("//input[@value='NEXT >']").click()
        #跳转到Summary下载页面
        driver.find_element_by_xpath("//input[@value='NEXT >']").click()
        # 下载Summary
        driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
        # 重命名summary文件
        sleep(5)
        summary = file + '\\summary.html'
        renamesummary = file + '\\4153_'+selectedFW+'.html'
        try:
            os.rename(summary, renamesummary)
            print(lastingDevicename+ ' testcase4153 '+selectedFW+' summary download successful')
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\4153_'+selectedFW+'.msi'
        except Exception as e:
            os.remove(renamesummary)
            os.rename(summary, renamesummary)
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\4153_'+selectedFW+'.msi'
        # 返回到下载页
        driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
        # 勾选同意协议
        driver.find_element_by_id('eulaOk').click()
        # #点击下载
        driver.find_element_by_id('download64bit').click()
        #调用重命名函数
        renameAndclose(driver,summary,renamesummary)
        print(lastingDevicename+ ' testcase4153 '+selectedFW+' download successful')
        print('\n')
    else:
        print(lastingDevicename+" only 2 version in JX")
        driver.close()