#-*-coding:utf8-*-

import requests
from lxml import etree
from factory import logger_factory
from multiprocessing.dummy import Pool



if __name__ == '__main__':
    LOGGER =logger_factory().get_logger('spider_jd')

    cook = {"Cookie": ""}
    url = 'https://m.jd.com/'
    html = requests.get(url).content
    html = str(html, 'utf-8')

    LOGGER.info(html)

    temp = requests.get(url, cookies=cook).content
    selector = etree.HTML(str(temp, 'utf-8'))
    # print(temp)
    # content = selector.xpath()
    # print(content)


