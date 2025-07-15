"""
20行代码3000个PPT完事!
一键爬取某PPT办公网站
https://www.ypppt.com/moban/
"""
import requests  # 导入请求模块
import re

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/131.0.0.0 Safari/537.36',
           'cookie': 'Hm_lvt_45db753385e6d769706e10062e3d6453=1733570196; HMACCOUNT=9FEB9E244BFC63B6; '
                     '__gads=ID=f0fa3df1c64ed93e:T=1733570197:RT=1733570197:S=ALNI_MaDcREMzLa6qfFkd5eKalP4vNJQtw; '
                     '__gpi=UID=00000f86db3a901e:T=1733570197:RT=1733570197:S=ALNI_MaTZfeNjLPceOPEpWgIQSvbCnY74w; '
                     '__eoi=ID=ea706b201002d7bc:T=1733570197:RT=1733570197:S=AA-AfjZeS6I-oAC6eAU3ejoP4_Vk; '
                     'Hm_lpvt_45db753385e6d769706e10062e3d6453=1733570351'}
page = 1
while True:
    # 获取PPT模版首页的数据
    if page == 1:
        url = 'https://www.ypppt.com/moban/'  # 准备一个网址
    else:
        url = f'https://www.ypppt.com/moban/list-{page}.html'

    resp = requests.get(url, headers=headers)  # 请求网站 得到响应
    if resp.status_code == 404:
        break
    resp.encoding = 'utf-8'  # 发现编码不对 改成万国码 utf-8
    # print(resp.text)
    # re正则
    # bs4
    # lxml
    'https://www.ypppt.com/moban/'  # 主页网址
    'https://www.ypppt.com/article/2024/16288.html'  # ppt页面网址
    'https://www.ypppt.com/p/d.php?aid=16288'  # 下载页面网址
    'https://down.ypppt.com/uploads/soft/240909/1-240Z91R306.pptx'  # 下载网址

    # 从得到的数据里面提取若干个id
    id_list = re.findall('href="/article/.*?/(.*?).html"class', resp.text)
    # print(id_list)

    # 把这些id拼接在'https://www.ypppt.com/p/d.php?aid='的后面
    for aid in id_list:
        url = 'https://www.ypppt.com/p/d.php?aid=' + aid
        # print(url)  # 请求这个网址

        # 请求具体的一个ppt下载页面链接
        resp = requests.get(url, headers=headers)
        # print(resp.text)

        # 得到下载链接 1 .zip 2 .rar 3 网盘链接 4 .pptx
        down_url = re.findall('<data href="(.*?)">下载地址1</data>', resp.text)[0]
        ppt_name = re.findall('<title>(.*?) - 下载页</title>', resp.text)[0]
        print(down_url)

        if 'pan.baidu' in down_url:
            continue
        else:
            # 得到后缀 https://down.ypppt.com/uploads/soft/240909/1-240Z91R306.pptx
            suffix = down_url.split('.')[-1]
            resp = requests.get(down_url, headers=headers)
            open(f'ppt模版/{ppt_name}-{aid}.{suffix}', 'wb').write(resp.content)  # 文件名.后缀名
    page += 1  # 爬完一页 page+=1


    # 翻页! 方法! 'https://www.ypppt.com/moban/list-1.html'
    # https://www.ypppt.com/moban/
    # https://www.ypppt.com/moban/list-2.html
    # https://www.ypppt.com/moban/list-3.html
    # https://www.ypppt.com/moban/list-4.html
