"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

print("第六步：对参数数量不确定的函数进行装饰")
print("------示例6: 对参数数量不确定的函数进行装饰")
'''示例6: 对参数数量不确定的函数进行装饰，

参数用(*args, **kwargs)，自动适应变参和命名参数'''


def deco(func):
    def _deco(*args, **kwargs):
        print("Before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("After %s called, result : %s" % (func.__name__, ret))
        return ret

    return _deco


@deco
def myfunc(a, b):
    print("myfunc(%s,%s) called." % (a, b))
    return a + b


@deco
def myfunc2(a, b, c):
    print("myfunc(%s,%s,%s) called." % (a, b, c))
    return a + b + c


myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)
# Before myfunc called.
# myfunc(1,2) called.
# After myfunc called, result : 3
# Before myfunc called.
# myfunc(3,4) called.
# After myfunc called, result : 7
# Before myfunc2 called.
# myfunc(1,2,3) called.
# After myfunc2 called, result : 6
# Before myfunc2 called.
# myfunc(3,4,5) called.
# After myfunc2 called, result : 12
