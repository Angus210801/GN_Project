import sys
import os
import shutil
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_configure import renameMsiFile, getLocation
from Common.function_basic import borwserConfigure, getLocation


# JX-JDU: Verify that the " Voice Language" ( Tune Pack) setting can be write to the DUT which has different FW version_Spanish.

def testcase10312l():
    i=1
    while i<=6:
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        file = getLocation() +lastingDevicename
        options = borwserConfigure()
        global driver
        driver = webdriver.Chrome(chrome_options=options)
        from Common.function_basic import linuxindexPage
        linuxindexPage = linuxindexPage(driver)
        #Select device页
        linuxindexPage.clickNextButton()
        #输入设备名
        linuxindexPage.chooseDevice()
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

            driver.find_element_by_xpath("//input[@value='NEXT >']").click()
            # 下载Summary
            driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
            # 重命名summary文件
            sleep(5)
            summary = file + '\\summary.html'
            renamesummary = file + '\\10312'+language_select+'.html'
            try:
                os.rename(summary, renamesummary)
                print(lastingDevicename+ ' testcase10312 summary download successful')
                summary = file + '\\JabraXpressFiles.zip'
                renamesummary = file + '\\10312_'+language_select
            except Exception as e:
                os.remove(renamesummary)
                os.rename(summary, renamesummary)
                summary = file + '\\JabraXpressFiles.zip'
                renamesummary = file + '\\10312'+language_select
            # 返回到下载页
            driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
            # 勾选同意协议
            driver.find_element_by_id('eulaOk').click()
            # 输入网址：
            driver.find_element_by_css_selector("input[name='localServerUrl']").send_keys('http://my.gn.com/')
            # #点击下载
            driver.find_element_by_id('downloadZip').click()
            sleep(20)
            try:
                while os.path.exists(summary)==False:
                    sleep(10)
                with zipfile.ZipFile(summary, "r") as zip_ref:
                    zip_ref.extractall(file)
                summary = file + '\\Files_to_place_on_local_server'
                os.rename(summary, renamesummary)
                shutil.rmtree(file + '\\Files_to_install_on_end-user_computers')
                os.remove(file + '\\JabraXpressFiles.zip')
                os.remove(file + '\\readme.txt')
                print(lastingDevicename+ ' testcase10312 '+language_select+'download successful')
                print('\n')
                i = i + 1
                driver.close()

            except Exception as e:
                sleep(40)
                os.rename(summary, renamesummary)
                print('rename success')
                i=i+1
        except:
            print("There is no language setting for this device")
            driver.close()
            break