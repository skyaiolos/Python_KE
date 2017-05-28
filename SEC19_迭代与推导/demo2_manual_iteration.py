"""
#  Script Description:
       手动迭代器
        

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/25
# File name ->
print("---Demo1---")
scores = [85, 76, 43, 23, 55, 99.11]
I = iter(scores)
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(next(I))
# print(next(I))
while True:
    try:
        s = next(I)
    except StopIteration:
        break
    print(s)

print("---Demo2---")
students = ['Tom', 'Jerry', 'Mike']
I = iter(students)
s = next(I)
print(s.upper())
s = I.__next__()

print(s.upper())

s = I.__next__()
print(s)
print(next(I))
