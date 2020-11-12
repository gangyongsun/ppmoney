from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()  # 重用父类的init方法
        self.name = name

    def run(self):  # 重写父类方法
        print("{} 正在执行。。。".format(self.name))
        time.sleep(2)
        print("{} 执行完毕。。。".format(self.name))


if __name__ == '__main__':
    p = MyProcess('Chancey')
    p.start()
    print('主进程')
