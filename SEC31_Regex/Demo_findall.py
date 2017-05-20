"""
#  Script Description:
    Python 正则表达式之RegexObject

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/7
import re

text = "Tom is 8 years old, Mike is 25 years old."
# 模式对象， 表现编译后的正则表达式（编译为字节码并缓存）
# re.compile(r'模式')
print('findall()'.center(100, '*'))
pattern = re.compile(r'\d+')
print(pattern.findall(text))
print(re.findall(r'\d+', text))

s = "\\author:Tom"
pattern = re.compile(r'\\author')
rex = pattern.findall(s)
print(rex)

text = "Tom is 8 years old, Mike is 25 years old.Peter is 87 years old."
pattern = re.compile(r'\d+')
rex = pattern.findall(text)
print(rex)

p_name = re.compile(r'[A-Z]\w+')
rex_p = p_name.findall(text)
print(rex_p)

p1 = re.compile(r'\d+')
p2 = re.compile(r'[A-Z]\w+')

print('findall() VS finditer()'.center(100, '*'))

print(p1.findall(text))
print()
print('finditer()'.center(30, '*'))
it = p1.finditer(text)
for item in it:
    print(item)
