import requests
import certifi

channel = '0140210'
# 输入一首歌曲的名称,用这个名称构造一个链接,请求这个链接,得到一系列歌曲的列表!
song_name = input('请输入歌曲名或者歌手名:')
url = (f'https://c.musicapp.migu.cn/v1.0/content/search_all.do?text={song_name}&pageNo=1'
       '&pageSize=20&isCopyright=1&sort=1&searchSwitch=%7B%22song%22%3A1%2C%22album%22%3A0%2C%22singer%22%3A0%2C'
       '%22tagSong%22%3A1%2C%22mvSong%22%3A0%2C%22bestShow%22%3A1%7D')
wz = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI '
                    'MiniProgramEnv/Mac MacWechat/WMPF XWEB/30626', 'channel': channel}
res = requests.get(url, headers=wz, verify=certifi.where())
JSON = res.json()

# JSON --> songResultData --> result 有歌曲列表
song_list = JSON['songResultData']['result']
index_list = []
for song_data in song_list:
    name = song_data['name']
    try:
        singers = song_data['singers'][0]['name']
    except:
        singers = '未知歌手'
    contentId = song_data['contentId']
    copyrightId = song_data['copyrightId']
    try:
        albumsId = song_data['albums'][0]['id']
        albums = song_data['albums'][0]['name']
    except:
        albums = '未知专辑'
        albumsId = ''
    index_list.append([name, singers, albums, contentId, copyrightId, albumsId])
    print(len(index_list), name, singers, albums)

choice = int(input('请输出序号选择:'))

# 根据歌曲信息,获取歌曲详情
url = f'https://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.3?copyrightId={index_list[choice - 1][4]}&contentId={index_list[choice - 1][3]}&resourceType=2&albumId={index_list[choice - 1][5]}&netType=01&toneFlag=PQ'
res = requests.get(url, headers=wz, verify=certifi.where())
JSON = res.json()

url = JSON['data']['url']
res = requests.get(url)
open(f'{index_list[choice - 1][0]}-{index_list[choice - 1][1]}-{index_list[choice - 1][2]}.mp3', 'wb').write(
    res.content)

# pip3 install pyinstaller
# pyinstaller --version
# pyinstaller -F -i music.png music.py
# pyinstaller music.spec
