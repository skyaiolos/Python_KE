"""
#  Script Description:
        常见迭代类型

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/25
# File name ->
t = (1, 2, 3, 4, 5)
for x in t:
    print(x ** 2)

emp = {'name': "Ton", 'salary': 8000, 'Job': "dev"}
print(type(emp.keys()))
for key in emp.keys():
    print(key)

for value in emp.values():
    print(value)

print(type(emp.values()))

for k, v in emp.items():
    print(f'{k} -> {v}')
