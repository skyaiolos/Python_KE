"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/21
# File name ->

print("<第二步：使用装饰函数在函数执行前和执行后分别附加额外功能>")
print("------示例2: 替换函数(装饰)")
'''示例2: 替换函数(装饰)

装饰函数的参数是被装饰的函数对象，返回原函数对象

装饰的实质语句: my_func = deco(my_func)'''


def deco(func):
    print("Before my_func() called.")
    func()
    print("After my_func() called.")
    return func


def my_func():
    print("my_func() called")


print("装饰的实质语句: my_func = deco(my_func)'''")
myFunc = deco(my_func)
myFunc()
print('----------')
myFunc()

# 装饰的实质语句: my_func = deco(my_func)'''
# Before my_func() called.
# my_func() called
# After my_func() called.
# my_func() called
# ----------
# my_func() called