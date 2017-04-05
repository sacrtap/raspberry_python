#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/5 11:33
# @Author  : Aries
# @Site    : 
# @File    : GPIOControl.py
# @Software: PyCharm

import RPi.GPIO as GPIO
import logging
import logging.config

class GPIOController:
    wheelArray = [12,33,35,32] #存放轮序的数组，存储规则【左前、右前，左后，右后】
    p = [] #存放舵机实例对象
    frequency = 1.0 #默认的频率值
    dutyCycle = 0.0 #默认的占空比
    def __init__(self):
        '''
        类初始化，GPIO.setmode(GPIO.BOARD)
        '''

        # 设置开发板模式
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        logging.info('GPIO.setmode(GPIO.BOARD) is completed.')
        # 创建舵机实例对象
        for wl in self.wheelArray:
            GPIO.setup(wl, GPIO.OUT)
            self.p.append(GPIO.PWM(wl, 0.5))
        logging.info('Control instance(4) is completed.')

    def setupInterPort(self,_arr):
        '''
        用于设置针脚端口，需要根据使用的针脚类型进行设置，默认使用GPIO.BOARD
        :param arr: 针脚端口数组，传值规则【左前、右前，左后，右后】
        :return: 无返回
        '''
        wheelArray = _arr
        for port in _arr:
            GPIO.setup(port, GPIO.OUT)
        _portInfo = str(_arr)
        logging.info('GPIO.setup ports'+_portInfo+' is completed.')

    def setFrequency(self,_pwm,_frequency):
        '''
        用于设置PWM的发送频率
        :param _pwm: 舵机实例
        :param _frequency: 频率，取值为>1.0
        :return: 无返回
        '''
        _pwm.ChangeFrequency(_frequency)
        logging.info('GPIO.ChangeFrequency Changed' + str(_frequency) + ' is completed.')

    def setDutyCycle(self,_pwm, _dutyCycle):
        '''
        用于设置占空比
        :param _pwm: 舵机实例
        :param _dutyCycle: 占空比，取值0.0-100.0
        :return: 无返回
        '''
        _pwm.ChangeDutyCycle(_dutyCycle)
        logging.info('GPIO.ChangeDutyCycle Changed' + str(_dutyCycle) + ' is completed.')

    def runForward(self,_hz):
        self.p[0] = GPIO.PWM(self.wheelArray[0], _hz)  # channel=12 frequency=50Hz，赫兹=1/秒
        self.p[2] = GPIO.PWM(self.wheelArray[2], _hz)  # channel=12 frequency=50Hz，赫兹=1/秒
        self.p[0].start(1)
        self.p[2].start(1)
        logging.info('The Car has running Forward...')

    def Stop(self):
        for px in self.p:
            px.stop()
        GPIO.clearup()
        logging.info('The Car has stop...')


