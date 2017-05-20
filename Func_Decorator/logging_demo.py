"""
#  Script Description:
        http://docs.pythontab.com/interpy/decorators/logging/
        日志(Logging)

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/4/30
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    return x + x


result = addition_func(4)
