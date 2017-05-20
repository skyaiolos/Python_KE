"""
#  Script Description:
    类间关系 - 聚合
        |-------------------------------|
        |                               |
|=======<>==========|            |======V============|          |===================|               
|    Department     |            |     Developer     |          |    Project        |
|-------------------|            |-------------------|          |-------------------|
| + name            |            | + name            |          | +name             |
| + manager         |<-----------| + skills          |          | +team             |
| +tel              |            |                   |    /---->| +start_date       |
| +employees        |            |                   |          |                   |
|-------------------|            |-------------------|   /      |-------------------|
| +develop_project()|            | +develop_project()|--/       |                   | 
|===================|            |===================|          |===================|


"""
from datetime import *

__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/13

class Department:
    def __init__(self, name, manager, tel):
        self.name = name
        self.manager = manager
        self.tel = tel
        self.employees = []

    def __repr__(self):
        return f"<Department :{self.name} >"


class Project:
    def __init__(self, name, team, start_date):
        self.name = name
        self.team = team
        self.start_date = start_date

    def __repr__(self):
        return f'<Project :{self.name}>'


class Developer:
    def __init__(self, department, name, skills):
        self.department = department
        self.name = name
        self.skills = skills
        self.department.employees.append(self)

    def __repr__(self):
        return f'<Developer : {self.name},技术：{self.skills}>'

    def develop_project(self, department, project, start_date):
        print(f'{self.name}所在{department.name}的项目组{project.team}正在开发{project},'
              f'项目开始时间{project.start_date}')


if __name__ == '__main__':
    dpt = Department("技术部", 'Mike', '010-88888888')
    d = Developer(department=dpt, name='Tom', skills=['Python', 'SQL', 'C#'])
    d2 = Developer(dpt, 'Jerry', ["Django", "MongoDB"])

    print(dpt.employees)
