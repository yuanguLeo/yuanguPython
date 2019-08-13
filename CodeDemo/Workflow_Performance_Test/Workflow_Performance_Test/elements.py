# 基本卖品
retail = {
    'group_code_xpath': '/html/body/div[1]/div[2]/div[2]/form/div[1]/div/ul/li/input',
    'group_login_btn_xpath': '//*[@id="js-submit"]',
    'login_xpath': '/html/body/div[1]/div[2]/div[2]/form/div[2]/div/ul[1]/li[1]/input',
    'password_xpath': '/html/body/div[1]/div[2]/div[2]/form/div[2]/div/ul[1]/li[2]/input',
    'login_btn_xpath': '//*[@id="js-submit"]',
    'good_system_xpath': '/html/body/div[2]/div/div[2]/ul/li[2]/a',
    'good_management_xpath': '//*[@id="left-300049_2.0"]/div/a',
    'provider_management_xpath': '//*[@id="left-300085"]/div/a',
    'order_protocol_management': '//*[@id="left-300060_2.0"]/div/a'
}

# 原材料
material = {
    'material_link_text': u"原材料",
    'new_link_text': u"添加",
    'name_xpath': '//*[@id="goodsName"]',
    'sort_xpath': '//*[@id="category"]/div/span',
    'sort_item_link_text': u"原材料Gp",
    'unit_xpath': '//*[@id="unit"]/div/span',
    'unit_item_link_text': u"只",
    'cinema_xpath': '/html/body/div[3]/div/div[2]/div/form/div[3]/div[2]/div[1]/div/input',
    'cinema_check_xpath': '//*[@id="js-tree_1_check"]',
    'cinema_ok_btn_link_text': u'确定',
    'save_btn_xpath': '/html/body/div[3]/div/div[2]/div/div/input[1]',
    'sure_btn_xpath': '//*[@id="js-btn-ok"]',
    'know_btn_xpath': '//*[@id="js-btn-ok"]',
    'next_page_class': 'js-next',
    'edit_btn_link_text': u'编辑',
}

# 单品
goods = {
    'goods_link_text': u'单品',
    'new_link_text': u"添加",
    'name_xpath': '//*[@id="goodsName"]',
    'sort_xpath': '//*[@id="category"]/div/span',
    'sort_item_link_text': u'现制食品2.2',
    'unit_xpath': '//*[@id="unit"]/div/span',
    'unit_item_link_text': u"只",
    'price_xpath': '//*[@id="basics-price"]/div[1]/input',
    'cinema_xpath': '/html/body/div[3]/div/div[2]/div/form/div[3]/div[2]/div[1]/div/input',
    'cinema_check_xpath': '//*[@id="js-tree_1_check"]',
    'cinema_ok_btn_link_text': u'确定',
    'save_btn_xpath': '/html/body/div[3]/div/div[2]/div/div/input[1]',
    'sure_btn_xpath': '//*[@id="js-btn-ok"]',
    'know_btn_xpath': '//*[@id="js-btn-ok"]',
    'next_page_class': 'js-next',
    'edit_btn_link_text': u'编辑',
}

# 合成品
mix = {
    'mix_link_text': u'合成品',
    'mix_define_link_text': u'·合成品定义',
    'mix_match_link_text': u'·合成品配比',
    'new_link_text': u"添加",
    'name_xpath': '//*[@id="goodsName"]',
    'sort_xpath': '//*[@id="category"]/div/span',
    'sort_item_link_text': u'现制食品2.2',
    'unit_xpath': '//*[@id="unit"]/div/span',
    'unit_item_link_text': u"只",
    'price_xpath': '//*[@id="basics-price"]/div[1]/input',
    'cinema_xpath': '/html/body/div[3]/div/div[2]/div/form/div[3]/div[2]/div[1]/div/input',
    'cinema_check_xpath': '//*[@id="js-tree_1_check"]',
    'cinema_ok_btn_link_text': u'确定',
    'save_btn_xpath': '/html/body/div[3]/div/div[2]/div/div/input[1]',
    'sure_btn_xpath': '//*[@id="js-btn-ok"]',
    'know_btn_xpath': '//*[@id="js-btn-ok"]',
    'next_page_class': 'js-next',
    'edit_btn_link_text': u'编辑',
    'add_material_xpath': '/html/body/div[3]/form/div[2]/table/tbody/tr[3]/td/div/div',
    'checkbox_xpath': "(.//*[normalize-space(text()) and normalize-space(.)='名称'])[1]/following::label[1]",
    'material_ok_btn_link_text': u'确定',
    'material_num_xpath': '//*[@class="grid-lastTr"]/td[4]/div/div/input',
    'material_save_btn_xpath': '/html/body/div[3]/div/input[1]'
}

