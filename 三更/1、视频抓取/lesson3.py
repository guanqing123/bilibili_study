import requests

wz = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/130.0.0.0 Safari/537.36',
      'referer':'https://www.kuaishou.com/theater/10000'}
url = ('https://www.kuaishou.com/short-video/3x5ksr2jisj8aqi?streamSource=theater&tubeId=5x62wesbqak7uq2&thirdTab=%E7'
       '%9F%AD%E7%89%87&fromPage=theater&fromChannal=10000')
res = requests.get(url, headers=wz)
print(res.status_code)
print('text>>', res.text)

from bs4 import BeautifulSoup  # 从bs4导入BeautifulSoup

soup = BeautifulSoup(res.text, 'lxml')  # 把文本整理好得到soup

# 找到所有的<li class='col-4'> 得到了很多条目录的数据
lis = soup.find_all('li', class_='col-4')  # 查找全部
print(lis)
# 找出 data
for l in lis:
    l.find('data')

# 1.
# soup.find('x')      # 找到第一条<x>.......</x>
# soup.find_all('x')  # 找到所有<x>........</x>

# <li>.....</li>
# <li class>...</li>
