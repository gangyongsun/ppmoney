from multiprocessing import Process
import time
import os


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("{} 正在执行。。。子进程ID：{}，父进程ID：{}".format(self.name, os.getpid(), os.getppid()))
        time.sleep(2)
        print("{} 执行完毕。。。子进程ID：{}，父进程ID：{}".format(self.name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    p1 = MyProcess('Chancey')
    p2 = MyProcess('Waller')

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('主进程', '父进程ID：', os.getpid(), '子进程ID：', os.getppid())

