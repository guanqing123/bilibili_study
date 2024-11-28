import os.path
import tkinter as tk
from threading import Thread

from DrissionPage import ChromiumPage, ChromiumOptions

import requests


def download_video():
    url = url_entry.get()

    co = ChromiumOptions()
    co.headless()

    driver = ChromiumPage(co)

    # 去请求博主的首页网址
    driver.get(url)

    # 数据监听 这段代码什么作用
    driver.listen.start(
        'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_****',
        method='GET'
    )

    # 等待数据包加载
    resp = driver.listen.wait()
    # 获取我们的响应数据
    data = resp.response.body

    a = data['aweme_list'][0]['author']['nickname']
    paths = f'./{a}'

    if not os.path.exists(paths):
        os.mkdir(paths)

    a = 1
    for i in data['aweme_list']:
        sp_url = i['video']['play_addr']['url_list'][-1]
        sp_res = requests.get(sp_url)
        file_path = os.path.join(paths, f'{a}.mp4')
        with open(file_path, 'wb') as f:
            f.write(sp_res.content)
        a = a + 1
        sp_name = i['desc']
        output_text.insert(tk.END, f'{sp_name}下载成功')
        output_text.yview(tk.END)


# 创建多线程 两个线程
def start_download_thread():
    download_thread = Thread(target=download_video)  # 运行下载函数
    download_thread.start()  # 启动函数就执行函数


root = tk.Tk()
root.title("VIP视频下载")

root.geometry("600x500")

url_label = tk.Label(root, text="请输入博主链接")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# 确认按钮
start_button = tk.Button(root, text="开始下载", command=start_download_thread)
start_button.pack(pady=10)

output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=10)

# 运行主循环
root.mainloop()

# 封包
# pyinstaller --onefile --noconsole 文件名.py
# 安卓 apk
# 苹果 ipa
# exe
