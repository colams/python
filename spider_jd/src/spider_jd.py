#-*-coding:utf8-*-

import requests
from factory import logger_factory

from lxml import etree
from multiprocessing.dummy import Pool

if __name__ == '__main__':
    LOGGER =logger_factory().get_logger('spider_jd')

    cook = {"Cookie": ""}
    url = 'https://m.jd.com/'
    #html = requests.get(url).content
    response = requests.post(url)

    html = str(response.content, 'utf-8')

    LOGGER.info(html)



