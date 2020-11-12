from multiprocessing import Process, Lock
import time


def foo(i, mutex):
    mutex.acquire()
    print("进程{}输出：1".format(i))
    time.sleep(2)
    print("进程{}输出：2".format(i))
    time.sleep(1)
    print("进程{}输出：3".format(i))
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(3):
        p = Process(target=foo, args=(i, mutex))
        p.start()
