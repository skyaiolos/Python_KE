import time
import datetime
import threading
import random

"""
#  Script Description:
    同步原语之：锁

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/10

eggs = []  # 放鸡蛋。
lock = threading.Lock()


def put_egg(n, lst):
    # lock.acquire()
    with lock:
        for i in range(1, n + 1):
            time.sleep(random.randint(0, 2))
            lst.append(i)
     # lock.release()


def main():
    threads = []

    for i in range(3):
        t = threading.Thread(target=put_egg, args=(5, eggs))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(eggs)


if __name__ == '__main__':
    main()
