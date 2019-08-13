from Lib.base_functions import *
from config import *
from elements import sku


def __sku_create():
    element_click('link_text', sku['sku_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', sku['new_link_text'])
        sleep(1)
        element_click('xpath', sku['sku_add_goods_btn_xpath'])
        sleep(0.3)
        element_click('xpath', sku['add_goods_xpath'])
        element_click('link_text', sku['goods_ok_btn_link_text'])
        sleep(0.3)
        value = b.find_element_by_xpath(sku['sku_name_xpath']).get_property('value')
        print(value)
        b.find_element_by_xpath(sku['sku_name_xpath']).clear()
        element_send_keys('xpath', sku['sku_name_xpath'], '售卖键-' + str(repeat + 1) + '-' + value + '-' + str(run_time))
        element_click('xpath', sku['sku_sell_group_xpath'])
        element_click('xpath', sku['all_sell_group_xpath'])
        element_click('link_text', sku['sell_group_ok_btn_link_text'])
        sleep(0.3)
        element_click('xpath', sku['cinema_xpath'])
        element_click('xpath', sku['cinema_check_xpath'])
        element_click('link_text', sku['cinema_ok_btn_link_text'])
        element_click('xpath', sku['save_btn_xpath'])
        sleep(0.3)
        element_click('xpath', sku['know_btn_xpath'])
        sleep(1)
        repeat = repeat + 1


def __sku_edit():
    element_click('link_text', sku['sku_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', sku['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(sku['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', sku['save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', sku['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def sku_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 创建原材料
    __sku_create()
    # 结束运行
    finish()


def sku_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __sku_edit()
    # 结束运行
    finish()
