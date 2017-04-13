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
        "/connect", "connect",
        "/action","action",
        "/getstatus",'getstatus'
        )  # 指定任何url都指向hello类

web.config.debug = True

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

modeArray = [1, 2, 3]

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

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
        if data.get('frequency'):
            _status = True
            _frequency = data.get('frequency')
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return render.connect(_status, _frequency)

class action:
    def GET(self):
        _mode = 0
        _json = None
        _taskid = 0
        _status = False
        data = web.input()
        if ((int(data.get('mode')) in modeArray) and (data.get('param') != "")):
            _mode = data.get('mode')
            _json = data.get('param')
            _status = True
            _taskid = 10001

        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return render.action(_mode, _taskid, _status)

class getstatus:
    def GET(self):
        _mode = 0
        _taskid = 0
        _code = 10004
        _error = "no message"
        data = web.input()
        if((int(data.get('mode')) in modeArray) and (data.get('taskid') != "")):
            return render.getstatus(data.get('mode'), data.get('taskid'), _code, _error)


app = web.application(urls, globals())
app.notfound = notfound
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()