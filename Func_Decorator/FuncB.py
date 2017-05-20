"""
#  Script Description:
        函数是可以嵌套的。


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/4/30

def hello(name):
    return 'Hello\t' + name


def action(name, func):
    return func(name)


print(action('Marry', hello))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def cal(x, y, func):
    return func(x, y)

print(cal(3, 5, add))
print(cal(3, 5, lambda x, y: x * y))
