#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/8 15:33

'''
对比数据库字段值是否相等
'''

import pymysql
import logging

# 设定日志级别
from CodeDemo.mysqlContrast.db_admin import conn_old, conn_new

logging.basicConfig(
    level=logging.DEBUG
)



# 新旧表字段存放在二维列表中
def db_card_active_log(tb_new, tb_old, *tb_field):
    """
    :param tb_new: 新表
    :param tb_old: 旧表
    :param tb_field: [[新表中字段,],[对应旧表中的字段,]]
    :return: 返回新旧表中的数据总量，以及旧表中存在，但是在新表中没有找到的数据
    """
    # 校验数据总量是否一致
    cmp_new_sql = "SELECT COUNT(*) FROM dgp_membership_db.card_active_log WHERE group_code = '23456798'; " + str(tb_new) + ";"
    cmp_old_sql = "SELECT COUNT(*) FROM center.card_active_log; " + str(tb_old) + ";"
    logging.debug(cmp_new_sql)
    logging.debug(cmp_old_sql)
    cursor_old = conn_old.cursor()
    cursor_new = conn_new.cursor()
    cursor_new.execute(cmp_new_sql)
    cursor_old.execute(cmp_old_sql)

    new_num = cursor_new.fetchone()
    old_num = cursor_old.fetchone()

    if new_num == old_num:
        ''.join(logging.info (tb_new + "和" + tb_old + "数据量相同:" + new_num))
    else:
        ''.join(logging.error ({tb_new  + "_new": new_num[0], tb_old: old_num[0]}))

    # 校验各字段值是否一致
    field_new = ", ".join(tb_field[0][0])
    field_old = ", ".join(tb_field[0][1])
    cmp_dt_new_sql = "select " + field_new + " from " + tb_new + ";"
    cmp_dt_old_sql = "select " + field_old + " from " + tb_old + ";"
    logging.debug(cmp_dt_new_sql)
    logging.debug(cmp_dt_old_sql)
    cursor_new.execute(cmp_dt_new_sql)
    cursor_old.execute(cmp_dt_old_sql)
    new_dt = cursor_new.fetchall()
    old_dt = cursor_old.fetchall()
    logging.debug(list(new_dt))
    logging.debug(list(old_dt))

    count = 0
    for item in old_dt:
        if item in new_dt:
            pass
        else:
            logging.error(tb_new + "新表中未找到:" + str(item))
            count += 1

    logging.error("总数: %d" % count)
    logging.error("\n\n")

    # 关闭游标
    cursor_old.close()
    cursor_new.close()
    return


# 测试表
test_table_field = [["field_new"], ["field_old"]]
db_card_active_log("test_table", "test_table", test_table_field)

# 关闭数据库连接
conn_old.close()
conn_new.close()

