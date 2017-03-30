#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 14:07
# @Author  : Aries
# @Site    : 
# @File    : EventClass.py
# @Software: PyCharm

class Event(object):
    """
    用于事件分发
    """
    def __init__(self, event_type, data=None):
        """
        定义event的类型和数据
        :param event_type: 监听事件类型
        :param data: 事件数据
        """
        self._type = event_type
        self._data = data

    @property
    def type(self):
        """
        返回event类型
        """
        return self._type

    @property
    def data(self):
        """
        返回event传递的数据
        """
        return self._data