#!/usr/bin/env python
# -*- coding: utf-8 -*
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
import CarController

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

modeArray = [1, 2, 3] # 自由、预设、轨迹

at = CarController.ActionTranslate()

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

# 定义相应类
class hello:
    def GET(self):
        logging.info('web service started.')
        return "web service started"


class connect:
    def POST(self):
        logging.info('connect function : connecting...')
        _status = False
        _frequency = 0
        data = web.input()
        if data.get('frequency'):
            _status = True
            _frequency = int(data.get('frequency'))
            CarController.BasicConfig(_frequency) # 设置命令发送频率
            logging.info('connect & setting : set frequency is %s', _frequency)
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return render.connect(_status, _frequency)

class action:
    def POST(self):
        logging.info('action function :start receive action...')
        _mode = 0
        _json = None
        _status = False
        data = web.input()
        if ((int(data.get('mode')) in modeArray) and (data.get('param') != "")):
            _mode = data.get('mode')
            _json = data.get('param')
            at.setParam(_mode, _json)
            _status = at.TransByMode()
            logging.info('receive action : mode is %s, result : status is %s', _mode, _status)
        else:
            logging.warning('receive action is wrong : mode is %s, [json]%s', _mode, (data.get('param')))
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return render.action(_mode, _status)

class getstatus:
    def POST(self):
        logging.info('getstatus function :start get status...')
        _error = "No Message"
        _code = 10002
        if at.getStatus() :
            _code = at.getCode()
        logging.info('get status result : code is %s, error is %s', _code, _error)
        return render.getstatus(_code, _error)

class stop:
    def POST(self):
        logging.info('stop function :stop init...')
        _code = 10006
        _error = "No Message"
        if at.getStatus() :
            _code = at.getCode()
        logging.info('stop result : code is %s, error is %s',_code, _error)
        return render.getstatus(_code, _error)


app = web.application(urls, globals())
app.notfound = notfound
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()