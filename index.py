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
        "/getstatus","getstatus",
        "/stop","stop"
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
        logging.info('connect function : connecting...')
        _status = False
        _frequency = 0
        data = web.input()
        if data.get('frequency'):
            _status = True
            _frequency = data.get('frequency')
            logging.info('connect & setting : set frequency is %s', _frequency)
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return render.connect(_status, _frequency)

class action:
    def GET(self):
        logging.info('action function :start receive action...')
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
            logging.info('receive action : mode is %s, result : status is %s, taskid is %s', _mode, _status, _taskid)
        else:
            logging.warning('receive action is wrong : mode is %s, [json]%s', _mode, (data.get('param')))
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return render.action(_mode, _taskid, _status)

class getstatus:
    def GET(self):
        logging.info('getstatus function :start get status...')
        _mode = 0
        _taskid = 0
        _code = 10004
        _error = "No Message"
        data = web.input()
        if((int(data.get('mode')) in modeArray) and (data.get('taskid') != "")):
            _mode = data.get('mode')
            _taskid = data.get('taskid')
            _code = 10001
            logging.info('get status : mode is %s, taskid is %s, result : code is %s, error is %s', _mode,_taskid, _code, _error)
            return render.getstatus(_mode, _taskid, _code, _error)

class stop:
    def GET(self):
        logging.info('stop function :stop init...')
        _mode = 0
        _taskid = 0
        _code = 10000
        _error = "No Message"
        data = web.input()
        if ((int(data.get('mode')) in modeArray) and (data.get('taskid') != "")):
            _mode = data.get('mode')
            _taskid = data.get('taskid')
            _code = 10001
            logging.info('stop : mode is %s, taskid is %s, result : code is %s, error is %s', _mode, _taskid, _code, _error)
            return render.getstatus(_mode, _taskid, _code, _error)


app = web.application(urls, globals())
app.notfound = notfound
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()