#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 15:20
# @Author  : Aries
# @Site    : 
# @File    : eventdispatcher.py
# @Software: PyCharm
from EventDispatcherClass import EventDispatcher
from MyEvent import WhoAsk
from MyEvent import WhoRespond

dispatcher = EventDispatcher()
who_ask = WhoAsk( dispatcher )
who_responde1 = WhoRespond( dispatcher )
who_responde2 = WhoRespond( dispatcher )
# WhoAsk ask
who_ask.ask()