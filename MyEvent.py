#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 15:10
# @Author  : Aries
# @Site    : 
# @File    : MyEvent.py
# @Software: PyCharm
import EventClass as Event


class MyEvent(Event):
    """
    When subclassing Event class the only thing you must do is to define
    a list of class level constants which defines the event types and the
    string associated to them
    """
    ASK     = "askMyEvent"
    RESPOND = "respondMyEvent"


class WhoAsk(object):
    """
    First class which ask who is listening to it
    """
    def __init__(self, event_dispatcher):
        # Save a reference to the event dispatch
        self.event_dispatcher = event_dispatcher
        # Listen for the RESPOND event type
        self.event_dispatcher.add_event_listener(
            MyEvent.RESPOND, self.on_answer_event
        )

    def ask(self):
        """
        Dispatch the ask event
        """
        print ">>> I'm instance {0}. Who are listening to me ?".format( self )
        self.event_dispatcher.dispatch_event(
            MyEvent(MyEvent.ASK, self)
        )

    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        print "<<< Thank you instance {0}".format( event.data )


class WhoRespond( object ):
    """
    Second class who respond to ASK events
    """
    def __init__(self, event_dispatcher):
        # Save event dispatcher reference
        self.event_dispatcher = event_dispatcher
        # Listen for ASK event type
        self.event_dispatcher.add_event_listener(
            MyEvent.ASK, self.on_ask_event
        )

    def on_ask_event(self, event):
        """
        Event handler for ASK event type
        """
        self.event_dispatcher.dispatch_event(
            MyEvent(MyEvent.RESPOND, self)
        )