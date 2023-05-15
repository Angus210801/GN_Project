import time

from test_scripts.testcase_action import *
import threading
from concurrent.futures import ThreadPoolExecutor
import os
import shutil


def testcase6098():
    """ 6098: JX-ThinC: Verify zip package content and JXDU version by creating a ZIP file."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Go to select firmware page
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase6134():
    """ 6134: JX-ThinC: All device settings and FW set to "Leave Unchange", all settings set to Protected."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure protect as yes
    config_the_protect_as_yes(driver)
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase7551():
    """ 7551: JX-ThinC: Install a ZIP file on end user environment with a later FW and set all settings are changed."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as random
    config_settings_as_random(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase7551p():
    """ 7551: JX-ThinC: Install a ZIP file on end user environment with a later FW and set all settings are changed."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_FW_as_lower_than_latest(driver)
    # Configure all settings as random
    config_settings_as_random(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase7555():
    """ 7555:JX-ThinC: Install a ZIP file on end user environment with a later FW and no setting change. """
    # Configure the basic function
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Go to select firmware page
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(testDeviceName,currentTestcaseName )
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase7555p():
    """ 7555p:JX-ThinC: Prepare package for the 7555p. """
    # Configure the basic function
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Go to select firmware page
    config_the_FW_as_lower_than_latest(driver)
    # Print configure finish
    print_the_config_finish(testDeviceName,currentTestcaseName )
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)


def testcase7556():
    """ 7556: JX-ThinC: Install a ZIP file on end user environment with a later FW and set all settings set to default."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    settings_default(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase7556p():
    """ 7556p:prepare package for 7556 JX-ThinC: Install a ZIP file on end user environment with a old FW and set all settings set not default value."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_settings_as_not_default(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)


def testcase7692():
    """JX-ThinC: All settings in the device can be changed from default value to min. value with installation of .zip file at the end user PC, no FW change."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_settings_as_Min(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase7695():
    """JX-ThinC: All settings in the device can be changed from default value to max. value with installation of .zip file at the end user PC, no FW change."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_settings_as_MAX(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)


def testcase10312l():
    i=1
    while i<=6:
        # Get current function name
        currentTestcaseName = sys._getframe().f_code.co_name
        driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
        # Go to select device page
        linuxtrack.click_next_button()
        # Input device name
        linuxtrack.select_device()
        # Configure the latest FW
        config_the_latest_FW(driver)


        #判断是否存在Language setting
        try:
            language_region_select = driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionId']")
            Select(language_region_select).select_by_index("1")
            language_select=driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionLanguageId']")
            languageList=Select(language_select)
            languageNum=len(languageList.options)
            Select(language_select).select_by_index(i)
            language_select=Select(language_select).first_selected_option.text
            # Print configure finish
            currentTestcaseName=currentTestcaseName+language_select
            print_the_config_finish(currentTestcaseName, testDeviceName)
            # Download summary
            goto_summary_page_and_download(driver)
            # Rename summary file
            rename_summary(currentTestcaseName, file, testDeviceName)
            # Go to download page
            action_download_zip_file(driver)
            # Download zip file and rename
            rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


        except:
            print("There is no language setting for this device")
            driver.close()
            break


def testcase16990():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()

    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_allow_downgrade(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def testcase16991():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_settings_as_Min(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName,file,testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver,file,currentTestcaseName,testDeviceName)

def run_linux_tests_in_threads():
    with ThreadPoolExecutor(max_workers=4) as executor:
        # executor.submit(testcase10312l)
        executor.submit(testcase6098)
        executor.submit(testcase6134)
        executor.submit(testcase16990)
        executor.submit(testcase16991)
        executor.submit(testcase7551)
        executor.submit(testcase7555)
        executor.submit(testcase7556)
        executor.submit(testcase7692)
        executor.submit(testcase7695)
        executor.submit(testcase7551p)
        executor.submit(testcase7555p)
        executor.submit(testcase7556p)

if __name__ == '__main__':

    # run_linux_tests_in_threads()
    run_linux_tests_in_threads()

    time.sleep(3)
    #
    with open("../config/device.txt", "rt") as f:
        testDeviceName = f.read()

    with open("../config/saveDir.txt", "rt") as f:
        file = f.read()
        folder = file.replace('/', '\\') + '\\' + testDeviceName

    for root, dirs, files in os.walk(folder):
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            for subroot, subdirs, subfiles in os.walk(subdir_path):
                for subfile in subfiles:
                    src_file = os.path.join(subroot, subfile)
                    dst_file = os.path.join(folder, subfile)
                    shutil.move(src_file, dst_file)
                for subsubdir in subdirs:
                    src_dir = os.path.join(subroot, subsubdir)
                    dst_dir = os.path.join(folder, subsubdir)
                    shutil.move(src_dir, dst_dir)
            shutil.rmtree(subdir_path)
