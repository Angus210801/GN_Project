
# 创建记录log的函数用于记录log，并供其他模块调用

import logging

import os

import time

# 创建日志文件夹

def createLogFolder():

    if not os.path.exists("log"):
        os.mkdir("log")

# 创建日志文件

def createLogFile():

    # 创建日志文件夹

    createLogFolder()

    # 创建日志文件

    if not os.path.exists("log/log.txt"):
        with open("log/log.txt", "w") as f:
            f.write("")
    else:
        with open("log/log.txt", "a") as f:
            f.write(" ")

# 创建日志记录器

def createLogger():

    # 创建日志文件

    createLogFile()

    # 创建日志记录器

    logger = logging.getLogger()

    # 设置日志等级

    logger.setLevel(logging.DEBUG)

    # 创建日志处理器

    fh = logging.FileHandler("log/log.txt", encoding="utf-8")

    # 创建日志格式器

    fmt = "%(asctime)s - %(levelname)s - %(message)s"

    formatter = logging.Formatter(fmt)

    # 设置日志处理器的日志格式

    fh.setFormatter(formatter)

    # 将日志处理器添加到日志记录器中

    logger.addHandler(fh)

    return logger

# 记录日志

