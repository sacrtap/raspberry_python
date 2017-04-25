#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/19 10:58
# @Author  : Aries
# @Site    : 
# @File    : paramDecoder.py
# @Software: PyCharm

import json
import logging
import logging.config

class FreeDecoder:
    def __init__(self, _json):
        self.jsonParam = json.loads(_json)

    def getDirection(self):
        return int(self.jsonParam["direction"])

    def getSpeed(self):
        return int(self.jsonParam["speed"])

class PresetDecoder:
    def __init__(self, _json):
        self.jsonParam = json.loads(_json)

    def getList(self):
        return self.jsonParam["list"]

    def getDirection(self, _r):
        return int(_r["direction"])

    def getSpeed(self, _r):
        return int(_r["speed"])

    def getDistance(self, _r):
        try:
            if(int(_r["distance"])):
                return int(_r["distance"])
            else:
                return 0
        except Exception, e:
            logging.warning('getDistance is warning: %s', e)
            return 0


    def getDuration(self, _r):
        try:
            if(int(_r["duration"])):
                return int(_r["duration"])
            else:
                return 0
        except Exception, e:
            logging.warning('getDuration is warning: %s', e)
            return 0