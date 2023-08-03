"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : testcase_chromedriver_update
#
#                   @Programmer   : Ella
#
#                   @Start Date   : 2022/03/25
#
#                   @Last Update  : 2022/12/23
#
#                   @Note: This is for the chromedriver update.
#-------------------------------------------------------------------
"""

import os
import re
import winreg
import zipfile
import time
import requests

base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本号的正则表达式

def onefloat(num):
    return '{:.1f}'.format(num)

def getChromeVersion():
    """通过注册表查询chrome版本"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前3位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return "1.1.1"


def get_chromedriver_version():
    """查询当前目录下的chromedriver版本"""
    try:
        outstd2 = os.popen('chromedriver --version').read()
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"

def getLatestChromeDriver(version):
    # Get the newest chromedrive version from website
    url = f"{base_url}LATEST_RELEASE_{version}"
    latest_version = requests.get(url).text
    print(f"    The latest Chrome Driver version matches the current Chrome:{latest_version}")
    # 下载chromedriver
    print("     Start Downloading chromedriver...")
    download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
    with requests.get(download_url,stream=True) as file, open(r'chromedriver.zip', 'wb') as zip_file:# 保存文件到脚本所在目录
        total_size = int(file.headers['content-length'])
        # 请求文件的大小单位字节B
        total_size = int(file.headers['content-length'])
        # 以下载的字节大小
        content_size = 0
        # 进度下载完成的百分比
        plan = 0
        # 请求开始的时间
        start_time = time.time()
        # 上秒的下载大小
        temp_size = 0
        # 开始下载每次请求1024字节
        for content in file.iter_content(chunk_size=1024):
            zip_file.write(content)
            # 统计以下载大小
            content_size += len(content)
            # 计算下载进度
            plan = (content_size / total_size) * 100
            # 每一秒统计一次下载量
            if time.time() - start_time > 2:
                # 重置开始时间
                start_time = time.time()
                # 每秒的下载量
                speed = content_size - temp_size
                # KB级下载速度处理
                if 0 <= speed < (1024 ** 2):
                    print('\r',onefloat(plan), '%', onefloat(speed / 1024), 'KB/s', end='')
                # MB级下载速度处理
                elif (1024 ** 2) <= speed < (1024 ** 3):
                    print('\r', onefloat(plan), '%', onefloat(speed / (1024 ** 2)), 'MB/s', end='')
                # 重置以下载大小
                temp_size = content_size
    print('\n')
    print(" 100%,downloaded!")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    print(" Unzip successfully")
    # 删除压缩包
    os.remove("chromedriver.zip")



def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    print(f'        Current Chrome Version: {chrome_version}')
    driver_version = get_chromedriver_version()
    print(f'        Current chromedriver Version: {driver_version}')
    if chrome_version == driver_version:
        print("     Same Version,No need to update.")
        if os.path.exists("LICENSE.chromedriver"):
            os.remove("LICENSE.chromedriver")
        if os.path.exists("chromedriver.zip"):
            os.remove("chromedriver.zip")
        return


    print("   Lower Version for chromedriver version,updating>>>")

    try:
        getLatestChromeDriver(chrome_version)
        print("chromedriver Updated successfully!")
    except requests.exceptions.Timeout:
        print("Chromedriver Download Failed,Check The Network Connection And Try Again")
    except Exception as e:
        print(f"Chromedriver Download Failed For Unknown Reason: {e}")

    #判断是否存在LICENSE.chromedriver文件，如果存在则删除


#
if __name__ == "__main__":
    checkChromeDriverUpdate()
