from Lib.base_functions import *
from config import *
from elements import package as p


def __package_create():
    element_click('link_text', p['package_link_text'])
    sleep(0.5)
    element_click('link_text', p['package_define_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', p['new_link_text'])
        sleep(1)
        element_send_keys('xpath', p['name_xpath'], '套餐-' + str(repeat + 1) + '-' + str(run_time))
        element_click('xpath', p['sort_xpath'])
        element_click('link_text', p['sort_item_link_text'])
        element_click('xpath', p['unit_xpath'])
        element_click('link_text', p['unit_item_link_text'])
        element_send_keys('xpath', p['price_xpath'], '26')
        element_click('xpath', p['cinema_xpath'])
        element_click('xpath', p['cinema_check_xpath'])
        element_click('link_text', p['cinema_ok_btn_link_text'])
        element_click('xpath', p['save_btn_xpath'])
        sleep(0.3)
        element_click('xpath', p['sure_btn_xpath'])
        sleep(0.3)
        element_click('xpath', p['know_btn_xpath'])
        sleep(1)
        repeat = repeat + 1


def __package_edit():
    element_click('link_text', p['package_link_text'])
    sleep(0.5)
    element_click('link_text', p['package_define_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', p['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(p['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', p['save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', p['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def __package_match_edit():
    element_click('link_text', p['package_link_text'])
    sleep(0.5)
    element_click('link_text', p['package_match_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
            i = 0
            while i < int(repeat / 10):
                element_click('class', p['next_page_class'])
                i = i + 1
                sleep(0.3)
            sleep(0.5)
            edit_btn = b.find_elements_by_link_text(p['edit_btn_link_text'])
            print(edit_btn)
            print('repeat: ' + str(repeat) + '    repeat%10: ' + str(repeat % 10))
            if is_workflow_on:
                edit_btn[0].click()
            else:
                edit_btn[repeat % 10].click()
            sleep(1)
            element_click('xpath', p['add_goods_xpath'])
            sleep(0.5)
            element_click('xpath', p['checkbox_xpath'])
            element_click('link_text', p['goods_ok_btn_link_text'])
            sleep(0.5)
            element_click('xpath', p['goods_save_btn_xpath'])
            sleep(0.3)
            element_click('xpath', p['continue_save_btn_xpath'])
            # sleep(0.3)
            # element_click('xpath', p['know_btn_xpath'])
            sleep(1)
            repeat = repeat + 1


def package_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 创建原材料
    __package_create()
    # 结束运行
    finish()


def package_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __package_edit()
    # 结束运行
    finish()


def package_match_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_goods_management()
    # 编辑原材料
    __package_match_edit()
    # 结束运行
    finish()
