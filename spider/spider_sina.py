#-*-coding:utf8-*-

import requests
from lxml import etree
from multiprocessing.dummy import Pool

cook = {"Cookie":""}
url = 'http://weibo.cn/u/1890493665'
html = requests.get(url).content
print(html)

html1 = requests.get(url,cookies=cook).content
selector = etree.HTML(html1)
print(html1)
content = selector.xpath()
print(content)