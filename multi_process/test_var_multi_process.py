from multiprocessing import Process

n = 0


def fun1():
    global n
    n = 100
    print('子进程中的变量：', n)


if __name__ == '__main__':
    p = Process(target=fun1)
    p.start()
    print('主进程中的变量：', n)
