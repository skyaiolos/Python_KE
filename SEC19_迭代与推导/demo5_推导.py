"""
#  Script Description:
        推导  ， map()

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/25
# File name ->

scores = (87, 88, 55, 88, 99, 88.22)
results = []
for x in scores:
    results.append(x)
print(results)

print('---推导，x for x in iteration---')
results = [x for x in scores]
print(results)

print("-----map()--------")
results = map(lambda x: x + 2, scores)
print(results)
print(list(results))

print('---推导，x + 2 for x in iteration---')

results = [x + 2 for x in scores]
print(results)

students = ['Tom', 'Jerry', 'Mike']

s_upper = [n.upper() for n in students]  # n.upper()  期望的结果，For前面是算法程式
print(s_upper)
