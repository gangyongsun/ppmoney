#!/user/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool
import time
import os
from util.common_util import walk_file


def word(files, index):
    print(os.path.basename(files[index]), str(os.path.getsize(files[index])) + 'B')
    time.sleep(1)


if __name__ == '__main__':
    # 遍历主文件夹
    slip_files = walk_file(path='/Users/alvin/Documents/Goldwind/数字化/故障可视化/1.5modle/', start_flag=None, end_flag='.txt.tmp1')
    size = len(slip_files)
    core_num = os.cpu_count()

    pool = Pool(processes=core_num)  # 申请的进程数
    for i in range(0, size):
        pool.apply_async(word, (slip_files, i,))  # 异步执行，非阻塞方式
    pool.close()  # 关闭进程池，关闭之后，不能再向进程池中添加进程
    pool.join()  # 当进程池中的所有进程执行完后，主进程才可以继续执行
