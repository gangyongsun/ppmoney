from multiprocessing import Process

import time


def game(name):
    print('%s 正在玩游戏。。。' % name)
    time.sleep(4)
    print('%s 玩完游戏了。。。' % name)


def sing(name):
    print('%s 正在唱歌。。。' % name)
    time.sleep(2)
    print('%s 唱完歌了。。。' % name)


if __name__ == '__main__':
    p1 = Process(target=game, args=('Chancey',), daemon=True)
    p2 = Process(target=sing, args=('Kevin',))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("进程一：", p1.name, ' 执行结束')
    print("进程二：", p2.name, ' 执行结束')
