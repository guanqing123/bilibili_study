# 导入requests模块
import requests

url = 'http://extshort.weixin.qq.com/mmtls/22454a51'

wz = {'user-agent': 'MicroMessenger Client'}

res = requests.get(url, headers=wz)
open('wx.mp4', 'wb').write(res.content)
print(res.status_code)
