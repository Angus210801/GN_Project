"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : main windows
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2021/02/25
#
#                   @Last Update  : 2023/05/23
#
#
#-------------------------------------------------------------------
"""
import time

from test_scripts.testcase_action import *
from selenium.webdriver.support.select import Select
from concurrent.futures import ThreadPoolExecutor
from test_scripts.testcase_action import goto_summary_page_and_download, action_download_msi, goto_pcsoftware_page, \
    action_download_jd


def testcase3961():
    """Jabra Direct Diagnostic Report plug-in version and s/n verification(not FW, settings=default）"""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase3965_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack,testDeviceName,file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack,testDeviceName,file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # Go to device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Config the settings as default
    settings_default(driver)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()
    # Configuure the settings as not default
    config_settings_as_not_default(driver)
    # print the configure finish message
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


def testcase4153_1():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
        Select(fw_select).first_selected_option.text
        # Configure allow downgrade
        config_allow_downgrade(driver)
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
        # Continue download
        testcase4153_3()
    else:
        print(testDeviceName + "only 1 version in JX")


def testcase4153_3():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # Go to configure page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()

    # Select FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList = Select(fw_select)
    fwNum = len(fwList.options)
    i = 3
    if i != fwNum - 1:
        Select(fw_select).select_by_index(i)
        selectedFW = Select(fw_select).first_selected_option.text
        # Configure allow downgrade
        config_allow_downgrade(driver)
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
        rename_msi_file(driver, file, currentTestcaseName+selectedFW,testDeviceName)
    else:
        print(testDeviceName + " only 2 version in JX")
        driver.close()


def testcase5509():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # Go to select device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # config the FW as latest
    config_the_latest_FW(driver)
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

def testcase5509_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # Go to select device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # config the FW as latest
    config_the_latest_FW(driver)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi_32bit(driver)
    # Rename msi file
    rename_msi_file_32bit(driver, file, currentTestcaseName, testDeviceName)


def testcase5664():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()
    # configuration settings as MAX
    config_settings_as_MAX(driver)
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


def testcase5664_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # 进入到选择device页
    windowsTrack.goto_selectdevice_page()
    # 输入Device
    windowsTrack.action_selectdevice_page()
    # configuration settings as MAX
    config_settings_as_MAX(driver)
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
    action_download_msi_32bit(driver)
    # Rename msi file
    rename_msi_file_32bit(driver, file, currentTestcaseName, testDeviceName)


def testcase5665():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # go to select device page
    windowsTrack.goto_selectdevice_page()
    # input device name
    windowsTrack.action_selectdevice_page()
    # Config all settings as MIN
    config_settings_as_Min(driver)
    # print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Config the SP as random
    config_random_sp(driver)
    # Config download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase5665_32b():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # go to select device page
    windowsTrack.goto_selectdevice_page()
    # input device name
    windowsTrack.action_selectdevice_page()
    # Config all settings as MIN
    config_settings_as_Min(driver)
    # print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Config the SP as random
    config_random_sp(driver)
    # Config download Jabra Direct
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi_32bit(driver)
    # Rename msi file
    rename_msi_file_32bit(driver, file, currentTestcaseName, testDeviceName)


def testcase7195():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # Go to select device page
    windowsTrack.goto_selectdevice_page()
    # Input device name
    windowsTrack.action_selectdevice_page()
    # Config the FW as lower than latest
    config_the_FW_as_lower_than_latest(driver)
    # Config the settings as random
    config_settings_as_random(driver)
    # print the configured finish message
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Config the SP as random
    config_random_sp(driver)
    # Download JD
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase7196():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
    # Go to select device page
    windowsTrack.goto_selectdevice_page()
    #  Input device name
    windowsTrack.action_selectdevice_page()
    # Config the settings as random
    config_settings_as_random(driver)
    # Go to PC software page
    goto_pcsoftware_page(driver)
    # Config the SP as random
    config_random_sp(driver)
    # Download JD
    action_download_jd(driver)
    # Go to summary page
    goto_summary_page_and_download(driver)
    # Download summary
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    action_download_msi(driver)
    # Rename msi file
    rename_msi_file(driver, file, currentTestcaseName, testDeviceName)


def testcase10312w():
    i = 1
    while i <= 6:
        # Get current test case name
        currentTestcaseName = sys._getframe().f_code.co_name
        # Configure driver
        driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
        # Select device page
        windowsTrack.goto_selectdevice_page()
        # Input device name
        windowsTrack.action_selectdevice_page()
        # Config the latest FW
        config_the_latest_FW(driver)
        # Determine whether there is a language selection box
        try:
            language_region_select = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionId']")
            Select(language_region_select).select_by_index("1")
            language_select = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionLanguageId']")
            languageList = Select(language_select)
            languageNum = len(languageList.options)
            print("There are " + str(languageNum) + " languages for this device")
            # Config the language
            Select(language_select).select_by_index(i)
            language_select = Select(language_select).first_selected_option.text
            # Print the configured finish message
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
            currentTestcaseName=currentTestcaseName+"_"+language_select
            rename_msi_file(driver, file, currentTestcaseName, testDeviceName)
            i = i + 1
        except:
            print("There is no language setting for this device")
            driver.close()
            break


def testcase10449():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    # Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver_windows(currentTestcaseName)
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
        config_allow_downgrade(driver)
        # Print the configured finish message
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
        currentTestcaseName = currentTestcaseName + "_" + selectedFW
        rename_msi_file(driver, file, currentTestcaseName, testDeviceName)
    else:
        print(testDeviceName + "just has 1 version in JX,so this case will pass")
        driver.close()

def run_windows_tests_in_threads():
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(testcase3961)
        executor.submit(testcase3965)
        executor.submit(testcase3966)
        executor.submit(testcase3965_32b)
        executor.submit(testcase3966_32b)
        executor.submit(testcase3968)
        executor.submit(testcase3969)
        executor.submit(testcase4090)
        executor.submit(testcase4090_32b)
        executor.submit(testcase4128_1)
        executor.submit(testcase4128_2)
        executor.submit(testcase4128_3)
        executor.submit(testcase4153_1)
        executor.submit(testcase4153_2)
        executor.submit(testcase4153_3)
        executor.submit(testcase5509)
        executor.submit(testcase5509_32b)
        executor.submit(testcase5664)
        executor.submit(testcase5664_32b)
        executor.submit(testcase5665)
        executor.submit(testcase5665_32b)
        executor.submit(testcase7195)
        executor.submit(testcase7196)
        executor.submit(testcase10312w)
        executor.submit(testcase10449)
        executor.submit(testcase10312w)
        print("Download start!")

def copy_files_to_folder(folder):
   #将子文件夹中的所有文件都复制到folder下后，删除子文件夹
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.msi') or file.endswith('html'):
                shutil.copy(os.path.join(root, file), folder)
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

if __name__ == '__main__':

    start_time = time.time()

    # Ask user what device to test, and save its name to the device.txt file
    test_device_name = input("Please input the device name: ")
    with open("../config/device.txt", "wt") as f:
        f.write(test_device_name)

    # run_linux_tests_in_threads()
    run_windows_tests_in_threads()

    time.sleep(3)
    print("Download finish!")
    #
    with open("../config/device.txt", "rt") as f:
        testDeviceName = f.read()

    with open("../config/saveDir.txt", "rt") as f:
        file = f.read()
        folder = file.replace('/', '\\') + '\\' + testDeviceName.replace("Jabra", "").replace(" ", "").lower()
        
    ## 下载完成后，folder下会有多个子文件夹，将子文件夹中的所有文件都复制到folder下，然后删除子文件夹
    copy_files_to_folder(folder)


    end_time = time.time()
    total_time = end_time - start_time
    # Transfer the time to minutes
    total_time = round(total_time / 60, 1)
    print("Test finish, the test run time is: "+ str(total_time))
