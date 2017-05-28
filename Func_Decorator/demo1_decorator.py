"""
#  Script Description:
    http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
    Python装饰器学习（九步入门） 

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/21
# File name ->

def my_func_try():
    print("using :", my_func_try.__name__)
    print(f"using : {my_func_try.__name__}")


my_func_try()

print("<第一步：最简单的函数，准备附加额外功能>")
print("------示例1: 最简单的函数,表示调用了两次")


def my_func():
    print("my_func() called")


my_func()
my_func()

# using : my_func_try
# using : my_func_try
# <第一步：最简单的函数，准备附加额外功能>
# ------示例1: 最简单的函数,表示调用了两次
# my_func() called
# my_func() called