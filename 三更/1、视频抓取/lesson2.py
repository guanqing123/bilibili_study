# 导入requests模块
import requests

url = ('https://cn-zjhz3-wasu-bcache-20.bilivideo.com/upgcxcode/19/94/26415599419/26415599419-1-100026.m4s?e'
       '=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1730006025&gen=playurlv2&os=bcache&oi=979676176&trid=00005d2e1404549c4aeda639072c5c2f6af9u&mid=504683999&platform=pc&og=cos&upsig=4c02827cbe545fc6e5e83bbf472e73fe&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=20027&bvc=vod&nettype=0&orderid=0,3&buvid=6A6A128E-4E11-5C0C-9268-5D7F12614C8044051infoc&build=0&f=u_0_0&agrr=0&bw=60333&logo=80000000')
wz = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV17UypYyE2p/?spm_id_from=333.1007.tianma.9-1-26.click&vd_source=50633961851476a9b0991ae7b138aa23'}
res = requests.get(url, headers=wz)
open('lesson2.avi', 'wb').write(res.content)
print(res.status_code)

url = ('https://cn-zjhz3-wasu-bcache-14.bilivideo.com/upgcxcode/19/94/26415599419/26415599419-1-30280.m4s?e'
       '=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1730006025&gen=playurlv2&os=bcache&oi=979676176&trid=00005d2e1404549c4aeda639072c5c2f6af9u&mid=504683999&platform=pc&og=hw&upsig=c146637fddda1554b1614b40d489fb5a&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=20021&bvc=vod&nettype=0&orderid=0,3&buvid=6A6A128E-4E11-5C0C-9268-5D7F12614C8044051infoc&build=0&f=u_0_0&agrr=0&bw=13773&logo=80000000')
wz = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV17UypYyE2p/?spm_id_from=333.1007.tianma.9-1-26.click&vd_source=50633961851476a9b0991ae7b138aa23'}
res = requests.get(url, headers=wz)
open('lesson2.mp3', 'wb').write(res.content)
print(res.status_code)

import subprocess


def merge_avi_mp3(video_path, audio_path, output_path):
    # 构建 ffmpeg 命令
    command = [
        'ffmpeg', '-i', video_path, '-i', audio_path,
        '-c:v', 'copy', '-c:a', 'aac',  # 保留原视频编码，使用 AAC 编码音频
        '-strict', 'experimental', output_path
    ]

    try:
        # 运行命令
        subprocess.run(command, check=True)
        print(f"合并成功！输出文件：{output_path}")
    except subprocess.CalledProcessError as e:
        print(f"合并失败：{e}")


# 示例调用 brew install ffmpeg
merge_avi_mp3('lesson2.avi', 'lesson2.mp3', 'output.mp4')

# # 1.导入一个模块！
# from moviepy.editor import *
# #
# video = VideoFileClip('lesson2.mp4')  # 2.加载素材！
# audio = AudioFileClip('lesson2.mp3')
# final = video.set_audio(audio)  # 3.给视频设置音频!
# final.write_videofile('完整视频.avi')  # 4.保存下来！
