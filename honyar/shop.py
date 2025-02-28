# 如何用代码循环打开浏览器 http://cp.wifenxiao.com/Dhs/user_list?name=62059182&mobile= 并点击按钮
import time

# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入自动化键盘操作
from DrissionPage.common import Keys, Actions

# python如何连接数据库
import pymysql
from collections import namedtuple

# 定义一个命名元组，用于存储每行查询结果
Record = namedtuple('Record', ['id', 'uid', 'rank'])

# 连接到 MySQL 数据库
conn = pymysql.connect(
    host='rm-bp1gxby0nmt9eccy07o.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    password='C5i1M8s6',
    database='hyaj',
    charset='utf8'
)

# 创建游标对象
cursor = conn.cursor()

# 执行查询 select id, uid, rank from o2o_user_change_dhs_rank where length(ifnull(uid,\'\'))>0 and length(ifnull(phone,
# \'\'))>0 and ifnull(flg,0)=0
cursor.execute("select id, uid, rank from o2o_user_change_dhs_rank where qs=1 and ifnull(flg, 0)=0")
# 使用对象列列表接收查询结果
records = [Record(*row) for row in cursor.fetchall()]

print('records.size()=', len(records))
for record in records:
    print(record.id, record.uid, record.rank)

# 关闭游标和数据库连接
cursor.close()
conn.close()


def updateFlg(id, flg):
    # 连接到数据库
    conn = pymysql.connect(
        host='rm-bp1gxby0nmt9eccy07o.mysql.rds.aliyuncs.com',
        port=3306,
        user='root',
        password='C5i1M8s6',
        database='hyaj',
        charset='utf8'
    )
    # 根据 uid 更新表
    try:
        with conn.cursor() as cursor:
            # 执行更新语句
            cursor.execute(f"UPDATE o2o_user_change_dhs_rank SET flg = '{flg}' WHERE id = '{id}'")
            # 提交事务
            conn.commit()
            print(f"更新成功，id={id}，flg={flg}")
    except Exception as e:
        # 发生错误时回滚事务
        conn.rollback()
        print(f"更新失败，id={id}，flg={flg}，错误信息：{e}")


def process_records(records, dp):
    for record in records:
        dp.get('http://cp.wifenxiao.com/Dhs/user_list')
        # 获取父元素
        searchbox = dp.ele('.tables-searchbox')
        # 在父元素作用域下查找 name="name" 的输入框 <input type="text" class="input mini" name="name" value="" placeholder="姓名/ID">
        name_input = searchbox.ele('.input mini')

        # 输入姓名到表单
        print('userId：' + record.uid)
        name_input.input(record.uid)  # 输入指定姓名或ID

        # 点击查询按钮
        search_button = searchbox.ele('.btn btn-primary')  # 定位查询按钮
        search_button.click()

        # 等待页面加载完成
        dp.wait.load_start()
        # 1: 分公司 (运营商-超级合伙人) 2: 总级订货商（内部员工）3: 省级订货商（鸿老板-合伙人）4：市级订货商（鸿师傅）5: 区级订货商（普通会员）
        # td = dp.ele('tag:a@@class=btn btn-new j-lower-dhs@@text()=设为内部员工')
        if record.rank == '4':
            td = dp.ele('tag:a@@class=btn btn-new j-lower-dhs@@text()=设为鸿师傅')
        else:
            td = dp.ele('tag:a@@class=btn btn-new j-lower-dhs@@text()=设为内部员工')
        if td:
            print("找到了按钮")
            td.click()  # 点击按钮

            sure = dp.ele('.jbox-buttons-ok btn btn-primary')
            if sure:
                sure.click()
                print("点击了确定按钮")
                # 调用 updateFlg
                updateFlg(record.id, '2')
            else:
                continue
        else:
            print("没有找到按钮,继续循环下一条记录")
            continue


# 打开浏览器
dp = ChromiumPage()
# 访问网站
dp.get('http://cp.wifenxiao.com/Dhs/user_list')
ac = Actions(dp)

# 如果页面有这个按钮,则需要登录 <button id="TencentLogin" data-appid="2099689224" data-cbfn="callback" type="button">登录</button>
login_button = dp.ele('#TencentLogin')

if login_button:
    # <input class="login-cont-ipt clearError" type="text" id="ipt_account" placeholder="请输入手机号码"> 输入账号
    # account_input = dp.ele('#ipt_account')
    # account_input.clear()
    # <input class="login-cont-pwd clearError" id="ipt_pwd" type="password" placeholder="请输入登录密码"> 输入密码
    # dp.ele('#ipt_pwd').clear()
    # dp.ele('#ipt_pwd').input('15857125375')
    # <button id="TencentLogin" data-appid="2099689224" data-cbfn="callback" type="button">登录</button> 点击登录
    login_button.click()
    # 等待 5 秒
    name = input("登录完毕,请输入n继续")
    if name == 'n':
        process_records(records, dp)
    else:
        print('非n则退出')
else:
    process_records(records, dp)
