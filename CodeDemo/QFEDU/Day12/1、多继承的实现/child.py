#!/usr/bin/env python
#_*_coding:utf-8_*_

from father import Father
from mother import Mother

class Child(Father,Mother):

    def __init__(self,money,faceValue):
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)












