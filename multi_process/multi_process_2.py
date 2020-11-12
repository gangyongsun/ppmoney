from multiprocessing import Process
import time


def fun(name):
    print("{} 正在执行。。。".format(name))
    time.sleep(2)
    print("{} 执行完毕。。。".format(name))


if __name__ == '__main__':
    # 实例化以得到四个对象
    p1 = Process(target=fun, args=('Chancey',))
    p2 = Process(target=fun, args=('Waller',))
    p3 = Process(target=fun, args=('Mary',))
    p4 = Process(target=fun, args=('Arry',))

    # 调用方法，开启四个进程
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print("主线程启动。。。")
