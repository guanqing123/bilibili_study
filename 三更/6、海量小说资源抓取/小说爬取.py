import os.path

import requests
from bs4 import BeautifulSoup

wz = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/130.0.0.0 Safari/537.36'}
url = 'https://book.zongheng.com/showchapter/1284449.html'
res = requests.get(url, headers=wz)
# print(res.text)

path = '闪婚傲娇女总裁'
if not os.path.exists(path):
    os.makedirs(path)

soup = BeautifulSoup(res.text, 'lxml')  # 把文本整理好,得到soup
# print(soup)
# 找到了所有的<li class='col-4'> 得到了很多条目录的数据！
lis = soup.find_all('li', class_="col-4")
for l in lis:
    a = l.find('a')
    title = a.text
    href = a.get('href')
    print(title, href)
    res = requests.get(href, headers=wz)
    soup = BeautifulSoup(res.text, 'lxml')
    content = soup.find('div', class_='content')
    format_content = '\n'.join(content.stripped_strings)
    open(f'{path}/{title}.txt', 'w').write(format_content)
