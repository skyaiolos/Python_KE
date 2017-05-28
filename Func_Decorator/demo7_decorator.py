"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

print("第七步：让装饰器带参数")
print("------示例7: 在示例4的基础上，让装饰器带参数")
'''示例7: 在示例4的基础上，让装饰器带参数，

和上一示例相比在外层多了一层包装。
装饰函数名实际上应更有意义些'''


def deco(arg):
    def _deco(func):
        def __deco():
            print("Before %s called [%s]" % (func.__name__, arg))
            func()
            print(" After %s called [%s]" % (func.__name__, arg))

        return __deco

    return _deco


@deco('my_module')
def my_func():
    print("my_func() called")


@deco("module2")
def my_func2():
    print("my_func2() called")


my_func()
my_func2()
# Before my_func called [my_module]
# my_func() called
#  After my_func called [my_module]
# Before my_func2 called [module2]
# my_func2() called
#  After my_func2 called [module2]