# 套餐
package = {
    'package_link_text': u'套餐',
    'package_define_link_text': u'·套餐定义',
    'package_match_link_text': u'·套餐内容',
    'new_link_text': u"添加",
    'name_xpath': '//*[@id="goodsName"]',
    'sort_xpath': '//*[@id="category"]/div/span',
    'sort_item_link_text': u'套餐Gp',
    'unit_xpath': '//*[@id="unit"]/div/span',
    'unit_item_link_text': u"只",
    'price_xpath': '//*[@id="basics-price"]/div[1]/input',
    'cinema_xpath': '/html/body/div[3]/div/div[2]/div/form/div[3]/div[2]/div[1]/div/input',
    'cinema_check_xpath': '//*[@id="js-tree_1_check"]',
    'cinema_ok_btn_link_text': u'确定',
    'save_btn_xpath': '/html/body/div[3]/div/div[2]/div/div/input[1]',
    'sure_btn_xpath': '//*[@id="js-btn-ok"]',
    'know_btn_xpath': '//*[@id="js-btn-ok"]',
    'next_page_class': 'js-next',
    'edit_btn_link_text': u'编辑',
    'add_goods_xpath': '/html/body/div[3]/div/div/div/form/div/div/div[2]/table/tbody/tr[2]/td/dl/dd/div[2]',
    'checkbox_xpath': "(.//*[normalize-space(text()) and normalize-space(.)='名称'])[1]/following::label[1]",
    'goods_ok_btn_link_text': u'确定',
    'goods_save_btn_xpath': '/html/body/div[3]/div/div/div/div/input[1]',
    'continue_save_btn_xpath': '//*[@id="js-btn-ok"]'
}


# 售卖键
sku = {
    'sku_link_text': u'售卖键管理',
    'new_link_text': u"添加",
    'sku_add_goods_btn_xpath': '/html/body/div[3]/form/div/table[1]/tbody/tr[2]/td/dl/dd/button',
    'add_goods_xpath': '//*[@class="transfer-list"]/table/tbody/tr[1]/td[1]/span/label',
    'goods_ok_btn_link_text': u'确定',
    'sku_name_xpath': '/html/body/div[3]/form/div/div[2]/table/thead/tr/td[2]/input[1]',
    'sku_sell_group_xpath': "(.//*[normalize-space(text()) and normalize-space(.)='所属售卖分组：'])[1]/following::span[1]",
    'all_sell_group_xpath': '/html/body/div[3]/form/div/table[2]/tbody/tr[1]/td/dl/dd/div[1]/div[1]/div/div/div[2]/label',
    'sell_group_ok_btn_link_text': u'确定',
    'cinema_xpath': '/html/body/div[3]/form/div/div[12]/div[1]/div/input',
    'cinema_check_xpath': '//*[@id="js-tree_1_check"]',
    'cinema_ok_btn_link_text': u'确定',
    'save_btn_xpath': '/html/body/div[3]/div/input[1]',
    'know_btn_xpath': '//*[@id="js-btn-ok"]',
    'edit_btn_link_text': u'编辑'
}


# 供应商
provider = {
    'provider_link_text': u'供应商维护',
    'new_link_text': u"添加",
    'name_xpath': '/html/body/div[3]/form/div[1]/table/tbody/tr[2]/td[1]/dl/dd/div/input',
    'short_name_xpath': '/html/body/div[3]/form/div[1]/table/tbody/tr[2]/td[2]/dl/dd/div/input',
    'save_btn_xpath': '//*[@id="js-submit"]',
    'ok_btn_link_text': u'确认',
    'edit_btn_link_text': u'编辑'
}


# 售卖协议
order_protocol = {
    'protocol_link_text': u'采购协议',
    'new_link_text': u"添加",
    'protocol_name_xpath': '//*[@id="agreementName"]',
    'protocol_type_list_xpath': '//*[@id="js-deal-type"]/div/span',
    'protocol_type_xpath': u'框架协议',
    'start_date_js': "$('input[name=startDate]').removeAttr('readonly')",
    'end_date_js': "$('input[name=endDate]').removeAttr('readonly')",
    'sign_date_js': "$('input[name=signDate]').removeAttr('readonly')",
    'start_date_xpath': '//*[@name="startDate"]',
    'end_date_xpath': '//*[@name="endDate"]',
    'sign_date_xpath': '//*[@name="signDate"]',
    'start_date_link_text': u'开始日期',
    'end_date_link_text': u'结束日期',
    'provider_list_xpath': '//*[@id="js-supplier"]/div/span',
    'provider_xpath': '//*[@id="js-supplier"]/div/div/div/ul/li[2]/a',
    'add_goods_btn_xpath': '//*[@id="js-add-goods"]',
    'goods_checkbox_xpath': '//*[@class="transfer-list"]/table/tbody/tr[1]/td[1]/span/label',
    'goods_save_btn_xpath': '//*[@id="js-btn-ok"]',
    'cost_start_xpath': '//*[@id="js-deal-type1"]/tr[2]/td[4]/div/div[1]/input',
    'cost_end_xpath': '//*[@id="js-deal-type1"]/tr[2]/td[4]/div/div[2]/input',
    'tax_xpath': '//*[@id="js-deal-type1"]/tr[2]/td[5]/div/div/input',
    'cinema_xpath': '/html/body/div[3]/div[1]/form[2]/div/div/div[1]/div/input',
    'cinema_check_xpath': '//*[@id="js-tree_1_check"]',
    'cinema_ok_btn_link_text': u'确定',
    'finish_btn_xpath': '/html/body/div[3]/div[2]/input[1]',
    'ok_btn_link_text': u'确定',
    'edit_btn_link_text': u'编辑',
    'save_btn_xpath': '/html/body/div[3]/div[2]/input[1]'
}
