#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 14:13
# @Author  : Aries
# @Site    : 
# @File    : EventDispatcherClass.py
# @Software: PyCharm

class EventDispatcher(object):
    """
    event分发类 监听和分发event事件
    """
    def __init__(self):
        """
        初始化类
        """
        self._events = dict()

    def __del__(self):
        """
        清空所有event
        """
        self._events = None

    def has_listener(self,event_type,listener):
        """
        返回注册到event_type的listener
        :param event_type: 监听事件类型
        :param listener: 监听者
        :return: 返回注册到event_type的listener
        """
        # Check for event type and for the listener
        if event_type in self._events.keys():
            return listener in self._events[event_type]
        else:
            return False

    def dispatch_event(self,event):
        """
        Dispatch an instance of Event class
        :param event: 监听事件的类型
        :return: 无
        """
        # 分发event到所有关联的listener
        if event.type in self._events.keys():
            listeners = self._events[event.type]
            for listener in listeners:
                listener(event)
    def add_event_listener(self,event_type,listener):
        """
        给某种事件类型添加listener
        :param event_type: 监听事件类型
        :param listener: 监听
        :return: 无
        """
        if not self.has_listener(event_type, listener):
            listeners = self._events.get(event_type, [])
            listeners.append(listener)
            self._events[event_type] = listeners
    def remove_event_listener(self,event_type,listener):
        """
        移出某种事件类型的所以listener
        :param event_type: 监听事件类型
        :param listener: 监听
        :return: 
        """
        if self.has_listener(event_type, listener):
            listeners = self._events[event_type]
            if len(listeners) == 1:
                # Only this listener remains so remove the key
                del self._events[event_type]
            else:
                # Update listeners chain
                listeners.remove(listener)
                self._events[event_type] = listeners