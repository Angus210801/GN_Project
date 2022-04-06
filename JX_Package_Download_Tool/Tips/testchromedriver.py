total_size = int(file.headers['content-length'])
# 请求文件的大小单位字节B
total_size = int(file.headers['content-length'])
# 以下载的字节大小
content_size = 0
# 进度下载完成的百分比
plan = 0
# 请求开始的时间
start_time = time.time()
# 上秒的下载大小
temp_size = 0
# 开始下载每次请求1024字节
for content in file.iter_content(chunk_size=1024):
    zip_file.write(content)
    # 统计以下载大小
    content_size += len(content)
    # 计算下载进度
    plan = (content_size / total_size) * 100
    # 每一秒统计一次下载量
    if time.time() - start_time > 1:
        # 重置开始时间
        start_time = time.time()
        # 每秒的下载量
        speed = content_size - temp_size
        # KB级下载速度处理
        if 0 <= speed < (1024 ** 2):
            print('\r', onefloat(plan), '%', onefloat(speed / 1024), 'KB/s', end='')
        # MB级下载速度处理
        elif (1024 ** 2) <= speed < (1024 ** 3):
            print('\r', onefloat(plan), '%', onefloat(speed / (1024 ** 2)), 'MB/s', end='')
        # 重置以下载大小
        temp_size = content_size