import requests

# url = "https://www.baidu.com/"
# cookies = {"name": "cookie-test"}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
#                   "Safari/537.36"
# }

# resp = requests.get(url=url, headers=headers)
# 方式一：resp.text 获取到的是字符串
# print(resp.text)

# 方式二：resp.content 获取到的是原始的二进制数据(bytes)
# decode() 二进制转字符串
# print(resp.content.decode())

# 获取响应码
# print(resp.status_code)
# 获取响应头
# print(f'响应头 : {resp.headers}')
# print(type(resp.cookies), resp.cookies)

# 获取请求头
# {'User-Agent': 'python-requests/2.32.3',
#  'Accept-Encoding': 'gzip, deflate, br',
#  'Accept': '*/*',
#  'Connection': 'keep-alive',
#  'Cookie': 'name=cookie-test'}
# print(resp.request.headers)
# 获取请求cookies
# print(resp.request._cookies)

# url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

# 发送请求获取响应信息
# resp = requests.get(url=url, headers=headers)

# 下载网页
# with open("baidu.html", "w", encoding="utf-8") as f:
#     f.write(resp.content.decode())

# 下载图片
# with open("baidu.png", "wb") as f:
#     f.write(resp.content)

# 下载网易云音乐
url = "https://m804.music.126.net/20250725091320/0a068004683dee9d4711ff2b0c492da9/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/18192765420/f612/0439/b743/04d72caccf53a1ef68eeeff0bd4e6fbd.m4a?vuutv=MBsnZwP9hjPZmFeTesYemuidGuOCwaTLFC7NbWens1bYErJkk/6+oLvtHRDgIaYIArZ4uzBtzmqTU7eRi4Ap+Hk3XXsOwivZvvsxaBsNLiU=&authSecret=000001983f0d686d16eb0a32b0150006"
resp = requests.get(url=url)
with open("wy.mp3", "wb") as f:
    f.write(resp.content)
