#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/12 18:12

'''
对比数据库字段值是否相等
'''
import db_admin

def db_card_active_log_num():
    """对比数据库表总数"""
    new_sql = "SELECT COUNT(*) FROM dgp_membership_db.card_active_log WHERE group_code = '23456798'; "
    new_sql_vlues = print(new_sql)
    print(new_sql_vlues)
    old_sql = "SELECT COUNT(*) FROM center.card_active_log; "
    old_sql_vlues = print(old_sql)
    print(old_sql_vlues)

    if new_sql_vlues == old_sql_vlues:
        print("新老集团结果一致！")
    else:
        print("新老集团结果不一致！")

def db_card_active_log():
    """对比数据库表字段值"""
    pass


db_card_active_log_num()


