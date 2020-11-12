n = 0


def fun1():
    global n
    n = 100
    print(n)


def fun2():
    print(n)


if __name__ == '__main__':
    fun1()
    fun2()
