#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-06-15
# @Author : lei.X
import os
import requests
from bs4 import BeautifulSoup


'''
获取alexaTop 1000
'''

outputfilepath = os.path.abspath('.') + '/' + 'alexa1000.txt'  # 在当前文件夹下创建一个过渡性质的文件output.txt
f = open(outputfilepath, 'w+', encoding='utf-8')

url = 'https://blog.csdn.net/wizardforcel/article/details/82864060'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
response = requests.get(url, headers=header)
html = response.text
soup = BeautifulSoup(html, 'lxml')
list_footer = soup.find_all("tr")
for temp in list_footer:
    tempStr = temp.text
    strList = tempStr.split("\n")
    # print(strList)
    print(strList[1] + " " + strList[3])
    f.writelines(strList[1] + " " + strList[3] + "\n")
f.close()
