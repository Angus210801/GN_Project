import os
import random
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_scripts.testcase_element_exist import isElementExist, isInputExist, isUploadButton
from test_scripts.testcase_action import *
from selenium.webdriver.support.select import Select
from test_scripts.testcase_action import goto_summary_page_and_download, action_download_msi, goto_pcsoftware_page, \
    action_download_jd


def testcase3961():
    """Jabra Direct Diagnostic Report plug-in version and s/n verification(not FW, settings=default）"""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Choose device
    windowsTrack.action_selectdevice_page()
    # Configure the device page with all settings as default
    settings_default(driver)
    # Protect = Yes
    config_the_protect_as_yes(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase3965():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Configure the protece=Yes
    config_the_protect_as_yes(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    ## Configure a random softphone
    config_random_sp(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase3965_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Configure the protece=Yes
    config_the_protect_as_yes(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Configure a random softphone
    config_random_sp(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi_32bit(driver)
    # Rename msi file
    rename_msi_file_32bit(driver, file, currentTestcaseName, testDeviceName)


def testcase3966():
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Select latest FW
    config_the_latest_FW(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Configure a random softphone
    config_random_sp(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase3966_32b():
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Select latest FW
    config_the_latest_FW(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Configure a random softphone
    config_random_sp(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi_32bit(driver)
    # Rename msi file
    rename_msi_file_32bit(driver, file, currentTestcaseName, testDeviceName)



def testcase3968():
    """Testcase3968: Configure the FW as manage by Jabra, download Jabra Direct, configure a random softphone"""

    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Configure the FW as manage by Jabra
    config_the_FW_as_manage_by_jabra(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Configure a random softphone
    config_random_sp(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)



def testcase3969():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # configure the protection as No
    config_the_protect_as_no(driver)
    # configure the settings as random
    config_settings_as_random(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Configure a random softphone
    config_random_sp(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)



def testcase4090():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # select the latest FW
    config_the_latest_FW(driver)
    # Cnnfure settings as not default
    config_settings_as_not_default(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase4090_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # select the latest FW
    config_the_latest_FW(driver)
    # Cnnfure settings as not default
    config_settings_as_not_default(driver)
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to the PC software page
    goto_pcsoftware_page(driver)
    # Download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi_32bit(driver)
    # Rename msi file
    rename_msi_file_32bit(driver, file, currentTestcaseName, testDeviceName)


def testcase4128_1():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Config the settings as default
    settings_default()
    # Print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Config the SP as random
    config_random_sp(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)

def testcase4128_2():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    #  Input device name
    windowsTrack.action_selectdevice_page()
    # print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Config the SP as random
    config_random_sp(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase4128_3():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()
    # Configuure the settings as not default
    config_settings_as_not_default(driver)
    # print the configure finish message
    print_the_config_finish()
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase4153_1():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Config the FW aS latest
    config_the_latest_FW(driver)
    # print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase4153_2():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # 选择Fw
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList = Select(fw_select)
    fwNum = len(fwList.options)
    i = 2
    if i != fwNum - 1:
        Select(fw_select).select_by_index(i)
        selectedFW = Select(fw_select).first_selected_option.text
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()
        print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
        # #进入softphone配置页
        driver.find_element_by_xpath("//input[@value='NEXT >']").click()
        # 勾选下载JD
        # Go to PC software page
        goto_pcsoftware_page(driver)
        ## 选择1个随机的Preferred softphone
        setting = driver.find_element_by_css_selector(
            "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
        if Select(setting):
            select = Select(setting)
            selectlen = len(select.options)
            Select(setting).select_by_index(random.randint(0, selectlen - 1))
        # 跳转到.msi下载页面
        driver.find_element_by_xpath("//input[@value='NEXT >']").click()
        # 跳转到Summary下载页面
        driver.find_element_by_xpath("//input[@value='NEXT >']").click()
        # 下载Summary
        driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
        # 重命名summary文件
        sleep(5)
        summary = file + '\\summary.html'
        renamesummary = file + '\\4153_' + selectedFW + '.html'
        try:
            os.rename(summary, renamesummary)
            print(testDeviceName + ' testcase4153 ' + selectedFW + ' summary download successful')
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\4153_' + selectedFW + '.msi'
        except Exception as e:
            os.remove(renamesummary)
            os.rename(summary, renamesummary)
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\4153_' + selectedFW + '.msi'
        # 返回到下载页
        driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
        # 勾选同意协议
        driver.find_element_by_id('eulaOk').click()
        # #点击下载
        driver.find_element_by_id('download64bit').click()
        # 调用重命名函数
        rename_msi_file(driver, summary, renamesummary)
        print(testDeviceName + ' testcase4153 ' + selectedFW + ' download successful')
        print('\n')
        testcase4153_3()
    else:
        print(testDeviceName + "only 1 version in JX")


def testcase4153_3():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # 选择Fw
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList = Select(fw_select)
    fwNum = len(fwList.options)
    i = 3
    if i != fwNum - 1:
        Select(fw_select).select_by_index(i)
        selectedFW = Select(fw_select).first_selected_option.text
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()
        print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
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
        renamesummary = file + '\\4153_' + selectedFW + '.html'
        try:
            os.rename(summary, renamesummary)
            print(testDeviceName + ' testcase4153 ' + selectedFW + ' summary download successful')
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\4153_' + selectedFW + '.msi'
        except Exception as e:
            os.remove(renamesummary)
            os.rename(summary, renamesummary)
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\4153_' + selectedFW + '.msi'
        # 返回到下载页
        driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
        # 勾选同意协议
        driver.find_element_by_id('eulaOk').click()
        # #点击下载
        driver.find_element_by_id('download64bit').click()
        # 调用重命名函数
        rename_msi_file(driver, summary, renamesummary)
        print(testDeviceName + ' testcase4153 ' + selectedFW + ' download successful')
        print('\n')
    else:
        print(testDeviceName + " only 2 version in JX")
        driver.close()


def testcase5509():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()
    # 选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\5509.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase5509 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\5509.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\5509.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase5509 download successful')
    print('\n')


def testcase5509_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()
    # 选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
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
    renamesummary = file + '\\5509_32bit.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase5509 summary download successful')
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5509_32bit.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5509_32bit.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download32bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase5509_32bit download successful')
    print('\n')


def testcase5664():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # configuration
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(selectlen - 1)
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2020')
                i = i + 1
                continue
            except:
                i = i + 1
                continue
        else:
            i = i + 1
            continue

    print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\5664.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase5664 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\5664.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\5664.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase5664 download successful')
    print('\n')


def testcase5664_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # configuration
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(selectlen - 1)
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2020')
                i = i + 1
                continue
            except:
                i = i + 1
                continue
        else:
            i = i + 1
            continue

    print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\5664_32b.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase5664_32bit summary download successful')
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5664_32b.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5664_32b.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download32bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase5664_32bit download successful')
    print('\n')


def testcase5665():
    ROOT_DIR = os.path.dirname(os.path.abspath("../config/bat.bmp"))
    print(ROOT_DIR)
    ROOT_DIR = ROOT_DIR + "\TestCase_Windows\001.bmp"
    print(ROOT_DIR)
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                Select(setting).select_by_index("1")
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2020')
                i = i + 1
                continue
            except:
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
                        "C:\\download\\bat.bmp")
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
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\5665.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase5665 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\5665.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\5665.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase5665 download successful')
    print('\n')


def testcase5665_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                Select(setting).select_by_index("1")
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2020')
                i = i + 1
                continue
            except:
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
                        "C:\\download\\bat.bmp")
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
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\5665.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase5665_32bit summary download successful')
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5665_32b.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5665_32b.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download32bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase5665_32bit download successful')
    print('\n')


def testcase7195():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # 选择FW为低版本
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList = Select(fw_select)
    fwNum = len(fwList.options)
    i = 3
    if i != fwNum - 1:
        i = fwNum - 1
        Select(fw_select).select_by_index(i)
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()

    # 配置设置项为随机项
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(random.randint(1, selectlen - 1))
                default = "*"
                selectedValue = Select(setting).first_selected_option.text
                chooseNotDefault = default in selectedValue
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
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys(
                        "C:\\download\\bat.bmp")
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
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7195.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase7195 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\7195.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\7195.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase7195 download successful')
    print('\n')


def testcase7196():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # 配置设置项为随机项
    set_table = driver.find_element(By.CLASS_NAME, 'settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(random.randint(1, selectlen - 1))
                default = "*"
                selectedValue = Select(setting).first_selected_option.text
                chooseNotDefault = default in selectedValue
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
                        "C:\\download\\bat.bmp")
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
    # 勾选下载JD
    # Go to PC software page
    goto_pcsoftware_page(driver)
    ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    # 跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7196.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName + ' testcase7196 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\7196.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\7196.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    # 调用重命名函数
    rename_msi_file(driver, summary, renamesummary)
    print(testDeviceName + ' testcase7196 download successful')
    print('\n')


def testcase10312w():
    i = 1
    while i <= 6:
        fo = open("device.txt", "rt")
        testDeviceName = fo.read()
        file = get_save_dir() + testDeviceName
        options = browser_configure()
        global driver
        driver = webdriver.Chrome(chrome_options=options)
        windowsTrack = windowsTrack(driver)
        # Select device页
        windowsTrack.goto_selectdevice_page()
        # 输入设备名
        windowsTrack.action_selectdevice_page()
        # 选择FW
        fw_select = driver.find_element_by_css_selector(
            "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
        Select(fw_select).select_by_index("1")

        # 判断是否存在Language setting
        try:
            language_region_select = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionId']")
            Select(language_region_select).select_by_index("1")
            language_select = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionLanguageId']")
            languageList = Select(language_select)
            languageNum = len(languageList.options)
            Select(language_select).select_by_index(i)
            language_select = Select(language_select).first_selected_option.text
            # 配置完成后打印提醒消息
            print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
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
            renamesummary = file + '\\10312_' + language_select + '.html'
            try:
                os.rename(summary, renamesummary)
                print(testDeviceName + ' testcase4090 summary download successful')
                summary = file + '\\JabraXPRESSx64.msi'
                renamesummary = file + '\\10312_' + language_select + '.msi'
            except Exception as e:
                os.remove(renamesummary)
                os.rename(summary, renamesummary)
                summary = file + '\\JabraXPRESSx64.msi'
                renamesummary = file + '\\10312_' + language_select + '.msi'
            # 返回到下载页
            driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
            # 勾选同意协议
            driver.find_element_by_id('eulaOk').click()
            # #点击下载
            driver.find_element_by_id('download64bit').click()
            # 调用重命名函数
            rename_msi_file(driver, summary, renamesummary)
            i = i + 1

        except:
            print("There is no language setting for this device")
            driver.close()
            break


def testcase10449():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()

    # 选择Fw
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList = Select(fw_select)
    fwNum = len(fwList.options)
    i = 2
    if i != fwNum - 1:
        Select(fw_select).select_by_index(i)
        selectedFW = Select(fw_select).first_selected_option.text
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()
        print(testDeviceName + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
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
        renamesummary = file + '\\10449_' + selectedFW + '.html'
        try:
            os.rename(summary, renamesummary)
            print(testDeviceName + ' testcase10449 ' + selectedFW + ' summary download successful')
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\10449_' + selectedFW + '.msi'
        except Exception as e:
            os.remove(renamesummary)
            os.rename(summary, renamesummary)
            summary = file + '\\JabraXPRESSx64.msi'
            renamesummary = file + '\\10449_' + selectedFW + '.msi'
        # 返回到下载页
        driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
        # 勾选同意协议
        driver.find_element_by_id('eulaOk').click()
        # #点击下载
        driver.find_element_by_id('download64bit').click()
        # 调用重命名函数
        rename_msi_file(driver, summary, renamesummary)
        print(testDeviceName + ' testcase10449 ' + selectedFW + ' download successful')
        print('\n')
    else:
        print(testDeviceName + "just has 1 version in JX,so this case will pass")
        driver.close()
