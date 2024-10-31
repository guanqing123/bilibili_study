# 导入requests模块
import requests

url = 'https://sns-video-qc.xhscdn.com/stream/110/4/01e71d90957480b50103700392cb7dce10_4.mp4?sign=83719de3d4f4450c52f9971b05d61e45&t=67268b89'

wz = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

res = requests.get(url, headers=wz)
open('abc.mp4', 'wb').write(res.content)
print(res.status_code)
