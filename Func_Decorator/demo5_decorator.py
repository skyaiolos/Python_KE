"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

print("第五步：对带参数的函数进行装饰")
print("------示例5: 对带参数的函数进行装饰")
'''示例5: 对带参数的函数进行装饰，

内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''


def deco(func):
    def _deco(a, b):
        print("Before myfunc() called.")
        ret = func(a, b)
        print("After myfunc() called, result : %s" % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print("myfunc(%s,%s) called." % (a, b))
    return a + b


myfunc(1, 2)
myfunc(3, 4)
# Before myfunc() called.
# myfunc(1,2) called.
# After myfunc() called, result : 3
# Before myfunc() called.
# myfunc(3,4) called.
# After myfunc() called, result : 7