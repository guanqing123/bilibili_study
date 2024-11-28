import json

import requests

url = ('https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime'
       '=1731286866879&mid=be6b2cb6b88921e52d9d8331b6cc6d0a&uuid=be6b2cb6b88921e52d9d8331b6cc6d0a&dfid'
       '=0R6kL02KhWCI0DHfpH0LEuxG&keyword=%E5%A4%A7%E9%B1%BC&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0'
       '&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature'
       '=30cfd3ebfa015977195f400585398216')

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/130.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)
# print(res.text) # callback123({})
result = res.text[12:-2]
song_json = json.loads(result)
lst = song_json["data"]["lists"]
# print(type(lst), lst)
for item in lst:
    print(f'歌曲: {item['SingerName'] + '-' + item['SongName']} \t 专辑：{item['AlbumName']}')

# 有很多参数需要加密了
url = ('https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1731288007216&mid'
       '=be6b2cb6b88921e52d9d8331b6cc6d0a&uuid=be6b2cb6b88921e52d9d8331b6cc6d0a&dfid=0R6kL02KhWCI0DHfpH0LEuxG&appid'
       '=1014&platid=4&encode_album_audio_id=n0800ae&token=&userid=0&signature=8e59b9ff8b2fd13192e7e811ad2283af')

url = ('https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1731288438878&mid'
       '=be6b2cb6b88921e52d9d8331b6cc6d0a&uuid=be6b2cb6b88921e52d9d8331b6cc6d0a&dfid=0R6kL02KhWCI0DHfpH0LEuxG&appid'
       '=1014&platid=4&encode_album_audio_id=1genmk88&token=&userid=0&signature=fe97b2bd383c336335e1791e599cfa2a')

# url = ('https://webfs.kugou.com/202411102154/9a121029532438263e3aaff797a26e6e/v3/bfbdd3df47727b701d4480ea36a8f73b/yp'
#        '/p_0_960111/ap1014_us0_mibe6b2cb6b88921e52d9d8331b6cc6d0a_pi406_mx38641536_s384134992.mp3')

# with open('大鱼.mp3', 'wb') as file:
#     file.write(res.content)
