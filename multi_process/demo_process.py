from multiprocessing import Process
import time
import os


def fun(name):
    print('{}正在执行'.format(name))
    # p = Process(target=time.sleep, args=(3,))
    # p.start()
    time.sleep(3)

if __name__ == '__main__':
    p = Process(target=fun, args=("Chancey",), daemon=True)
    p.start()
    p1 = Process(target=fun, args=("Kevin",), daemon=True)
    p1.start()
    p.join()
    p1.join()
    print("主进程", os.getpid(), os.getppid())
