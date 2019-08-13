from Lib.base_functions import *
from config import *
from elements import goods as g


def __goods_create():
    element_click('link_text', g['goods_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', g['new_link_text'])
        sleep(1)
        element_send_keys('xpath', g['name_xpath'], '单品-' + str(repeat + 1) + '-' + str(run_time))
        element_click('xpath', g['sort_xpath'])
        element_click('link_text', g['sort_item_link_text'])
        element_click('xpath', g['unit_xpath'])
        element_click('link_text', g['unit_item_link_text'])
        element_send_keys('xpath', g['price_xpath'], '26')
        element_click('xpath', g['cinema_xpath'])
        element_click('xpath', g['cinema_check_xpath'])
        element_click('link_text', g['cinema_ok_btn_link_text'])
        element_click('xpath', g['save_btn_xpath'])
        sleep(0.3)
        element_click('xpath', g['sure_btn_xpath'])
        sleep(0.3)
        element_click('xpath', g['know_btn_xpath'])
        sleep(1)
        repeat = repeat + 1


def __goods_edit():
    element_click('link_text', g['goods_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', g['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(g['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', g['save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', g['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def goods_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 创建原材料
    __goods_create()
    # 结束运行
    finish()


def goods_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __goods_edit()
    # 结束运行
    finish()
