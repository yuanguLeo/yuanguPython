from Lib.base_functions import *
from config import *
from elements import material as m


def __material_create():
    element_click('link_text', m['material_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', m['new_link_text'])
        sleep(1)
        element_send_keys('xpath', m['name_xpath'], '原材料-' + str(repeat + 1) + '-' + str(run_time))
        element_click('xpath', m['sort_xpath'])
        element_click('link_text', m['sort_item_link_text'])
        element_click('xpath', m['unit_xpath'])
        element_click('link_text', m['unit_item_link_text'])
        element_click('xpath', m['cinema_xpath'])
        element_click('xpath', m['cinema_check_xpath'])
        element_click('link_text', m['cinema_ok_btn_link_text'])
        element_click('xpath', m['save_btn_xpath'])
        sleep(0.3)
        element_click('xpath', m['sure_btn_xpath'])
        sleep(0.3)
        element_click('xpath', m['know_btn_xpath'])
        sleep(1)
        repeat = repeat + 1


def __material_edit():
    element_click('link_text', m['material_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', m['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(m['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', m['save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', m['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def material_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 创建原材料
    __material_create()
    # 结束运行
    finish()


def material_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __material_edit()
    # 结束运行
    finish()
