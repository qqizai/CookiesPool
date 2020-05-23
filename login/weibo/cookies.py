#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 16:51
# @Author  : qizai
# @File    : cookies.py
# @Software: PyCharm

import json
import time
import hashlib
import requests


class WeiboCookies():
    def __init__(self, username, password):
        self.login_url = 'https://passport.weibo.cn/sso/login'
        self.username = username
        self.password = password
        self.session = requests.Session()

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; nxt-al10 Build/LYZ28N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 sinablog-android/5.3.2 (Android 5.1.1; zh_CN; huawei nxt-al10/nxt-al10)",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }

    def get_cookies(self):
        """
        获取Cookies
        :return:
        """
        return self.session.cookies.get_dict()

    def login(self):
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
            "username": self.username,
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
            "password": self.password,
            "mainpageflag": "1",
            "hff": ""
        }

        res = self.session.post(self.login_url, headers=headers, data=data)
        try:
            ajson = json.loads(res.text)
        except:
            ajson = {}

        if ajson and ajson["retcode"]==20000000 and ajson["data"].get("uid", 0)!=0:
            print("登录成功，resp: {}".format(res.text))
            ajson["status"] = 1
        else:
            ajson["status"] = 0
        return ajson

    def main(self):
        """
        破解入口
        :return: cookie
        """
        # 初始化登录
        status = self.login()
        # 检查是否登录成功
        if status["status"]==1:
            cookies = self.get_cookies()
            return {
                "status": 1,
                "content": cookies,
                "msg": "",
                "username": self.username,
            }
        elif status["status"]==0:
            return {
                "status": 2,
                "content": "{}".format(status.get("msg", "其他错误")),
                "msg": "{}".format(status.get("msg", "其他错误")),
                "username": self.username,
            }


if __name__ == '__main__':
    result = WeiboCookies('14773427930', 'x6pybpakq1').main()
    # result = WeiboCookies('3711963257@qq.com', '').main()
    print(result)





