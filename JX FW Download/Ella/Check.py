import os
import re
import winreg
import zipfile
import requests
from sel_def_logger import MyLog
from tqdm import tqdm

my_logg = MyLog().logger
base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*.\d*')  # 匹配前4位版本号的正则表达式


def getChromeVersion():
    """通过注册表查询chrome版本"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前4位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return "1.1.1"


def getChromeDriverVersion():
    """查询Chromedriver版本"""
    outstd2 = os.popen('chromedriver --version').read()
    try:
        version = outstd2.split(' ')[1]
        return version
    except Exception as e:
        return "0.0.0"


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
    print(download_url)
    file = requests.get(download_url,stream=True)
    content_size = int(file.headers['Content-Length']) / 1024
    with open("chromedriver.zip", 'wb') as zip_file:  # 保存文件到脚本所在目录
        for data in tqdm(iterable=file.iter_content(1024), total=content_size, unit='k', desc="chromedriver.zip"):
            zip_file.write(data)
    my_logg.info("Download successfully")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    my_logg.info("Unzip completed")


def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    my_logg.info(f'Current Chrome Version: {chrome_version}')
    driver_version = getChromeDriverVersion()
    my_logg.info(f'Current chromedriver Version: {driver_version}')
    if chrome_version == driver_version:
        my_logg.info("Same Version,No need to update")
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