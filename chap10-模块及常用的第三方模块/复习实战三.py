import jieba
from wordcloud import WordCloud

# 文件读取文本到字符串
if __name__ == '__main__':
    fp = open('华为手机.txt', 'r', encoding='utf-8')
    content = fp.read()
    lst = jieba.lcut(content)
    st = set(lst)
    content = ' '.join(st)

    wordcloud = WordCloud(font_path='Hiragino Sans GB.ttc',
                          background_color='white', width=800, height=600).generate(content)
    wordcloud.to_file('huawei.png')