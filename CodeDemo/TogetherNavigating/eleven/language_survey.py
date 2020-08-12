#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/11 15:35

'''

'''

from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_results()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

#显示调查结果
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()






