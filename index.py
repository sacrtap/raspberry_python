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
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

controller = GPIOControl.GPIOController()

urls = ("/.*", "hello",
        "/runForward","runForward"
        )  # 指定任何url都指向hello类
app = web.application(urls, globals())  # 绑定url

# 定义相应类
class hello:
    def GET(self):
        logging.info('web service is connected.')
        return "hello"

class runForward:
    def GET(self):
        controller.runForward(50)

if __name__ == "__main__":
    app.run()