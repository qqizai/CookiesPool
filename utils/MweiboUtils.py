#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 14:12
# @Author  : qizai
# @File    : mweiboUtils.py
# @Software: PyCharm
"""微博相关参数处理工具"""
import time
import random


def site_id(prefix: str)->str:
    """
    处理指定前缀/获取时间戳
    :param prefix:
    :return:
    """
    _id = str(int(time.time()*1000))+str(int(random.random()*100000))
    return prefix+_id if prefix is not None else _id




