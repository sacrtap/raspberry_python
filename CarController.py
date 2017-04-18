#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 15:19
# @Author  : Aries
# @Site    : 
# @File    : CarController.py
# @Software: PyCharm

import logging
import logging.config

class basicConfig:
    def __init__(self, _mode, _frequency):
        self.mode = _mode
        self.frequency = _frequency

    def getMode(self):
        return self.mode

    def getFrequency(self):
        return self.frequency

