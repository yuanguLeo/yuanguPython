#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 9:39

#7.1例题
# message = input('Tell me something, and will repeat it back to you: ')
# print(message)

#7.2.2例题
prompt = '\nTell me something, and will repeat it back to you: '
prompt = "\nEnter 'quit' to end the program: "
message = ''
while message != 'quit' :
    message = input(prompt)
    if message != 'quit':
        print(message)





