"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

print("第八步：让装饰器带 类 参数")
print("------示例8: 装饰器带类参数")
'''示例8: 装饰器带类参数'''


class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called. (这里是静态方法)")

    @staticmethod
    def release():
        print("  locker.release() called. (不需要对象实例化)")


def deco(cls):
    '''cls 必须实现acquire和release静态方法'''

    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()

            finally:
                cls.release()

        return __deco

    return _deco


@deco(locker)
def my_func():
    print("my_func() called.")


my_func()
my_func()

# before my_func called [<class '__main__.locker'>].
# locker.acquire() called. (这里是静态方法)
# my_func() called.
# locker.release() called. (不需要对象实例化)
# before my_func called [<class '__main__.locker'>].
# locker.acquire() called. (这里是静态方法)
# my_func() called.
# locker.release() called. (不需要对象实例化)
