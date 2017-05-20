"""
#  Script Description:
    类间关系 - 依赖。

|===================|          |===================|               
|     Developer     |          |    Project        |
|-------------------|          |-------------------|
| + name            |          | +name             |
| + skills          |          | +team             |
|-------------------|   /------| +start_date       |
| +develop_project()|--/       |-------------------| 
|===================|       


"""
from datetime import *

__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/13

class Project:
    def __init__(self, name, team, start_date):
        self.name = name
        self.team = team
        self.start_date = start_date

    def __repr__(self):
        return f'<Project :{self.name}>'


class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __repr__(self):
        return f'<Developer : {self.name},技术：{self.skills}>'

    def develop_project(self, project, start_date):
        print(f'{self.name}所在的项目组->"{project.team}"正在开发{project},'
              f'项目开始时间:{project.start_date}')


if __name__ == '__main__':
    d = Developer('Tom', ('Python', 'SQL', 'C#'))
    print(d)

    proj = Project('OA', 'DEV02', date(2017, 5, 13))
    print(proj)

    d.develop_project(project=proj, start_date=proj.start_date)
