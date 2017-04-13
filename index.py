#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/5 10:58
# @Author  : Aries
# @Site    : 
# @File    : index.py.py
# @Software: PyCharm
# git pull origin master

import web
#import GPIOControl
import logging
import logging.config
import os

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

#controller = GPIOControl.GPIOController()

urls = ("/", "hello",
        "/connect", "connect"
        )  # 指定任何url都指向hello类

app = web.application(urls, globals())
application = app.wsgifunc()
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

# 定义相应类
class hello:
    def GET(self):
        logging.info('web service root.')
        return "web service root"

class connect:
    def GET(self):
        _status = False
        _frequency = 0
        data = web.input()
        _frequency = data.get('frequency')
        if _frequency:
            _status = True
        web.header('Content-Type', 'text/json')
        return render.connect(_status, _frequency)

if __name__ == "__main__":
    app.run()