import requests


def bilibili_video_download():
    mp4_1 = ('https://upos-sz-estgcos.bilivideo.com/upgcxcode/17/66/449806617/449806617_x17-1-100026.m4s?e'
             '=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1753685835&oi=3662368422&nbs=1&uipk=5&platform=pc&gen=playurlv3&os=upos&trid=bf462a2d451143eb9b051c78838db9eu&og=cos&mid=504683999&upsig=b1715d56a7392840069351df66422c40&uparams=e,deadline,oi,nbs,uipk,platform,gen,os,trid,og,mid&bvc=vod&nettype=0&bw=949297&buvid=6A6A128E-4E11-5C0C-9268-5D7F12614C8044051infoc&build=0&dl=0&f=u_0_0&agrr=0&orderid=0,3')
    mp4_2 = ('https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/17/66/449806617/449806617_nb2-1-30280.m4s?e'
             '=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1753685835&trid=bf462a2d451143eb9b051c78838db9eu&og=cos&gen=playurlv3&os=cosbv&mid=504683999&oi=3662368422&nbs=1&uipk=5&platform=pc&upsig=df507b0e38652688f2e19807e1a1454d&uparams=e,deadline,trid,og,gen,os,mid,oi,nbs,uipk,platform&bvc=vod&nettype=0&bw=132783&build=0&dl=0&f=u_0_0&agrr=0&buvid=6A6A128E-4E11-5C0C-9268-5D7F12614C8044051infoc&orderid=0,3')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/138.0.0.0 Safari/537.36',
        'Referer': 'https://www.bilibili.com/video/BV1uY411s7Yj/?spm_id_from=333.337.search-card.all.click&vd_source'
                   '=50633961851476a9b0991ae7b138aa23'
    }

    mp4_resp = requests.get(mp4_1, headers=headers)
    with open('mp4_1.mp4', 'wb') as file:
        file.write(mp4_resp.content)
    mp4_resp = requests.get(mp4_2, headers=headers)
    with open('mp4_2.mp3', 'wb') as file:
        file.write(mp4_resp.content)

    from moviepy.editor import ffmpeg_tools
    # 将本地的mp4_1.mp4和mp4_2.mp3合成为 天地龙鳞.mp4
    ffmpeg_tools.ffmpeg_merge_video_audio('mp4_1.mp4', 'mp4_2.mp3', '天地龙鳞.mp4')


def douyin_video_download():
    mp4_1 = 'https://v3-web-prime.douyinvod.com/video/tos/cn/tos-cn-vd-0026/ooAreWaWDACvE6s4AYFACD9h4BfhoAAREPg1AX/media-audio-und-mp4a/?a=6383&ch=0&cr=8&dr=0&er=1&lr=default&cd=0%7C0%7C0%7C3&cv=1&br=127&bt=127&cs=4&mime_type=video_mp4&qs=15&rc=ZmlnZmloaGdoOTtoOGVkZkBpM3ZwcHA5cjtwNDMzNGkzM0AxMTYyYS0wNV8wMzQ1LjMtYSMubGoyMmRjcGJhLS1kLS9zcw%3D%3D&btag=80000e00030000&cquery=100o_101s&dy_q=1753705389&expire=1753792036&l=2025072820230848CB35C7E79A1ACFFCEB&ply_type=4&policy=4&signature=fb2fa898029ccdccfff0329095bd74ca&tk=webid&webid=63dd93172fb5fdaa8078f33ae0ba1106c8e3f1f870eecbc4b54b497d452c3517503a1b448454e061402c41a1a5c8f04d0c3361cfaf2549f878b809eee3da7aa0f8123229101554b9625e604b868a8f4c3c00e6e314300d552cd9c74e6fc44ee62b37fe3bc8737d557375cde042dc7fb119149c76a4b35bd06f75b2abfda1d16b7a6e3728c6095dedb38c141f1c6e6e05f61a2ccc97e657a34a0f3e8e11a6ff91-d7cd83533d5a53336ba46109263cefae&fid=a6dc9478b1e9959317b1db4a739c7f36'
    mp4_2 = 'https://v3-web-prime.douyinvod.com/video/tos/cn/tos-cn-vd-0026/ooAreWaWDACvE6s4AYFACD9h4BfhoAAREPg1AX/media-video-hvc1/?a=6383&ch=0&cr=8&dr=0&er=1&lr=default&cd=0%7C0%7C0%7C3&cv=1&br=1038&bt=1038&cs=4&mime_type=video_mp4&qs=15&rc=aWQzOTdkaGdnZWc7OmlkZEBpM3ZwcHA5cjtwNDMzNGkzM0A0NjM0X15fXzUxXjFgXjUuYSMubGoyMmRjcGJhLS1kLS9zcw%3D%3D&btag=80000e00030000&cquery=101s_100o&dy_q=1753705389&expire=1753792036&l=2025072820230848CB35C7E79A1ACFFCEB&ply_type=4&policy=4&signature=eb4a434cec8ec514ca22de9e0eb59f05&tk=webid&webid=63dd93172fb5fdaa8078f33ae0ba1106c8e3f1f870eecbc4b54b497d452c3517503a1b448454e061402c41a1a5c8f04d0c3361cfaf2549f878b809eee3da7aa0f8123229101554b9625e604b868a8f4c3c00e6e314300d552cd9c74e6fc44ee62b37fe3bc8737d557375cde042dc7fb119149c76a4b35bd06f75b2abfda1d16b7a6e3728c6095dedb38c141f1c6e6e05f61a2ccc97e657a34a0f3e8e11a6ff91-d7cd83533d5a53336ba46109263cefae&fid=a6dc9478b1e9959317b1db4a739c7f36'

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/138.0.0.0 Safari/537.36'
    }
    mp4_resp = requests.get(mp4_1, headers=header)
    with open('dou.mp4', 'wb') as file:
        file.write(mp4_resp.content)
    mp4_resp = requests.get(mp4_2, headers=header)
    with open('yin.mp4', 'wb') as file:
        file.write(mp4_resp.content)

    from moviepy.editor import ffmpeg_tools
    ffmpeg_tools.ffmpeg_merge_video_audio('dou.mp4', 'yin.mp4', 'douyin.mp4')


if __name__ == '__main__':
    # bilibili_video_download()
    douyin_video_download()
