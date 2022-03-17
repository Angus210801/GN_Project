import os
import re
import winreg
import time
import zipfile
import requests
from sel_def_logger import MyLog
from tqdm import tqdm

my_logg = MyLog().logger
base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本号的正则表达式


def getChromeVersion():
    """通过注册表查询chrome版本"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前3位版本号
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


def getLatestChromeDriver(version):
    # 获取该chrome版本的最新driver版本号
    url = f"{base_url}LATEST_RELEASE_{version}"
    latest_version = requests.get(url).text
    my_logg.info('与当前chrome匹配的最新chromedriver版本为:%s',latest_version)
    # 下载chromedriver
    my_logg.info("开始下载chromedriver...")
    # url_tmp=f"{base_url}{latest_version}/"
    # print(url_tmp)
    download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
    file = requests.get(download_url,stream=True)
    content_size = int(file.headers['Content-Length']) / 1024
    with open("chromedriver.zip", 'wb') as zip_file:  # 保存文件到脚本所在目录
        for data in tqdm(iterable=file.iter_content(1024), total=content_size, unit='k', desc="chromedriver.zip"):
            zip_file.write(data)
    my_logg.info("下载完成.")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    my_logg.info("解压完成.")


def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    my_logg.info(f'当前chrome版本: {chrome_version}')
    driver_version = getChromeDriverVersion()
    my_logg.info(f'当前chromedriver版本: {driver_version}')
    if chrome_version == driver_version:
        my_logg.info("版本兼容，无需更新.")
        return
    my_logg.info("chromedriver版本与chrome浏览器不兼容，更新中>>>")
    try:
        getLatestChromeDriver(chrome_version)
        my_logg.info("chromedriver更新成功!")
    except requests.exceptions.Timeout:
        my_logg.error("chromedriver下载失败，请检查网络后重试！")
    except Exception as e:
        my_logg.error(f"chromedriver未知原因更新失败: {e}")


if __name__ == "__main__":
    checkChromeDriverUpdate()