"""
#  Script Description:
    Python 正则表达式之RegexObject

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/7
import re

print('match()'.center(100, '*'))
text = '<html><head></head><body></body></html>'
pattern = re.compile(r'<html>')
rex = pattern.match(text)
print(rex, '\n', rex.group(0))

text2 = ' <html><head></head><body></body></html>'
rex_space = pattern.match(text2)
print('Sine the first word is the space : ', rex_space)

rex_space_2 = pattern.match(text2, 1)
print(rex_space_2)
print(rex_space_2.group(0))
print()
print('search()'.center(100, '*'))
rex_search = pattern.search(text2)
print(rex_search)
print(rex_search.group(0))

print()
print('match() VS search()'.center(100, '*'))

text = "Tom is 8 years old, Mike is 25 years old.Peter is 87 years old."
p1 = re.compile(r'\d+')
p2 = re.compile(r'[A-Z]\w+')
print(p1.match(text))
print(p2.search(text), p2.search(text).group(0))
