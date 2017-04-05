#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/5 11:33
# @Author  : Aries
# @Site    : 
# @File    : GPIOControl.py
# @Software: PyCharm

import RPi.GPIO as GPIO

class gpioController:
    def __init__(self):
        # 设置开发板模式
        GPIO.setmode(GPIO.BOARD)
        return "GPIO.SETMODE:",GPIO.BOARD,"完成设置"

    def setupInterPort(self,arr):
        for port in arr:
            GPIO.setup(port, GPIO.OUT)

    #每2秒钟闪烁一次的示例
    p = GPIO.PWM(12, 0.5)# channel=12 frequency=50Hz，赫兹=1/秒
    p.start(1)
    input('点击回车停止：')   # 在 Python 2 中需要使用 raw_input
    p.stop()
    GPIO.clearup()
