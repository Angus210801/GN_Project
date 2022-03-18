import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Common.function_Configure import borwserConfigure, renameAndclose


def testcase10312w():
    i=1
    while i<=6:
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        file = "C:\\download\\" +lastingDevicename
        options = borwserConfigure()
        global driver
        driver = webdriver.Chrome(chrome_options=options)
        from Common.function_Basic import windowsPage
        windowsPage = windowsPage(driver)
        #Select device页
        windowsPage.clickNextButton()
        #输入设备名
        windowsPage.chooseDevice()
        #选择FW
        fw_select = driver.find_element_by_css_selector(
            "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
        Select(fw_select).select_by_index("1")


        #判断是否存在Language setting
        try:
            language_region_select = driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionId']")
            Select(language_region_select).select_by_index("1")
            language_select=driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionLanguageId']")
            languageList=Select(language_select)
            languageNum=len(languageList.options)
            Select(language_select).select_by_index(i)
            language_select=Select(language_select).first_selected_option.text
            #配置完成后打印提醒消息
            print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
            # #进入softphone配置页
            driver.find_element_by_xpath("//input[@value='NEXT >']").click()
            # 跳转到.msi下载页面
            driver.find_element_by_xpath("//input[@value='NEXT >']").click()
            # 跳转到Summary下载页面
            driver.find_element_by_xpath("//input[@value='NEXT >']").click()
            # 下载Summary
            driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
            # 重命名summary文件
            sleep(5)
            summary = file + '\\summary.html'
            renamesummary = file + '\\10312_'+language_select+'.html'
            try:
                os.rename(summary, renamesummary)
                print(lastingDevicename + ' testcase4090 summary download successful')
                summary = file + '\\JabraXPRESSx64.msi'
                renamesummary = file + '\\10312_'+language_select+'.msi'
            except Exception as e:
                os.remove(renamesummary)
                os.rename(summary, renamesummary)
                summary = file + '\\JabraXPRESSx64.msi'
                renamesummary = file + '\\10312_'+language_select+'.msi'
            # 返回到下载页
            driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
            # 勾选同意协议
            driver.find_element_by_id('eulaOk').click()
            # #点击下载
            driver.find_element_by_id('download64bit').click()
            # 调用重命名函数
            renameAndclose(driver, summary, renamesummary)
            i=i+1

        except:
            print("There is no language setting for this device")
            driver.close()
            break
