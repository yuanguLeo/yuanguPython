#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/12 11:13

'''

'''

import unittest
from information import Employee

class testInformation(unittest.TestCase):
    """测试Information"""
    def setUp(self) -> None:
        """创建员工"""
        self.employees = Employee('张','三',5000)

    def test_give_default_raise(self):
        """打印默认年薪"""
        self.employees.give_raise()
        self.assertEqual(self.employees.annual_salarys,8000)

    def test_give_custom_raise(self):
        """打印自定义年薪"""
        self.employees.give_raise(5000)
        self.assertEqual(self.employees.annual_salarys,10000)

if __name__ == 'main':
    unittest.main()
