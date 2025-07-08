import pandas as pd
import matplotlib.pylab as plt

# import matplotlib.font_manager as fm
# lst = [f.name for f in fm.fontManager.ttflist]
# print(lst)

# 读取Excel文件
df = pd.read_excel('JD手机销售数据.xlsx')
print(df)
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['Songti SC']
# 设置画布的大小
plt.figure(figsize=(10, 6))
labels = df['商品名称']
y = df['北京出库销量']
print(labels)
print(y)

# 绘制饼图
plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90)

# 设置x,y轴刻度
plt.axis('equal')
plt.title('2028年1月北京各手机品牌出库量占比图')
# 显示出来
plt.show()
