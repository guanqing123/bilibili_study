import requests

url = "http://cp.wifenxiao.com/Dhs/set_lower_dhs?v=65"
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/131.0.0.0 Safari/537.36",
    "Cookie": 'cache_account=15857125375; cache_pwd=; cache_pwd_checked=false; '
                  'PHPSESSID=db42de039078197a716a6364ab926f54; plat_env=fxcp; db_id=27; '
                  'user_auth=think%3A%7B%22sid%22%3A%224031216%22%2C%22last_time%22%3A%221737423608%22%2C%22aid%22%3A'
                  '%224010845%22%7D; user_auth_sign=702da04ca837c481d8148c89c9a3599051964bae; shop_id=4031216; '
                  'r_token=cb8aa989a8457befbe4f425764e8f3ce; user_lists_code=320048; '
                  'redirect_url=%2FDhs%2Fuser_list%3Fname%3D38892713%26mobile%3D'
}
data = {
    "user_id": "62065980",
    "rank": "2",
    "pid": "0"
}
response = requests.post(url, headers=headers, data=data)
print(response.text)
