from multiprocessing import Process
import time


def fun(name):
    print("{} 正在执行。。。".format(name))
    time.sleep(2)
    print("{} 执行完毕。。。".format(name))


if __name__ == '__main__':
    p = Process(target=fun, args=('Chancey',))  # 这里传参必须是以元组的形式传参
    p.start()
    print("主线程启动。。。")
