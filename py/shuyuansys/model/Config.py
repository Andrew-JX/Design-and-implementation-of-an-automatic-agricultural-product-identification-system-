
import os
import re
import sys


class Config:
    systemxh = ""  # 本程序配置序号

    chromediv = ""
    chromedriverdiv = ""

    # 数据库
    host = '',
    port = 3306,
    user = '',
    password = '',
    db = '',
    # --

    def __init__(self):
        configdir = os.getcwd() + "/config.txt"
        with open(configdir, "r") as f:
            data = f.readlines()
            self.systemxh = data[0].replace("\n", "")

            self.chromediv = data[1].replace("\n", "")
            self.chromedriverdiv = data[2].replace("\n", "")

            self.host = data[3].replace("\n", "")
            self.port = data[4].replace("\n", "")
            self.user = data[5].replace("\n", "")
            self.password = data[6].replace("\n", "")
            self.db = data[7].replace("\n", "")