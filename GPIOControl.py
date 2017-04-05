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
        '''
        类初始化，GPIO.setmode(GPIO.BOARD)
        '''
        # 设置开发板模式
        GPIO.setmode(GPIO.BOARD)
        return "GPIO.SETMODE:",GPIO.BOARD,"完成设置"

    def setupInterPort(self,_arr):
        '''
        用于设置针脚端口，需要根据使用的针脚类型进行设置，默认使用GPIO.BOARD
        :param arr: 针脚端口数组
        :return: 无返回
        '''
        for port in _arr:
            GPIO.setup(port, GPIO.OUT)

    def setFrequency(self,_frequency):
        '''
        用于设置PWM的发送频率
        :param _frequency: 频率，取值为>1.0
        :return: 无返回
        '''
        GPIO.ChangeFrequency(_frequency)

    def setDutyCycle(self,_dutyCycle):
        '''
        用于设置占空比
        :param _dutyCycle: 占空比，取值0.0-100.0
        :return: 无返回
        '''
        GPIO.ChangeDutyCycle(_dutyCycle)

    def runForward(self):


    #每2秒钟闪烁一次的示例
    p = GPIO.PWM(12, 0.5)# channel=12 frequency=50Hz，赫兹=1/秒
    p.start(1)
    input('点击回车停止：')   # 在 Python 2 中需要使用 raw_input
    p.stop()
    GPIO.clearup()
