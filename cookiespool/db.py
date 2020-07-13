import json
import random
import redis
from cookiespool.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class RedisClient(object):
    def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化Redis连接
        :param host: 地址
        :param port: 端口
        :param password: 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.type = type
        self.website = website

    def name(self):
        """
        获取Hash的名称
        :return: Hash名称
        """
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        """
        设置键值对
        :param username: 用户名
        :param value: 密码或Cookies
        :return:
        """
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        """
        根据键名获取键值
        :param username: 用户名
        :return:
        """
        return self.db.hget(self.name(), username)

    def delete(self, username):
        """
        根据键名删除键值对
        :param username: 用户名
        :return: 删除结果
        """
        return self.db.hdel(self.name(), username)

    def count(self):
        """
        获取数目
        :return: 数目
        """
        return self.db.hlen(self.name())

    def random(self):
        """
        随机得到键值，用于随机Cookies获取
        :return: 随机Cookies
        """
        cookie_list = self.db.hvals(self.name())
        return random.choice(cookie_list) if cookie_list else ""

    def usernames(self):
        """
        获取所有账户信息
        :return: 所有用户名
        """
        return self.db.hkeys(self.name())

    def all(self):
        """
        获取所有键值对
        :return: 用户名和密码或Cookies的映射表
        """
        return self.db.hgetall(self.name())


if __name__ == '__main__':
    # 添加账号
    conn = RedisClient('accounts', 'weibo')
    result = conn.set('hell2o', 'sss3s')
    print(result)

    # 添加cookies
    # cookie_db = RedisClient('cookies', 'weibo')
    # cookies = {'XSRF-TOKEN': '234309', '_T_WM': '31149364869', 'ALF': '1592889350', 'M_WEIBOCN_PARAMS': 'oid%3D4505609644905372%26luicode%3D10000011%26lfid%3D102803_ctg1_5188_-_ctg1_5188%26uicode%3D20000174', 'MLOGIN': '1', 'SCF': 'Aq5BmMlr5db8fW0DgBQ2SmoDOZKr94vR4IH3RqrRZ3sDJCzSKZSfSj_69lGyzgIQ1Y7hiiBQrx4LqNuo62NQLzM.', 'SSOLoginState': '1590297350', 'SUB': '_2A25zznNWDeRhGeBK4lAZ9i7LzTyIHXVRMR0erDV6PUJbktANLXXtkW1NRx0c-R-fMOfxrNlsSJv3TBVuW6b2st_Z', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4z1Vq87klgAsYrZ4q2i3P5JpX5KzhUgL.FoqX1KzRSo5NSo52dJLoIp.LxKqL1-zLBo.LxKBLB.BLBoSZqg4Dqc-_', 'SUHB': '0jBIcMRciCrsEj', 'WEIBOCN_FROM': '1110006030'}
    # result = cookie_db.set("17057850969", json.dumps(cookies))
    # print(result)

    # cookies = {'XSRF-TOKEN': 'af46d0', '_T_WM': '31149364869', 'ALF': '1592889350', 'M_WEIBOCN_PARAMS': 'oid%3D4505609644905372%26lfid%3D102803_ctg1_5188_-_ctg1_5188%26luicode%3D20000174%26uicode%3D20000174', 'MLOGIN': '1', 'SCF': 'Aq5BmMlr5db8fW0DgBQ2SmoDOZKr94vR4IH3RqrRZ3sD9Nd2kxpnDpxJljStwwm7i7pEIsKuBMxCiIbrtI2UY0g.', 'SSOLoginState': '1590300626', 'SUB': '_2A25zzn-CDeRhGeFK7lQS9SnKzz2IHXVRMQHKrDV6PUJbktAKLU-jkW1NQytPZGidl15UfXzZVQ8BqaNPAN9Wv3B3', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWrJmS59NkQ2IGE8mjo4S-p5JpX5KzhUgL.FoMXSKq0SKMcSh22dJLoIEBLxK-LBonL1heLxK-L1K5L1h.LxK-LBK.L1h.LxK-L1hBLB.qt', 'SUHB': '0C1C6t1JMng5a5', 'WEIBOCN_FROM': '1110006030'}
    # result = cookie_db.set("0017209233072", json.dumps(cookies))
    # print(result)

