from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()  # 重用父类的init
        self.name = name

    def run(self):  # 重写父类方法
        print("{} 正在执行。。。".format(self.name))
        time.sleep(2)
        print("{} 执行完毕。。。".format(self.name))


if __name__ == '__main__':
    p1 = MyProcess('Chancey')
    p2 = MyProcess('Waller')
    p3 = MyProcess('Mary')
    p4 = MyProcess('Arry')

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print('主进程')
