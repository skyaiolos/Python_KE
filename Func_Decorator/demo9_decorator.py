"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

print("第九步：装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器")
print("------示例9: 装饰器带类参数，并分拆公共类到其他py文件中")
'''示例9: 装饰器带类参数，并分拆公共类到其他py文件中

同时演示了对一个函数应用多个装饰器'''

from Func_Decorator.demo9_mylocker import *


class example:
    @lockhelper(mylocker)
    def my_func(self):
        print("my_func() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def my_func2(self, a, b):
        print(" my_func2() called")
        return a + b


if __name__ == '__main__':
    a = example()
    print('11111111111my_func()')
    a.my_func()
    print(a.my_func())

    print('2222222222my_func2()')
    print(a.my_func2(1, 2))
    print(a.my_func2(3, 4))
#
# before my_func called.
# mylocker.acquire() called
# my_func() called.
#   mylockder.unlock() called.
# before my_func called.
# mylocker.acquire() called
# my_func() called.
#   mylockder.unlock() called.
# None
# before __deco called.
# mylocker.acquire() called
# before my_func2 called.
# lockerex.acquire() called.
#  my_func2() called
#   lockerex.unlock() called.
#   mylockder.unlock() called.
# 3
# before __deco called.
# mylocker.acquire() called
# before my_func2 called.
# lockerex.acquire() called.
#  my_func2() called
#   lockerex.unlock() called.
#   mylockder.unlock() called.
7
