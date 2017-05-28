"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/21

def myfunc():
    print("myfunc() called")


print("<第三步：使用语法糖@来装饰函数>")

print("-----示例3: 使用语法糖@来装饰函数，相当于“my_func = deco(my_func)")
'''示例3: 使用语法糖@来装饰函数，相当于“my_func = deco(my_func)”

但发现新函数只在第一次被调用，且原函数多调用了一次'''


def deco(func):
    print("Before my_func() called.")
    func()
    print("After my_func() called.")
    return func


@deco
def my_func():
    print("my_func() called")


my_func()
my_func()

# Before my_func() called.
# my_func() called
# After my_func() called.
# my_func() called
# my_func() called
