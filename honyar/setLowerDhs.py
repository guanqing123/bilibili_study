import requests

url  = 'http://cp.wifenxiao.com/Dhs/set_lower_dhs?v=35'

# 创建一个列表
userIds = ['62059182']

# 遍历集合
for userId in userIds:
    # 设置headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36',
        'cookie': 'cache_account=15857125375; cache_pwd=; cache_pwd_checked=false; '
                  'PHPSESSID=db42de039078197a716a6364ab926f54; plat_env=fxcp; shop_id=4031216; '
                  'clientIp=103.88.46.225; user_auth=think%3A%7B%22sid%22%3A%224031216%22%2C%22last_time%22%3A'
                  '%221737430967%22%2C%22aid%22%3A%224010845%22%7D; '
                  'user_auth_sign=0ba5fee850d955966f6bb3ef19c3785749e278b3; r_token=8ec397e4e6e94199e52dfeb7c77eb7a8; '
                  f'user_lists_code=520341; redirect_url=%2FDhs%2Fuser_list%3Fname%3D{userId}%26mobile%3D',
        'referer': f'http://cp.wifenxiao.com/Dhs/user_list?name={userId}&mobile=',
        'Origin':'http://cp.wifenxiao.com',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
    # user_id=38892713&rank=2&pid=0 这个参数怎么传递
    url = url + '&user_id=' + userId + '&rank=2&pid=0'
    # 发起post请求
    response = requests.post(url=url, headers=headers)
    print(response.text)
