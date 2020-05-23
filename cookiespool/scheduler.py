import time
import traceback
from multiprocessing import Process

from cookiespool.api import app
from cookiespool.config import CYCLE, TESTER_MAP, API_PORT, API_HOST, API_PROCESS, GENERATOR_PROCESS, VALID_PROCESS
from cookiespool.config import GENERATOR_MAP
from cookiespool.tester import WeiboValidTester
from cookiespool.generator import WeiboCookiesGenerator


class Scheduler(object):
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print('Cookies检测进程开始运行')
            try:
                for website, cls in TESTER_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    tester.run()
                    print('Cookies检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)
                print(traceback.format_exc())
    
    @staticmethod
    def generate_cookie(cycle=CYCLE):
        while True:
            print('Cookies生成进程开始运行')
            try:
                for website, cls in GENERATOR_MAP.items():
                    generator = eval(cls + '(website="' + website + '")')
                    generator.run()
                    print('Cookies生成完成')
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)
                print(traceback.format_exc())

    @staticmethod
    def api():
        print('API接口开始运行')
        app.run(host=API_HOST, port=API_PORT)
    
    def run(self):
        # API服务运行
        if API_PROCESS:
            api_process = Process(target=Scheduler.api)
            api_process.start()

        # 自动检测新添加的账号及生成cookie服务
        if GENERATOR_PROCESS:
            generate_process = Process(target=Scheduler.generate_cookie)
            generate_process.start()

        # 检查cookie是否有效服务
        if VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()
