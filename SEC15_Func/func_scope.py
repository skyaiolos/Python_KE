"""
#  Script Description:
    函数作用域

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/14

x = 5


def func():
    global x
    x = 100
    print(x * 10)


print(x)

func()
print(x)
