"""
#  Script Description:
        类 ， 继承与多态

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/13
class Employee:
    def __init__(self, name, department, title, salary):
        self.name = name
        self.department = department
        self.title = title
        self.salary = salary

    def __repr__(self):
        return f'<员工 ：{self.name}>'

    def working(self):
        print(f'员工{self.name}在工作...')


class Developer(Employee):
    def __init__(self, name, department, title, salary, skills):
        # super.__init__(self,name,department,title,salary)
        Employee.__init__(self, name, department, title, salary)
        self.skills = skills

    def working(self):
        super().working()
        print(f'开发人员在码代码...')


class Accountant(Employee):
    def __init__(self, name, department, title, salary, certification):
        # super.__init__()
        Employee.__init__(self, name, department, title, salary)
        self.certification = certification

    def working(self):
        super().working()
        print(f'会计在做财务报表')


if __name__ == '__main__':
    d = Developer('Tom', '技术部', 'DET', 13000, ['Python', 'Flask'])

    d.working()
    a = Accountant('Marry', '财务部', '会计员', 9800, '会计从业资格证')
    a.working()
