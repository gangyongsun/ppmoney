from multiprocessing import Process
import time


def foo(name):
    print("进程{}输出：1".format(name))
    time.sleep(2)
    print("进程{}输出：2".format(name))
    time.sleep(3)
    print("进程{}输出：3".format(name))


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=foo, args=(i,))
        p.start()
