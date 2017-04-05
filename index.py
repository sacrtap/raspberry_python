#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/5 10:58
# @Author  : Aries
# @Site    : 
# @File    : index.py.py
# @Software: PyCharm
# git pull origin master

import web

urls = ("/.*", "hello")  # 指定任何url都指向hello类
app = web.application(urls, globals())  # 绑定url

# 定义相应类
class hello:
    def GET(self):
        return 'Hello, world!'

if __name__ == "__main__":
    app.run()