#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 16:14

'''
测试city _functions.py
'''

import unittest
from city_functions import get_information

class informationTestCase(unittest.TestCase):
    '''测试city _functions.py'''
    def test_city_country(self):
        '''测试不通过'''
        information_name = get_information('Santiago','Chile')
        self.assertEqual(information_name,'Santiago Chile')

    def test_city_country_population(self):
        '''测试通过'''
        information_name__population = get_information('Santiago', 'Chile','500000')
        self.assertEqual(information_name__population, 'Santiago,Chile--population = 500000')

if __name__ == 'mian':
    unittest.main()

