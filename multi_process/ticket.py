from multiprocessing import Process, Lock
import time


def search(name):
    time.sleep(1)
    with open('data.txt') as f:
        count = int(f.read())
    print('<%s> 查看到剩余票数【%s】' % (name, count))


def get(name):
    time.sleep(1)
    f = open('data.txt')
    count = f.read()
    f.close()
    count = int(count)
    if count > 0:
        count -= 1
        time.sleep(1)
        f = open('data.txt', 'w')
        f.write(str(count))
        f.close()
        print('<%s> 购票成功' % name)


def start(name, mutex):
    search(name)
    mutex.acquire()
    get(name)
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(5):
        p = Process(target=start, args=('顾客%s' % i, mutex))
        p.start()
