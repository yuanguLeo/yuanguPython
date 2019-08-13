from Lib.base_functions import *
from config import *
from elements import order_protocol as op


def __order_protocol_create():
    element_click('link_text', op['protocol_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', op['new_link_text'])
        sleep(1)
        element_send_keys('xpath', op['protocol_name_xpath'], '采购协议-' + str(repeat + 1) + '-' + str(run_time))
        element_click('xpath', op['protocol_type_list_xpath'])
        sleep(0.3)
        element_click('link_text', op['protocol_type_xpath'])
        sleep(0.3)
        b.execute_script(op['start_date_js'])
        element_send_keys('xpath', op['start_date_xpath'], '2017-11-01')
        b.execute_script(op['end_date_js'])
        element_send_keys('xpath', op['end_date_xpath'], '2019-12-30')
        b.execute_script(op['sign_date_js'])
        b.find_element_by_xpath(op['sign_date_xpath']).clear()
        element_send_keys('xpath', op['sign_date_xpath'], '2017-11-01')
        element_click('xpath', op['provider_list_xpath'])
        sleep(0.3)
        element_click('xpath', op['provider_xpath'])
        sleep(0.3)
        element_click('xpath', op['add_goods_btn_xpath'])
        sleep(0.3)
        element_click('xpath', op['goods_checkbox_xpath'])
        element_click('xpath', op['goods_save_btn_xpath'])
        sleep(0.3)
        element_send_keys('xpath', op['cost_start_xpath'], '10')
        element_send_keys('xpath', op['cost_end_xpath'], '20')
        element_send_keys('xpath', op['tax_xpath'], '7')
        element_click('xpath', op['cinema_xpath'])
        sleep(0.3)
        element_click('xpath', op['cinema_check_xpath'])
        element_click('link_text', op['cinema_ok_btn_link_text'])
        sleep(0.3)
        element_click('xpath', op['finish_btn_xpath'])
        sleep(0.3)
        element_click('link_text', op['ok_btn_link_text'])
        sleep(1)
        repeat = repeat + 1


def __order_protocol_edit():
    element_click('link_text', op['protocol_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', op['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(op['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', op['save_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def order_protocol_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_order_protocol_management()
    # 创建原材料
    __order_protocol_create()
    # 结束运行
    finish()


def order_protocol_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_order_protocol_management()
    # 编辑原材料
    __order_protocol_edit()
    # 结束运行
    finish()
