import json
from flask import Flask, g
from cookiespool.config import GENERATOR_MAP
from cookiespool.db import RedisClient
from cookiespool.generator import WeiboCookiesGenerator


__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <h2>Welcome to Cookie Pool System</h2>
    <div>
        <table>
            <tr>
                <td>接口名字</td>
                <td>API</td>
            </tr>
            <tr>
                <td>获取随机的Cookie, 访问地址如 /<website>/random</td>
                <td><a href="/weibo/random" target="_blank">点击我进行获取一个随机Cookie</a></td>
            </tr>
            <tr>
                <td>添加用户, 访问地址如 /<website>/add/<username>/<password></td>
                <td><a href="/weibo/add/test@163.com/abc123" target="_blank">点击我进行添加账号密码：【test@163.com】【abc123】Cookie</a></td>
            </tr>
            <tr>
                <td>获取Cookies总数, 如 /<website>/count</td>
                <td><a href="/weibo/count" target="_blank">点击我进行获取微博的cookie总数Cookie</a></td>
            </tr>
        </table>
    </div>"""


def get_conn():
    """
    获取
    :return:
    """
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('RedisClient' + '("cookies", "' + website + '")'))
            setattr(g, website + '_accounts', eval('RedisClient' + '("accounts", "' + website + '")'))
    return g


@app.route('/<website>/random')
def random(website):
    """
    获取随机的Cookie, 访问地址如 /weibo/random
    :return: 随机Cookie
    """
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies


@app.route('/<website>/add/<username>/<password>')
def add(website, username, password):
    """
    添加用户, 访问地址如 /weibo/add/user/password
    :param website: 站点
    :param username: 用户名
    :param password: 密码
    :return: 
    """
    g = get_conn()
    print(f"添加新账号 username：{username} password：{password}")
    getattr(g, website + '_accounts').set(username, password)
    _cls = GENERATOR_MAP.get(website, "")
    if _cls:
        generator = eval(_cls + '(website="' + website + '")')
        generator.run()
    return json.dumps({'status': '1'})


@app.route('/<website>/count')
def count(website):
    """
    获取Cookies总数
    """
    g = get_conn()
    count = getattr(g, website + '_cookies').count()
    return json.dumps({'status': '1', 'count': count})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
