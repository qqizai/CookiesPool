#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:11
# @Author  : qizai
# @File    : StrUtils.py
# @Software: PyCharm
"""字符串处理工具类"""

import base64
from urllib.parse import quote, unquote


def str2b64(string: str)->str:
    """
    字符串转base64
    :param string: 源字符串
    :return: base64编码的字符串
    """
    return base64.b64encode(string.encode("utf8")).decode()


if __name__ == '__main__':
    print(str2b64("abc%40123.com"))
    print(quote("https://blog.csdn.net/"))
    print(unquote("https%3A//blog.csdn.net/"))
    print(unquote("abc%40123.com"))
    pass



