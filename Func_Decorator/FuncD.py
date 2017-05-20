"""
#  Script Description:
        装饰器定义
"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/4/30

def tags(tag_name):
    def tag_decorate(func):
        def wrapper(*args, **kwargs):  # *args 表示在当前的位置可以传入任意一个参数。
            return '<{0}>{1}</{0}>'.format(tag_name, func(*args, **kwargs))  # **kwargs 表示以字典表为参数进行传递

        return wrapper

    return tag_decorate

@tags('div')
@tags('span')
@tags('b')
def get_text(msg):
    return 'HTML' + msg


print(get_text('优品课堂'))
