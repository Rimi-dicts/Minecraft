from time import sleep

import requests
from bs4 import BeautifulSoup


def getSoup(url: str):
    sleep(1)
    html = requests.get(url, "lxml")
    html.encoding = "utf-8"
    return BeautifulSoup(html.text, features="lxml")


class Downloader:
    def __init__(self, fp):
        self.outFile = open(fp, "w", encoding="utf-8")

    def getAll(self):
        self.getChineseName()
        self.outFile.close()

    def getChineseName(self):
        resList = (
            getSoup("https://zh.minecraft.wiki/w/Minecraft_Wiki:%E8%AF%91%E5%90%8D%E6%A0%87%E5%87%86%E5%8C%96")
            .select("#mw-content-text > div.mw-parser-output > table > tbody > tr > td:nth-child(3)"))

        print("获取标准译名列表完毕")
        self.outFile.write("# 标准译名列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))
