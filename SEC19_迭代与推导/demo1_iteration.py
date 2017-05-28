"""
#  Script Description:
        迭代器
        

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/25
# File name ->

scores = [85, 76, 43, 23, 55, 99.11]

for s in scores:
    print(s)

print("---enumerate(scores)---")
for i, s in enumerate(scores):
    print(f"第{i + 1}门功课成绩是:{s}")
    print("--------------------")
    print("第%d门功课成绩是:%s" % (i + 1, s))
    print("--------------------")
    print("第{}门功课成绩是:{}".format((i + 1), s))
    print("====================")
