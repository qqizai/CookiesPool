#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 17:02
# @Author  : qizai
# @File    : temp.py
# @Software: PyCharm

# 登录新浪微博
import os
import re
import time
import random
import cchardet
import requests
from lxml import etree


# 登录
def login(url, username, password):
    headers = {
        "Origin": "https://passport.weibo.cn",
        "Content-Length": "169",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Host": "passport.weibo.cn",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Connection": "keep-alive",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "qq": "",
        "savestate": "1",
        "client_id": "",
        "wentry": "",
        "code": "",
        "ec": "0",
        "r": "http://weibo.cn/",
        "loginfrom": "",
        "hfp": "",
        "pagerefer": "",
        "entry": "mweibo",
        "password": password,
        "mainpageflag": "1",
        "hff": ""
    }

    s = requests.Session()
    res = s.post(url, headers=headers, data=data)
    print(res.text)
    print('login state:', res)
    print(res.status_code)
    print(res.cookies.get_dict())
    print(res.cookies)
    return s


def main():
    login_url = 'https://passport.weibo.cn/sso/login'
    username = '545897643@qq.com'
    password = ''

    s = login(login_url, username, password)

    # fans_url='https://weibo.cn/5822306215/fans'
    # fans_url='https://weibo.cn/5822306215/follow'
    # get_fans(s,fans_url)


if __name__ == '__main__':
    main()




