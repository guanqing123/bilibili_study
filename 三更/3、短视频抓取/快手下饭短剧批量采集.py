import requests
import re
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

name = input('请输入短视频名称:')

if not os.path.exists(name):
    os.makedirs(name)

# 快手小短剧 https://www.kuaishou.com/theater/0
url = 'https://www.kuaishou.com/graphql'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/130.0.0.0 Safari/537.36'}
episodeNumber = 28
while True:
    data = {
        "operationName": "visionTubeEpisodeQuery",
        "variables": {
            "tubeId": "5xenu4z4qybseia",
            "episodeNumber": episodeNumber,
            "page": "theater",
            "channelId": 0
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionTubeEpisodeQuery($tubeId: String, $episodeNumber: Int, $page: String, $channelId: Int, $webPageArea: String) {\n  visionTubeEpisode(tubeId: $tubeId, episodeNumber: $episodeNumber, page: $page, channelId: $channelId, webPageArea: $webPageArea) {\n    ...feedContent\n    result\n    status\n    __typename\n  }\n}\n"
    }
    res = requests.post(url, headers=headers, json=data)

    # 正则表达式去提取res.text中的视频链接
    down_url = re.findall('"photoUrl":"(.*?)",', res.text)[0]
    down_res = requests.get(down_url, headers=headers)
    open(f'{name}/第{episodeNumber + 1}集.mp4', 'wb').write(down_res.content)
    episodeNumber += 1

clips = []
for i in range(1, episodeNumber):
    # 加载视频剪辑
    clips.append(VideoFileClip(f'{name}/第{i}集.mp4'))

# 合并视频
final_clip = concatenate_videoclips(clips, method="compose")
# 导出合并后的视频
final_clip.write_videofile(f'{name}/完整视频.mp4', codec="libx264", fps=24)
