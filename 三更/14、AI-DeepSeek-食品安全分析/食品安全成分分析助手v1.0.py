# 开启摄像头 pip3 install opencv-python
# pip3 install pandas
# pip3 install pyzbar
import time

import cv2
import pandas as pd
# raise ImportError('Unable to find zbar shared library')
# ImportError: Unable to find zbar shared library
# 缺少zbar库，请安装zbar brew list zbar
# sudo ln -s $(brew --prefix zbar)/lib/libzbar.dylib /usr/local/lib/libzbar.dylib
from pyzbar import pyzbar
import requests

url = "https://api.deepseek.com/chat/completions"
headers = {
    'Authorization': 'Bearer sk-c2dff78f06364094a863a4d74a2b3c37',
    'Content-Type': 'application/json'
}

last_barcode = ''  # 定义一个最后一次识别到的条形码

cap = cv2.VideoCapture(0)  # 0 1 打开摄像头

# 读取表格的数据 在现实的项目中，数据一般会保存在数据库中，这里我们使用表格
df = pd.read_excel('products.xlsx')
# 为了保证100%成功!
df['条形码'] = df['条形码'].astype(str)


# 通过条形码数值查表/数据库
def lookup_product(barcode_data):
    if df is None:  # 如果表格为空
        return None
    result = df[df['条形码'] == barcode_data]  # 查找所有符合的结果!
    if not result.empty:  # 如果查询的结果非空
        product_info = result.iloc[0]  # 获取商品的信息
        return {
            '条形码': product_info['条形码'],
            '产品名称': product_info['产品名称'],
            '产品类型': product_info['产品类型'],
            '配料': product_info['配料'],
            '食品添加剂': product_info['食品添加剂']
        }
    else:
        return None  # 没有查询到结果


# 扫描条形码
def scan_barcode(frame):  # 拿来一帧图像
    global last_barcode
    barcodes = pyzbar.decode(frame)

    # 遍历识别的每一个条形码
    for barcode in barcodes:
        # 辅助画框 数字也写出来
        x, y, w, h = barcode.rect  # 获取条形码的矩形框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcode_data = barcode.data.decode('utf-8')
        cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # barcode_data 就是条形码的数值 拿这个数字取查询表格/数据库
        print(f'获取到条形码:{barcode_data}')
        product_info = lookup_product(barcode_data)
        if product_info['条形码'] != last_barcode:  # 如果这次识别到的条形码和上次识别到的条形码不一致
            print(product_info)

        # 把product_info 提交给大模型
        # sk-c2dff78f06364094a863a4d74a2b3c37

        json = {
            "model": "deepseek-chat",  # deepseek v3大模型
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个安全专家，负责评估食品的ngsafe.com"
                },
                {
                    "role": "user",
                    "content": f"请对以下信息进行评估，并给出相应的建议：\n条形码：{product_info['条形码']}\n产品名称：{product_info['产品名称']}\n产品类型：{product_info['产品类型']}\n"
                }
            ]
        }
        response = requests.post(url=url, headers=headers, json=json)
        result = response.json()
        print(result['choices'][0]['message']['content'])
        (open(f'{product_info["产品名称"]}-{product_info["条形码"]}.md', 'w', encoding='utf-8')
         .write(result['choices'][0]['message']['content']))
        last_barcode = barcode_data  # 记录最后一次识别到的条形码

    # print(barcodes, type(barcodes))
    return frame  # 处理完成之后 返回


while True:
    _, frame = cap.read()  # 获取到一帧图像
    frame = scan_barcode(frame)  # 调用扫描函数
    cv2.imshow('zbar', frame)  # 显示这一帧图像
    cv2.waitKey(20)  # 保持窗口

# 界面卡住了, 开线程 让AI查询这个功能重新开一个线程去处理！
# 缓存! 商品 先查有没有现成的分析报告 有的话 就直接返回 没有的话 才去查AI
