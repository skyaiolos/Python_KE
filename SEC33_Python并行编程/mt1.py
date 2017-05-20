import time
import datetime
import _thread

"""
#  Script Description:
    _thread 实现多线程
"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/10

def worker(n):
    start_time = time.ctime()
    s = datetime.datetime.now().second
    print('函数执行开始于：{}'.format(start_time))
    time.sleep(n)
    over_time = time.ctime()
    o = datetime.datetime.now().second
    user_sec = o - s
    # user_time = (over_time - start_time)
    print('函数执行结束于：{},所用时{}秒'.format(over_time, user_sec))


def main():
    print('主函数执行开始于：{}'.format(time.ctime()))
    _thread.start_new_thread(worker, (4,))
    _thread.start_new_thread(worker, (2,))
    time.sleep(5)
    print('主函数执行结束于：{}'.format(time.ctime()))


if __name__ == '__main__':
    main()
