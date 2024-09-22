import datetime


def txt_to_m3u(input_file, output_file):
    try:
        # 读取 txt 文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"文件 {input_file} 不存在。")
        return

    # 打开 m3u 文件并写入内容
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    current_time = now.strftime("%m-%d %H:%M")
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U x-tvg-url="https://live.fanmingming.com/e.xml" catchup="append" catchup-source="?playseek=${(b)yyyyMMddHHmmss}-${(e)yyyyMMddHHmmss}"\n')
            f.write(f'#EXTINF:-1 group-title="💚更新时间{current_time}",河南卫视\n')
            f.write(f'http://61.163.181.78:9901/tsfile/live/1034_1.m3u8?key=txiptv&playlive=1&authid=0\n')

            # 初始化 genre 变量
            genre = ''
            # 遍历 txt 文件内容
            for line in lines:
                line = line.strip()
                if "," in line:  # 防止文件里面缺失",”号报错
                    channel_name, channel_url = line.split(',', 1)
                    if channel_url == '#genre#':
                        genre = channel_name
                    else:
                        # 将频道信息写入 m3u 文件
                        f.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-name="{channel_name}" tvg-logo="https://live.fanmingming.com/tv/{channel_name}.png" group-title="{genre}",{channel_name}\n')
                        f.write(f'{channel_url}\n')
    except IOError:
        print(f"无法写入文件 {output_file}。")


# 将txt文件转换为m3u文件
txt_to_m3u('yeye.txt', 'yeye.m3u')
