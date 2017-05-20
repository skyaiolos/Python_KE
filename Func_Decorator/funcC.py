"""
#  Script Description:
        函数工具，简单装饰器
        @staticmethod
        @classmethod
        @property
    @app.route()
    def func():
    pass

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/4/30
def p_decorator(func):
    def func_wrapper(msg):
        # return '<p>' + func(msg) + '</p>'
        return f'<p>{func(msg)}</p>'

    return func_wrapper

def div_decorator(func):
    def func_wrapper(msg):
        return f'<div>{func(msg)}</div>'

    return func_wrapper

@div_decorator
@p_decorator
def get_text(msg):
    return 'HTML 修饰 ' + msg

# html_p = p_decorator(get_text)
print(get_text('优品课堂'))
