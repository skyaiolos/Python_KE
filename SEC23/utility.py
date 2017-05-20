"""
#  Script Description:
    @staticmethod   . 类里的静态方法。

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/13
class Utility:
    @staticmethod  # 只是纯粹的静态的方法
    def connect_db():
        print('链接数据库。。。')

    @staticmethod
    def upload_img():
        print('上传图片至指定的目录...')

    @staticmethod
    def other_method():
        pass


util = Utility()
util.connect_db()
util.upload_img()
util.other_method()
