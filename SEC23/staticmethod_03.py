"""
#  Script Description:
    人 类型
    调用静态的方法

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

import datetime
from SEC23.utility import Utility


# Create by Jianguo on 2017/5/13
class Person:
    # count = 0
    people = []

    def __init__(self, name, birthday, gender='男', salary=0):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.salary = salary
        # Person.count += 1
        Person.people.append(self)

    @classmethod  # 类的方法，只和类有关系，和实例无关，cls = class.
    def print_all_people(cls):
        Utility.connect_db()
        print(cls.people)

    @property
    def salary(self):
        return self._salary  # 带下划线变量表示私有的。

    @salary.setter
    def salary(self, value):
        if value <= 0:
            self._salary = 0
        else:
            self._salary = value

    def get_age(self):
        return datetime.date.today().year - self.birthday.year

    @property  # 属性装饰器。
    def age(self):
        return datetime.date.today().year - self.birthday.year

    @age.setter
    def age(self, value):
        # print(f'你赋值是：{value}')
        # print("年龄是同过生日计算 ，不能赋值。")
        raise ValueError('年龄不能赋值，只能通过生日计算！')

    def say(self, word):
        print("{}说{}".format(self.name, word))

    def __str__(self):
        return f'<Person {self.name},{self.birthday},{self.gender},{self.salary}>'

    def __repr__(self):
        return f'<Person {self.name},{self.birthday},{self.gender},{self.salary}>'


p = Person('Tom', datetime.date(1990, 4, 26), '女', -9000)
p2 = Person('Jerry', datetime.date(1990, 4, 26), '女', 9000)

Person.print_all_people()
