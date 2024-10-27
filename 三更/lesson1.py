# 把视频的链接存放在一个叫url的变量中！
url = ('https://vd3.bdstatic.com/mda-qjr4mvyyy0sprve1/sc/h264/1729912601236615561/mda-qjr4mvyyy0sprve1.mp4?v_from_s'
       '=bdapp-bdappcore-feed-nanjing')

# 导入一个requests的模块
import requests

# 用requests模块的get功能 给它一个网址 得到网址的回应
res = requests.get(url)

# 把得到的res.content保存在文件中
open('lesson1.mp4', 'wb').write(res.content)

print(res.status_code)
