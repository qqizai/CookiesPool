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
        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/'
        self.profile_url = "https://m.weibo.cn/profile"  # 个人中心
        self.username = username
        self.password = password
        self.session = requests.session()

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

    def is_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            resp = self.session.get(url=self.profile_url, headers=self.headers)
            print(resp.text)
            print(resp.status_code)
            return (resp.status_code >= 200) and (resp.status_code < 300)
        except Exception as e:
            return False

    def get_login(self):
        new_time = str(int(time.time()))
        sign = new_time + '_' + hashlib.md5((self.username + self.password + new_time).encode("utf-8")).hexdigest()
        url = "https://appblog.sina.com.cn/api/passport/v3_1/login.php"
        data = {
            "cookie_format": "1",
            "sign": sign,
            "pin": "e3eb41c951f264a6daa16b6e4367e829",
            "appver": "5.3.2",
            "appkey": "2546563246",
            "phone": self.username,
            "entry": "app_blog",
            "pwd": self.password
        }

        resp = self.session.post(url=url, data=data, headers=self.headers)
        print(resp.text)
        try:
            result = json.loads(resp.text)
            return result["msg"]=="success"
        except:
            return False

    def main(self):
        """
        破解入口
        :return: cookie
        """
        # 初始化登录
        login_status = self.get_login()
        if not login_status:
            return {
                "status": 3,
                "content": "登录失败 - [login fail]",
            }

        # 检查是否登录成功
        if self.is_successfully():
            cookies = self.get_cookies()
            return {
                'status': 1,
                'content': cookies
            }
        else:
            return {
                "status": 3,
                "content": "登录失败 - [check fail]"
            }


if __name__ == '__main__':
    # # result = WeiboCookies('14773427930', 'x6pybpakq1').main()
    # result = WeiboCookies('1573372196@qq.com', '19960112LdZ').main()
    # print(result)
    # {"duration":256,"sign":"1589709475_30030559f70f59e9918adb65d7370276","dup_count":0,"err_count":1,"sso_return":"result=succ&uniqueid=2528335600&phone=&userid=1573372196%40qq.com&ag=4&displayname=%D0%C4%EC%60%B5%C4%B4%B0%91%F4&gender=1&birthday=1995-11-22&enrolltime=&name=1573372196%40qq.com&status=0&ac=2&showpincode=0&st=0&user_type=1&sub=_2A25zxXrzDeRxGeRL6VoS8yvKyzyIHXVu04k7rDV_PUJbkdANLVHXkWpNU1Zt8niK2MihzEX1f03uAAx03yvGY-kQ","sso_err":0,"sub":"_2A25zxXrzDeRxGeRL6VoS8yvKyzyIHXVu04k7rDV_PUJbkdANLVHXkWpNU1Zt8niK2MihzEX1f03uAAx03yvGY-kQ","err":0,"msg":"success","data":{"uid":"2528335600","cookie":{".sina.com.cn":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV_PUJbitANLW7ZkWtNU1Zt8optEIoaLoHmIlFnXHsARGx1g-nv; Path=\/; Domain=.sina.com.cn; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.sina.com.cn"],".sina.cn":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV9PUJbitANLUr-kWtNU1Zt8gRs9JsHATyHsUs4sys07UUK4z9Z; Path=\/; Domain=.sina.cn; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.sina.cn"],".weibo.com":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV8PUJbitANLUvukWtNU1Zt8o9ckkn_Acb_d8rhWB64OrnB6vPG; Path=\/; Domain=.weibo.com; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.com","SUHB=0HTwjdCJ2d97ci; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.com"],".weibo.cn":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV6PUJbitANLXjNkWtNU1Zt8jRuq6ckdCnCJqBkbXzFFo0EsUrn; Path=\/; Domain=.weibo.cn; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.cn","SUHB=0JvxQASyUZoR4W; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.cn"],"sina.com.cn":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV_PUJbitANLW7ZkWtNU1Zt8optEIoaLoHmIlFnXHsARGx1g-nv; Path=\/; Domain=.sina.com.cn; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.sina.com.cn"],"sina.cn":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV9PUJbitANLUr-kWtNU1Zt8gRs9JsHATyHsUs4sys07UUK4z9Z; Path=\/; Domain=.sina.cn; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.sina.cn"],"weibo.com":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV8PUJbitANLUvukWtNU1Zt8o9ckkn_Acb_d8rhWB64OrnB6vPG; Path=\/; Domain=.weibo.com; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.com","SUHB=0HTwjdCJ2d97ci; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.com"],"weibo.cn":["SUB=_2A25zxXrzDeRhGeRL6VoS8yvKyzyIHXVQmSC7rDV6PUJbitANLXjNkWtNU1Zt8jRuq6ckdCnCJqBkbXzFFo0EsUrn; Path=\/; Domain=.weibo.cn; HttpOnly; expires=Mon, 18-May-2020 06:57:55 GMT","SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5NHD95QESKzRe0efSo57Ws4Dqcj_i--fi-isiKn0i--4iKL2iKnRi--NiKLWiKnXi--Ni-8WiK.Ni--ciKnRi-zc; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.cn","SUHB=0JvxQASyUZoR4W; expires=Monday, 17-May-2021 09:57:55 GMT; path=\/; domain=.weibo.cn"]},"expire":1589781475},"time_stamp":1589709475}
    cookies = {
        'XSRF-TOKEN': 'f8ed60',
        'MLOGIN': '1',
        'M_WEIBOCN_PARAMS': 'uicode%3D20000174',
        'WEIBOCN_FROM': '1110005030',
        '_T_WM': '75389264703',
        'SUB': "_2A25zxXz6DeRhGeRL6VoS8yvKyzyIHXVRRgSyrDV6PUJbktANLUL-kW1NU1Zt8kioG9zhfjrM4HrtaOujCt0u1jXO",
        'SUBP': "0033WrSXqPxfM725Ws9jqgMF55529P9D9WWofOfe78QiPRCZNab0b.pw5JpX5K-hUgL.Fozfeon0e0-ceh52dJLoIpjLxK.L1-BLBoeLxK-L1hMLBK2LxK.LBK5L1h-t",
        'SUHB': "0JvxQASyUZoR4W",
    }





