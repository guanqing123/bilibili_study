# import requests

# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
# }
# url = 'https://movie.douban.com/top250'
# # 发送请求
# resp = requests.get(url=url, headers=headers)
# with open('douban.html', 'w', encoding='utf-8') as f:
#     f.write(resp.content.decode())

"""
1、导入lxml
2、将获取到的网页内容转换为xml
3、通过xpath去定位和解析页面中的内容

xpath数据提取的技巧：
    1、定位到包含所有数据的元素 //ol
    2、再从中找到包含单条数据所有内容的元素 //ol/li
    3、对定位到包含所有元素的列表进行遍历,得到包含单条数据的元素
    4、再提取单条数据中的详细内容
"""
import requests
from lxml import etree

# 读取html页面内容(请求得到的response.content.decode())
page = open('douban.html', 'r', encoding='utf-8').read()

# 将html页面内容转换为xml文档对象
html = etree.HTML(page)

# 一、直接提取
# 使用xpath语法提取页面数据
# titles = html.xpath("//*[@class='title'][1]/text()")
# scores = html.xpath("//*[@class='rating_num']/text()")
# print(titles)
# print(scores)

# # 定位到包含单条数据所有内容的元素
# data_list = html.xpath("//ol/li")
# # 对定位到包含所有元素的列表进行遍历,得到包含单条数据的元素
# for li in data_list:
#     # 提单条数据中的详细内容
#     title = li.xpath(".//span[@class='title'][1]/text()")
#     score = li.xpath(".//span[@class='rating_num'][1]/text()")
#     number = li.xpath(".//div[@class='info']/div[@class='bd']/div/span[last()]/text()")
#     print(f'标题:{title[0]} \t 评分:{score[0]}, \t 评价人数:{number[0]}')


'''
1、准备好top250电影数据所有的url地址,放在一个列表中

2、遍历列表中的url地址,进行抓取

3、代码优化
'''


# 二、函数方式
# def get_data(url):
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
#     }
#     resp = requests.get(url, headers=headers)
#     html = etree.HTML(resp.content.decode())
#     data_list = html.xpath("//ol/li")
#
#     for li in data_list:
#         title = li.xpath(".//span[@class='title'][1]/text()")
#         score = li.xpath(".//span[@class='rating_num'][1]/text()")
#         number = li.xpath(".//div[@class='info']/div[@class='bd']/div/span[last()]/text()")
#         print(f'标题:{title[0]} \t 评分:{score[0]}, \t 评价人数:{number[0]}')
#
#
# if __name__ == '__main__':
#     for i in range(0, 10):
#         url = f'https://movie.douban.com/top250?start={i*25}&filter='
#         get_data(url)

# 三、面向对象
class DouBan:
    base_url = 'https://movie.douban.com/top250?start={}&filter='

    def __init__(self):
        # 定义一个属性用来保存所有的url地址
        self.url_list = []
        # 生成所有页面的url地址保存到url_list属性中
        for i in range(0, 10):
            url = self.base_url.format(i * 25)
            self.url_list.append(url)

    def get_page_data(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        resp = requests.get(url, headers=headers)
        html = etree.HTML(resp.content.decode())
        data_list = html.xpath("//ol/li")

        for li in data_list:
            title = li.xpath(".//span[@class='title'][1]/text()")
            score = li.xpath(".//span[@class='rating_num'][1]/text()")
            number = li.xpath(".//div[@class='info']/div[@class='bd']/div/span[last()]/text()")
            print(f'标题:{title[0]} \t 评分:{score[0]}, \t 评价人数:{number[0]}')

    def run(self):
        for url in self.url_list:
            self.get_page_data(url)


if __name__ == '__main__':
    douban = DouBan()
    douban.run()
