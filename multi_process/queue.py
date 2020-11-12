from multiprocessing import Queue
from queue import Queue
q = Queue()

for i in range(5):
    q.put(i)
    print('队列是否已满：', q.full())
    print('队列大小：', q.qsize())

for i in range(5):
    q.get()
    print('取出一个消息')
    print('队列是否为空：', q.empty())
