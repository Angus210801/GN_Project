import os
import re
import time
import winreg
import zipfile
import requests
from Common.sel_def_logger import MyLog

my_logg = MyLog().logger
base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*.\d*')  # 匹配前4位版本号的正则表达式


def getChromeVersion():
    """通过注册表查询chrome版本"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        version = ".".join(value.split(".")[:-1])
        return version  # 返回前4位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return "1.1.1"


def getChromeDriverVersion():
    """查询Chromedriver版本"""
    outstd2 = os.popen('chromedriver --version').read()
    try:
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"
def onefloat(num):
    return '{:.1f}'.format(num)

def getLatestChromeDriver(version):
    # 获取该chrome版本的最新driver版本号
    version_tmp = ".".join(version.split(".")[:-1])
    print(version_tmp)
    url = f"{base_url}LATEST_RELEASE_{version_tmp}"
    latest_version = requests.get(url).text
    my_logg.info('The latest Chrome Driver version matches the current Chrome:%s',latest_version)
    # 下载chromedriver
    my_logg.info("Start Downloading chromedriver...")
    # url_tmp=f"{base_url}{latest_version}/"
    # print(url_tmp)
    download_url = f"{base_url}{version}/chromedriver_win32.zip"
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
            if time.time() - start_time > 1:
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
    print("100%,downloaded!")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    print("Unzip successfully")


def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    my_logg.info(f'Current Chrome Version: {chrome_version}')
    driver_version = getChromeDriverVersion()
    my_logg.info(f'Current chromedriver Version: {driver_version}')
    if chrome_version == driver_version:
        print("Same Version,No need to update")
        my_logg.info("Same Version,No need to update")
        print("\n")
        print("Click the bottom button to selece the location that the test package should save.")
        return
    my_logg.info("Lower Version for chromedriver version,updating")
    try:
        getLatestChromeDriver(chrome_version)
        my_logg.info("Chromedriver Updated successfully!")
    except requests.exceptions.Timeout:
        my_logg.error("Chromedriver Download Failed,Check The Internet Connection And Try Again")
    except Exception as e:
        my_logg.error(f"Chromedriver Download Failed For Unknown Reason: {e}")

if __name__ == "__main__":
    checkChromeDriverUpdate()