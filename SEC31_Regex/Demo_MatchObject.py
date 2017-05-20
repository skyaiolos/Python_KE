"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/7
import re

text = 'Tom is 8 years old, Jerry is 23 years old'
p1 = re.compile(r'\d+')
p2 = re.compile(r'(\d+).*?(\d+)')
print(p1.findall(text))
m = p2.search(text)
print(m)
print(m.group(0))
print(m.group(1), 'index is: ', m.start(1), ',end is: ', m.end(1))
print(m.group(2), 'index is: ', m.start(2), ',end is: ', m.end(2))
# print(m.start(1))
# print(m.start(2))
print(m.groups())
