"""
#  Script Description:
    列表推到 -  推及多使用项目开发， filter()

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/26
# File name ->
scores = [85, 76, 42, 56, 98, 77, 98.2]
score_1 = list(filter(lambda x: x >= 60, scores))
print(score_1)

score_2 = [x for x in scores]
print(score_2)

score_3 = [x for x in scores if x >= 60]
print(score_3)

students = ['Tom', 'Jerry', 'Mike']

# 显示姓名含有 'e ' 的名称
e = [n for n in students if 'e' in n]

print(e)

# 过滤操作， 如果分数 <=60  ，就 + 2 打印
score_4 = [x + 2 for x in scores if x < 60]
print(score_4)
#  Set  去重复
scores = [85, 76, 42, 56, 42, 76, 98, 77, 98.2]
s = [s for s in scores]
print(s)

print("---------set-----------")
print(set(s))
s = {s for s in scores}
print(s)
# ---------set-----------
# {98, 98.2, 42, 76, 77, 85, 56}
# {98, 98.2, 42, 76, 77, 85, 56}

t = (s for s in scores)
print(type(t))
print(t)
# <class 'generator'>
# <generator object <genexpr> at 0x000002516FAEF048>
