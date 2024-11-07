import jieba
from wordcloud import WordCloud

# 读取数据
# with open('华为手机.txt', 'r', encoding='utf-8') as file:
#     s = file.read()

with open('ltc.txt', 'r', encoding='utf-8') as file:
    s = file.read()

# 中文分词
lst = jieba.lcut(s)
# 排除词
stopword = ['用户体验', '需求', '反馈']

txt = ''.join(lst)
# 绘制词云图 msyh.ttc（微软雅黑）/System/Library/Fonts/PingFang.ttc
wordcloud = WordCloud(background_color='white', font_path='Hiragino Sans GB.ttc',
                      stopwords=stopword, width=800, height=600)

# 由txt生成词云图
wordcloud.generate(txt)
# 保存图片
# wordcloud.to_file('华为手机评价词云图.png')
wordcloud.to_file('ltc词云图.png')