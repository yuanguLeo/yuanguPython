from Lib.base_functions import *
from config import *
from elements import provider as p


def __provider_create():
    element_click('link_text', p['provider_link_text'])
    sleep(1)
    repeat = start_mum
    while repeat < end_num:
        element_click('link_text', p['new_link_text'])
        sleep(1)
        element_send_keys('xpath', p['name_xpath'], '供应商-' + str(repeat + 1) + '-' + str(run_time))
        element_send_keys('xpath', p['short_name_xpath'], '供应商-' + str(repeat + 1) + '-' + str(run_time))
        element_click('xpath', p['save_btn_xpath'])
        sleep(0.3)
        element_click('link_text', p['ok_btn_link_text'])
        sleep(1)
        repeat = repeat + 1


def __provider_edit():
    element_click('link_text', p['provider_link_text'])
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
            sleep(1)
            repeat = repeat + 1


def provider_create():
    # 登陆
    login()
    # 跳转到原材料
    goto_provider_management()
    # 创建原材料
    __provider_create()
    # 结束运行
    finish()


def provider_edit():
    # 登陆
    login()
    # 跳转到原材料
    goto_provider_management()
    # 编辑原材料
    __provider_edit()
    # 结束运行
    finish()
