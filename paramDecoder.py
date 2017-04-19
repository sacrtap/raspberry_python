#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/19 10:58
# @Author  : Aries
# @Site    : 
# @File    : paramDecoder.py
# @Software: PyCharm

import json

class FreeDecoder:
    def __init__(self, _json):
        self.jsonParam = json.loads(_json)

    def getDirection(self):
        return self.jsonParam["direction"]

    def getSpeed(self):
        return self.jsonParam["speed"]

