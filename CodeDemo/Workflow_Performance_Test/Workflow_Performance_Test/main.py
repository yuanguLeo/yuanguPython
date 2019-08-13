from Lib.material import *
from Lib.goods import *
from Lib.mix import *
from Lib.package import *
from Lib.sku import *
from Lib.provider import *
from Lib.order_protocol import *

# 请先到config.py中设置需要的参数(包括账号，集团，创建数量，是否使用审批流)，如果执行中遇到问题，请检查elements.py并更改对应识别元素

# 执行操作：
# 1.创建原材料 2.编辑原材料 3.创建单品 4.编辑单品 5.创建合成品定义 6.编辑合成品定义 7.编辑合成品配比 8.创建套餐定义
# 9.编辑套餐定义 10.编辑套餐内容 11.创建售卖键 12.编辑售卖键 13.创建供货商 14.编辑供货商 15.创建采购协议 16.编辑采购协议

execute = 16

# 执行测试
if execute == 1:
    # 1.创建原材料
    material_create()
elif execute == 2:
    # 2.编辑原材料
    material_edit()
elif execute == 3:
    # 3.创建单品
    goods_create()
elif execute == 4:
    # 4.编辑单品
    goods_edit()
elif execute == 5:
    # 5.创建合成品定义
    mix_create()
elif execute == 6:
    # 6.编辑合成品定义
    mix_edit()
elif execute == 7:
    # 7.编辑合成品配比
    mix_match_edit()
elif execute == 8:
    # 8.创建套餐定义
    package_create()
elif execute == 9:
    # 9.编辑套餐定义
    package_edit()
elif execute == 10:
    # 10.编辑套餐内容
    package_match_edit()
elif execute == 11:
    # 11.创建售卖键
    sku_create()
elif execute == 12:
    # 12.编辑售卖键
    sku_edit()
elif execute == 13:
    # 13.创建供货商
    provider_create()
elif execute == 14:
    # 14.编辑供货商
    provider_edit()
elif execute == 15:
    # 15.创建采购协议
    order_protocol_create()
elif execute == 16:
    # 16.编辑采购协议
    order_protocol_edit()
else:
    print("请检查execute的参数是否正确")
