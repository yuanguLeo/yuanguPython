#!/usr/bin/env python
#_*_coding:utf-8_*_

import calendar

'''
日历模块

'''
#返回指定某年某月的日历
print(calendar.month(2019.3))

#返回指定年的日历
print(calendar.calendar(2019))

#判断闰年
print(calendar.isleap(2000))

#返回某个月的weekday的第一天和这个月的总天数
print(calendar.monthrange(2019,3))

#返回某个月以每个月为元素的列表
print(calendar.monthcalendar(2017,7))










