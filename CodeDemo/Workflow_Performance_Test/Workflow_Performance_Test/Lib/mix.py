from Lib.base_functions import *
from config import *
from elements import mix


def __mix_create():
    element_click('link_text', mix['mix_link_text'])
    sleep(0.5)
    element_click('link_text', mix['mix_define_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', mix['new_link_text'])
        sleep(1)
        element_send_keys('xpath', mix['name_xpath'], '合成品-' + str(repeat + 1) + '-' + str(run_time))
        element_click('xpath', mix['sort_xpath'])
        element_click('link_text', mix['sort_item_link_text'])
        element_click('xpath', mix['unit_xpath'])
        element_click('link_text', mix['unit_item_link_text'])
        element_send_keys('xpath', mix['price_xpath'], '26')
        element_click('xpath', mix['cinema_xpath'])
        element_click('xpath', mix['cinema_check_xpath'])
        element_click('link_text', mix['cinema_ok_btn_link_text'])
        element_click('xpath', mix['save_btn_xpath'])
        sleep(0.3)
        element_click('xpath', mix['sure_btn_xpath'])
        sleep(0.3)
        element_click('xpath', mix['know_btn_xpath'])
        sleep(1)
        repeat = repeat + 1


def __mix_edit():
    element_click('link_text', mix['mix_link_text'])
    sleep(0.5)
    element_click('link_text', mix['mix_define_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', mix['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(mix['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', mix['save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', mix['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def __mix_match_edit():
    element_click('link_text', mix['mix_link_text'])
    sleep(0.5)
    element_click('link_text', mix['mix_match_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', mix['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(mix['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', mix['add_material_xpath'])
            sleep(0.5)
            element_click('xpath', mix['checkbox_xpath'])
            element_click('link_text', mix['material_ok_btn_link_text'])
            sleep(0.5)
            element_send_keys('xpath', mix['material_num_xpath'], '1')
            element_click('xpath', mix['material_save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', mix['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def mix_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 创建原材料
    __mix_create()
    # 结束运行
    finish()


def mix_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __mix_edit()
    # 结束运行
    finish()


def mix_match_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __mix_match_edit()
    # 结束运行
    finish()
