#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/5 10:58
# @Author  : Aries
# @Site    : 
# @File    : index.py.py
# @Software: PyCharm
# git pull origin master

import web
import GPIOControl
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='debug.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

urls = ("/.*", "hello")  # 指定任何url都指向hello类
app = web.application(urls, globals())  # 绑定url

# 定义相应类
class hello:
    def GET(self):
        logging.info('web service is ok.')
        return "hello"

if __name__ == "__main__":
    app.run()