from moviepy.editor import VideoFileClip


def convert_mp4_to_wmv(input_file, output_file):
    # 读取 mp4 文件
    clip = VideoFileClip(input_file)

    # 写出为 wmv 文件
    clip.write_videofile(output_file, codec="libx264")


# 示例
convert_mp4_to_wmv("aaa.mp4", "aaa.wmv")
