#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 15:19
# @Author  : Aries
# @Site    : 
# @File    : CarController.py
# @Software: PyCharm

import logging
import logging.config
import json
import paramDecoder
import time
class Mode:
    free = 1
    preset = 2
    orbit = 3

class Direction:
    front = "front"
    behind = "behind"
    left = "left"
    right = "right"
    up = "up"
    down = "down"
    stop= "stop"

class BasicConfig:
    frequency = 200
    def __init__(self, _frequency = 200):
        self.frequency = _frequency

    def setFrequency(self, _frequency):
        self.frequency = _frequency

    @classmethod
    def getFrequency(self):
        return int(self.frequency)

class CarMotion:
    defaultStep = 100 # 用于直线行走时的默认步数
    defaultSpeed = 10 # 用于直线行走时的默认速度
    defaultTurnStep = 50 # 用于转弯时的默认步数
    defaultTurnSpeed = 5 # 用于转弯时的默认速度

    def MotionByDirection(self, _direction, _speed):
        if(_direction == Direction.front):
            return self.MoveFront(self.defaultStep, _speed)
        elif(_direction == Direction.behind):
            return self.MoveBehind(self.defaultStep, _speed)
        elif(_direction == Direction.left):
            return self.TurnLeftByStep(self.defaultTurnStep, self.defaultTurnSpeed)
        elif(_direction == Direction.right):
            return self.TurnRightByStep(self.defaultTurnStep, self.defaultTurnSpeed)
        elif(_direction == Direction.up):
            return self.MoveUp(self.defaultStep, _speed)
        elif(_direction == Direction.down):
            return self.MoveDown(self.defaultStep, _speed)
        elif(_direction == Direction.stop):
            return self.Stop(10,10)
        else:
            return False
    @classmethod
    def stopCar(self):
        return self.Stop(self.defaultStep, self.defaultSpeed)

    def setDefaultStep(self, _step = 100):
        self.defaultStep = _step

    def setDefaultTurnStep(self, _step = 50):
        self.defaultTurnStep = _step

    def MoveWithAPI(self, _moterNumber, _turn, _step, _speed):
        '''
        调取硬件操作接口函数
        :param _moterNumber: 电机编号左前（1）、右前（2）、左后（3）、右后（4）
        :param _turn:  电机旋转，顺时针旋转（1），逆时针旋转（0）
        :param _step:  电机行走步数，如52步
        :param _speed:  电机行走速度，如100转/分
        :return: 
        '''
        # need to do:cm cover to angle/s
        # the function hasn't done, need to write here
        ActionTranslate.setCode(10001) #设定为正在运行的状态
        return True

    def Stop(self,_step, _speed):
        self.MoveWithAPI(1,0, _step, _speed)
        self.MoveWithAPI(2,0, _step, _speed)
        self.MoveWithAPI(3,0, _step, _speed)
        self.MoveWithAPI(4,0, _step, _speed)
        self.MoveWithAPI(5,0, _step, _speed)
        logging.info('stop step & speed is : %s , %s', _step, _speed)
        return True

    def MoveFront(self, _step = defaultStep, _speed = defaultSpeed):
        self.MoveWithAPI(1, 1, _step, _speed)
        self.MoveWithAPI(2, 1, _step, _speed)
        self.MoveWithAPI(3, 1, _step, _speed)
        self.MoveWithAPI(4, 1, _step, _speed)
        logging.info('MoveFront with step & speed is : %s , %s', _step, _speed)
        return True

    def MoveBehind(self, _step = defaultStep, _speed = defaultSpeed):
        self.MoveWithAPI(1, 0, _step, _speed)
        self.MoveWithAPI(2, 0, _step, _speed)
        self.MoveWithAPI(3, 0, _step, _speed)
        self.MoveWithAPI(4, 0, _step, _speed)
        logging.info('MoveBehind with step & speed is : %s , %s', _step, _speed)
        return True

    def TurnLeftByStep(self, _step = defaultTurnStep, _speed = defaultSpeed):
        self.MoveWithAPI(1, 0, _step, 0)
        self.MoveWithAPI(2, 1, _step, _speed)
        self.MoveWithAPI(3, 0, _step, 0)
        self.MoveWithAPI(4, 1, _step, _speed)
        logging.info('TurnLeftByStep with step & speed is : %s , %s', _step, _speed)
        return True

    def TurnRightByStep(self, _step = defaultTurnStep, _speed = defaultSpeed):
        self.MoveWithAPI(1, 1, _step, _speed)
        self.MoveWithAPI(2, 0, _step, 0)
        self.MoveWithAPI(3, 1, _step, _speed)
        self.MoveWithAPI(4, 0, _step, 0)
        logging.info('TurnRightByStep with step & speed is : %s , %s', _step, _speed)
        return True

    def MoveUp(self, _step = defaultStep, _speed = defaultSpeed):
        self.MoveWithAPI(5, 1, _step, _speed)
        logging.info('MoveUp with step & speed is : %s , %s', _step, _speed)
        return True

    def MoveDown(self, _step = defaultStep, _speed = defaultSpeed):
        self.MoveWithAPI(5, 0, _step, _speed)
        logging.info('MoveDown with step & speed is : %s , %s', _step, _speed)
        return True

class ActionTranslate:
    cm = None
    status = False
    param = None
    def __init__(self):
        self.cm = CarMotion()
        self.status = False
        self.code = 10006 #停止状态

    def setParam(self, _mode, _param):
        self.mode = int(_mode)
        self.param = _param

    def getStatus(self):
        return self.status

    @classmethod
    def setCode(self, _code):
        self.code = _code

    def getCode(self):
        return self.code

    def TransByMode(self):
        if(self.mode == Mode.free):
            jsonObj = paramDecoder.FreeDecoder(self.param)
            self.status = self.cm.MotionByDirection(jsonObj.getDirection(),jsonObj.getSpeed())
            if(self.status):
                self.setCode(10002)
            else:
                self.setCode(10003)
            return self.status

        elif(self.mode == Mode.preset):
            jsonObj = paramDecoder.PresetDecoder(self.param)
            for r in jsonObj.getList():
                if(jsonObj.getDuration(r)):
                    num = int(jsonObj.getDuration(r)*1000 / BasicConfig.getFrequency())
                    i = 1
                    while i == num:
                        self.status = self.cm.MotionByDirection(jsonObj.getDirection(r), jsonObj.getSpeed(r))
                        i += 1
                        time.sleep(BasicConfig.getFrequency() - 100 / 1000)
                    return True
                elif(jsonObj.getDistance(r)):
                    #计算距离和步数相除后的数量
                    num = 100
                    i = 1
                    while i == num:
                        i += 1
                        self.status = self.cm.MotionByDirection(jsonObj.getDirection(r), jsonObj.getSpeed(r))
                        time.sleep(BasicConfig.getFrequency() - 100 / 1000)
                    return True
                else:
                    logging.info('duration & distance is %s & %s', jsonObj.getDuration(r), jsonObj.getDistance(r))
                    return False
        elif(self.mode == Mode.orbit):
            #预留给轨迹文件读取
            return True
        else:
            return False

    @classmethod
    def stopAction(self):
        self.status = True
        self.cm.stopCar()
        return True