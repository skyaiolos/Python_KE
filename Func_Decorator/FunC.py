"""
#  Script Description:
        函数嵌套


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/4/30

def hello(name):
    def get_message():
        return 'hello,'

    result = get_message() + name
    return result


print(hello('Jerry'))
