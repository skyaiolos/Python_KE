"""
#  Script Description:
    '''mylocker.py: 公共类 for 示例9.py'''

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/21

'''demo9_mylocker.py: 公共类 for 示例9.py'''
class mylocker:
    def __init__(self):
        print("mylocker.__init__() called")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called")

    @staticmethod
    def unlock():
        print("  mylockder.unlock() called.")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")

def lockhelper(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco(*args,**kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args,**kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco