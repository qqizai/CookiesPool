import json
from cookiespool.db import RedisClient
from login.weibo.cookies import WeiboCookies


class CookiesGenerator(object):
    def __init__(self, website='default'):
        """
        父类, 初始化一些对象
        :param website: 名称
        :param browser: 浏览器, 若不使用浏览器则可设置为 None
        """
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def new_cookies(self, username, password):
        """
        新生成Cookies，子类一定需要重写
        :param username: 用户名
        :param password: 密码
        :return:
        """
        raise NotImplementedError
    
    def process_cookies(self, cookies):
        """
        处理Cookies
        :param cookies:
        :return:
        """
        dict = {}
        for cookie in cookies:
            dict[cookie['name']] = cookie['value']
        return dict
    
    def run(self):
        """
        运行, 得到所有账户, 然后顺次模拟登录
        :return:
        """
        accounts_usernames = self.accounts_db.usernames()
        cookies_usernames = self.cookies_db.usernames()
        
        for username in accounts_usernames:
            if not username in cookies_usernames:
                password = self.accounts_db.get(username)
                print('正在生成Cookies', '账号', username, '密码', password)
                result = self.new_cookies(username, password)
                # 成功获取
                if result.get('status') == 1:
                    # cookies = self.process_cookies(result.get('content'))
                    cookies = result.get('content')
                    print('成功获取到Cookies', cookies)
                    if self.cookies_db.set(username, json.dumps(cookies)):
                        print('成功保存Cookies')
                # 密码错误，移除账号
                elif result.get('status') == 2:
                    print("reason: {}".format(result.get('content')))
                    if self.accounts_db.delete(username):
                        print('成功删除账号: {}'.format(username))
                else:
                    print("其他错误: {}".format(result.get('content')))
        else:
            print('所有账号都已经成功获取Cookies')
    

class WeiboCookiesGenerator(CookiesGenerator):
    def __init__(self, website='weibo'):
        """
        初始化操作
        :param website: 站点名称
        """
        CookiesGenerator.__init__(self, website)
        self.website = website
    
    def new_cookies(self, username, password):
        """
        生成Cookies
        :param username: 用户名
        :param password: 密码
        :return: 用户名和Cookies
        """
        return WeiboCookies(username, password).main()


if __name__ == '__main__':
    generator = WeiboCookiesGenerator()
    generator.run()
