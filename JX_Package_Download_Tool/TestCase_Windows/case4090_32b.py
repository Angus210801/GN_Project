import sys
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_configure import renameMsiFile
from Common.function_basic import borwserConfigure, getLocation
from Common.function_Judge import isElementExist, isInputExist, isUploadButton


#JX-JDU: Make a package for both specified FW version update and DUT settings configuration. DUT has lower version.
def testcase4090_32b():
    #Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    #Configure driver
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # 进入到选择device页
    windowsTrack.clickNextButton()
    #输入Device
    windowsTrack.chooseDevice()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    #配置设置项为随机项
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
            "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(random.randint(1, selectlen - 1))
                default="*"
                selectedValue=Select(setting).first_selected_option.text
                chooseNotDefault=default in selectedValue
                while chooseNotDefault:
                    Select(setting).select_by_index(random.randint(1, selectlen - 1))
                    selectedValue = Select(setting).first_selected_option.text
                    chooseNotDefault = default in selectedValue
                i = i + 1
                continue
        elif isInputExist(driver,
                "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2021')
            except:
                i = i + 1
                continue
            i = i + 1
            continue
        else:
            i = i + 1
            continue

        # 判断按钮是否可用
        nextButton = driver.find_element_by_xpath("//input[@value='NEXT >']")
        isNextButtonEnable = nextButton.is_enabled()
        if isNextButtonEnable == False:
            i = 0
            while i < table_tr_number:
                flag = isElementExist(driver,
                                      "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                          i) + "].SelectedValue']")
                if flag:
                    setting = driver.find_element_by_css_selector(
                        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']")
                    if Select(setting):
                        i = i + 1
                        continue
                elif isInputExist(driver,
                                  "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']"):
                    try:
                        driver.find_element_by_css_selector(
                            "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                i) + "].SelectedValue']").send_keys('2021')
                        i = i + 1
                        continue
                    except Exception as e:
                        i = i + 1
                        continue
                elif isUploadButton(driver, "input[value='Upload']"):
                    try:
                        driver.find_element_by_css_selector(
                            "input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys(
                            "C:\\download\\001.bmp")
                        sleep(5)
                        i = i + 1
                        continue
                    except Exception as e:
                        print(e)
                else:
                    i = i + 1
                    continue
    # 判断按钮是否可用
    nextButton = driver.find_element_by_xpath("//input[@value='NEXT >']")
    isNextButtonEnable = nextButton.is_enabled()
    if isNextButtonEnable == False:
        i = 0
        while i < table_tr_number:
            flag = isElementExist(driver,
                                  "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']")
            if flag:
                setting = driver.find_element_by_css_selector(
                    "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']")
                if Select(setting):
                    i = i + 1
                    continue
            elif isInputExist(driver,
                              "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('2021')
                    i = i + 1
                    continue
                except Exception as e:
                    i = i + 1
                    continue
            elif isUploadButton(driver, "input[value='Upload']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys(
                        "C:\\download\\001.bmp")
                    sleep(5)
                    i = i + 1
                    continue
                except Exception as e:
                    print(e)
            else:
                i = i + 1
                continue
    print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
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
    renamesummary = file + '\\4090_32b.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName+ ' testcase4090_32b summary download successful')
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\4090_32b.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\4090_32b.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download32bit').click()
    #调用重命名函数
    renameMsiFile(driver, summary, renamesummary)
    print(testDeviceName+ ' testcase4090_32b download successful')
    print('\n')