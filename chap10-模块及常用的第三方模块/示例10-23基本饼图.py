# https://pyecharts.org/#/zh-cn/intro
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 准备数据
lst = [['华为', 1000], ['OPPO', '1200'], ['苹果', 3000], ['小米', 980]]
c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add('', lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="2028年北京手机出库占比情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("phone.html")
)
# [['可乐', 36], ['雪碧', 145], ['橙汁', 106], ['绿茶', 38], ['奶茶', 119], ['百威', 126], ['青岛', 114]]
# print([list(z) for z in zip(Faker.choose(), Faker.values())])
