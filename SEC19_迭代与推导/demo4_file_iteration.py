"""
#  Script Description:
    常用迭代类型  - 文件

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/25
# File name ->
f = open('data.txt', 'r', encoding='utf-8')
f_contents = f.read()
print(f_contents)
f_contents = f.read()
print('--------')
print(f_contents)
print('~~~~~~~~~')
print(f.seek(0))  # 作用类似与指针再次指向文件头
f_contents = f.read()
print(f_contents)
print('~~~~~~~~~')

print('=====readline()=====')
f.seek(0)
print("-----show single line-----")
f_lines = f.readline()
print(f_lines)

print("-----show multi lines-----")
lines = f.readlines()
for line in lines:
    print(line)

print('---line in file---')
for line in open('data.txt', 'r', encoding='utf-8'):
    print(line)

