#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 15:45
# @Author  : Aries
# @Site    : 
# @File    : carServer.py
# @Software: PyCharm

from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  return environ['PATH_INFO'][1:]

httpd = make_server('127.0.0.1', 8082, simple_app)
httpd.serve_forever()