from time import sleep
from selenium.common.exceptions import NoSuchElementException
from config import *
from elements import retail as r


def element_is_exist(method, value):
    if method == "xpath":
        try:
            b.find_element_by_xpath(value).is_displayed()
            return True
        except NoSuchElementException:
            print("xpath is not find: " + value)
            return False
    elif method == "link_text":
        try:
            b.find_element_by_link_text(value).is_displayed()
            return True
        except NoSuchElementException:
            print("link_text is not find: " + value)
            return False
    elif method == "class":
        try:
            b.find_element_by_class_name(value).is_displayed()
            return True
        except NoSuchElementException:
            print("class is not find: " + value)
            return False
    else:
        print("参数异常")


def element_click(method, value):
    if method == "xpath":
        retry = 0
        while retry < 9:
            if element_is_exist(method, value):
                b.find_element_by_xpath(value).click()
                print("点击元素xpath：" + value)
                break
            else:
                sleep(1)
                retry = retry + 1
    elif method == "link_text":
        retry = 0
        while retry < 9:
            if element_is_exist(method, value):
                b.find_element_by_link_text(value).click()
                print("点击元素like_name：" + value)
                break
            else:
                sleep(1)
                retry = retry + 1
    elif method == "class":
        retry = 0
        while retry < 9:
            if element_is_exist(method, value):
                b.find_element_by_class_name(value).click()
                print("点击元素class：" + value)
                break
            else:
                sleep(1)
                retry = retry + 1
    else:
        print("参数异常")


def element_send_keys(method, value, keys):
    if method == "xpath":
        retry = 0
        while retry < 9:
            if element_is_exist(method, value):
                b.find_element_by_xpath(value).send_keys(keys)
                print("对元素xpath：" + value + "输入：" + keys)
                break
            else:
                sleep(1)
                retry = retry + 1
    elif method == "link_text":
        retry = 0
        while retry < 9:
            if element_is_exist(method, value):
                b.find_element_by_link_text(value).send_keys(keys)
                print("对元素like_name：" + value + "输入：" + keys)
                break
            else:
                sleep(1)
                retry = retry + 1
    elif method == "class":
        retry = 0
        while retry < 9:
            if element_is_exist(method, value):
                b.find_element_by_class_name(value).send_keys(keys)
                print("对元素class：" + value + "输入：" + keys)
                break
            else:
                sleep(1)
                retry = retry + 1
    else:
        print("参数异常")


def login():
    b.get("http://retail.yinghezhong.com")
    element_send_keys('xpath', r['group_code_xpath'], group_code)
    element_click('xpath', r['group_login_btn_xpath'])
    element_send_keys('xpath', r['login_xpath'], username)
    element_send_keys('xpath', r['password_xpath'], password)
    element_click('xpath', r['login_btn_xpath'])
    sleep(1)


def goto_goods_management():
    element_click('xpath', r['good_management_xpath'])
    sleep(1)


def goto_provider_management():
    element_click('xpath', r['provider_management_xpath'])


def goto_order_protocol_management():
    element_click('xpath', r['order_protocol_management'])


def finish():
    b.close()
