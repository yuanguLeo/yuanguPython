from selenium import webdriver
import time


# 相关设置
username = "rogersun"
password = "admin123"
group_code = '16161616'


# CONFIG (e.g. runtime = 21 活动名称为 常规活动180831-21-97) 用于防止重名
run_time = time.strftime("%H%M-%Y%m%d", time.localtime())
print(run_time)

# 需要创建的数量（循环次数 设置end_num为要执行的次数）
start_mum = 0
end_num = 5

# 是否开启审批流 (True \ False)
# 备注：如果编辑的是没有审核通过的数据也需要设置成False，除了合成品配比和套餐内容
# 如果混合出现待审核和通过的状态，懒得适配代码了，手动审核通过后执行
is_workflow_on = True


# 创建浏览器
b = webdriver.Chrome()
# Windows窗口最大化
# b.maximize_window()
# Mac系统窗口最大化
b.fullscreen_window()
