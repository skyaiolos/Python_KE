"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

print("<第四步：使用内嵌包装函数来确保每次新函数都被调用>")
print("------示例4: 使用内嵌包装函数来确保每次新函数都被调用")
'''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
    内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''


def deco(func):
    def _deco():
        print(" Before myfunc () called:")
        func()
        print("  After myfunc () called:")
        # 不需要返回func，实际上应返回原函数的返回值

    return _deco


@deco
def myfunc():
    print("myfunc() called.")
    return 'OK'


myfunc()
myfunc()
#  Before myfunc () called:
# myfunc() called.
#   After myfunc () called:
#  Before myfunc () called:
# myfunc() called.
#   After myfunc () called:
