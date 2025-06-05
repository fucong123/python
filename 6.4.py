import numpy as  np
import matplotlib.pyplot as plt

students = [
{'name': '张三', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese':80, 'math': 90, 'english': 85},
{'name': '李四', 'gender': 'male', 'age': 16, 'class': 'class2', 'chinese':70, 'math': 85, 'english': 80},
{'name': '王五', 'gender': 'female', 'age': 15, 'class': 'class3', 'chinese':90, 'math': 95, 'english': 90},
{'name': '赵六', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese':75, 'math': 80, 'english': 85},
{'name': '钱七', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese':85, 'math': 90, 'english': 80},
{'name': '孙八', 'gender': 'male', 'age': 19, 'class': 'class2', 'chinese':90, 'math': 95, 'english': 95},
{'name': '周九', 'gender': 'female', 'age': 18, 'class': 'class3', 'chinese':80, 'math': 85, 'english': 80},
{'name': '吴十', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese':70, 'math': 75, 'english': 70},
]


# 1、用饼图统计信息工程学院女生和男生的人数；
def   pie(students):
    male =0
    female = 0
    gender = ["male","female"]
    for info in students:
        if info["gender"] =="male":
            male+=1
        else:
            female+=1
    nums=[male,female]
    plt.pie(x=nums, labels=gender)
    plt.show()


# 2、用柱图分析语文成绩优、良、中、差的人数；
def  bar(students):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    level = ["优","良","中","差"]
    good = 0
    nice = 0
    mid = 0
    bad = 0
    for info in students:
        if info["chinese"] >90:
            good+=1
        elif info["chinese"] >80  :
            nice+=1
        elif info["chinese"] >60:
            mid+=1
        else:
            bad+=1
    nums=[good,nice,mid,bad]
    x=range(len(level))
    plt.bar(x,nums,width=0.5)
    plt.xticks(x, level)
    plt.show()

# 3、利用散点图分析语文和英语成绩的相关性；
def scatter(studets):
    chinese = []
    english = []   
    for info in students:
        chinese.append(info["chinese"])
        english.append(info["english"])
    plt.scatter(chinese, english)
    plt.show()


# 4、利用折线图分析学生年龄和数学平均成绩的走势图
def  plot(students):
    age=[]
    math = []
    for info in students:
        age.append(info["age"])
        math.append(info["math"])
    plt.plot(age, math)
    plt.show()


def  m1():
    x=[3,5,1,2,9,6]
    y=[1,2,3,4,5,6]
    plt.plot(x, y)
    plt.show()
if __name__ == "__main__":
    m1()

