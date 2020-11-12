from threading import Thread
import time


def MyThread(name):
    print('%s 正在执行。。。。' % name)
    time.sleep(2)
    print('%s 执行完毕。。。。' % name)


if __name__ == '__main__':
    t1 = Thread(target=MyThread, args=('chancey',))
    t1.start()
    print("主线程")
