#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/7 16:33

'''
例题：test_name_ function.py
'''

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
     '''测试name_function'''
     def test_first_last_name(self):
         '''测试name_function的结果是否能够正确运行'''
         fromatted_name = get_formatted_name('Janis','Joplin')
         self.assertEqual(fromatted_name,'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

