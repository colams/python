# -*-coding:utf8-*-

import requests
from JD_crawl import JD_crawl
from factory import logger_factory
from lxml import etree


def get_html(url):
    jd_crawl = JD_crawl()
    html = requests.get(url, headers=jd_crawl.headers).content
    print(html)
    return str(html, 'GBK')


def get_response(url):
    cookie = {"Cookie": ""}
    response = requests.post(url)
    return response


def get_data():
    html = get_html('https://passport.jd.com/new/login.aspx')
    print(html)
    selector = etree.HTML(html)
    content = selector.xpath('//input[@type="hidden"]')
    dict = {}
    for i in range(len(content)):
        dict[i] = content[i].attrib
        print(dict[i])
    return content


def main_local():
    logger = logger_factory().get_logger('spider_jd')
    url = 'https://plogin.m.jd.com/cgi-bin/m/domlogin'
    html = get_html(url)
    logger.info(html)

def main():
    un = input('请输入京东账号：')
    pwd = input('请输入京东密码：')
    jd = JD_crawl(un, pwd)
    jd.login()
    jd.shopping()




if __name__ == '__main__':
    # main()
    get_data()
