# class Girlfriend:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
# girlfriend = Girlfriend(name="小红")
# print(girlfriend.name)

# class Phone:
#     def __init__(self,color,size,price,brand):
#         self.color=color
#         self.size = size
#         self.price = price
#         self.brand = brand

# phone = Phone("蓝色",6.3,9999,"小米")
# print(f"手机品牌是{phone.brand},售价{phone.price},{phone.size}大小,{phone.color}")


# class Student:
#     def __init__(self,name,age,tel,score,sex):
#         self.name=name
#         self.age = age
#         self.tel= tel
#         self.bscore = score
#         self.sex = sex
#     def __str__(self):
#         return f"{self.name},{self.age},{self.tel},{self.bscore},{self.sex}"
# stu=Student("小明",18,1888888,99,"男")
# print(stu)


# class Animal:
#     def makeSound(self):
#         print("hello,world")
#     def __init__(self,name):
#         self.name=name


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#     def makeSound(self):
#         print("hello,dog")
#     pass



# class Cat(Animal):
#     def makeSound(self):
#         print("hello,cat")

# Animal=Dog("旺旺")
# Animal.makeSound

# class Friend:
#     def __init__(self, name):
#         self.name = name
#         pass
#     def study(self):
#         print('一起学习')
#         pass
#     def film(self):
#         print('一起看电影')
#         pass

# class HoneyFriend(Friend):
#     def __init__(self, name):
#         super(HoneyFriend, self).__init__(name)
#         pass


# class Student:
#     def __init__(self,name,age,score,sex,tel):
#         self.name=name
#         self.age = age
#         self.tel= tel
#         self.score = score
#         self.sex = sex
#     def getStudent(self):
#         print( f"姓名是{self.name},年龄是{self.age},电话是{self.tel},分数是{self.score},性别是{self.sex}")
#     def getScore(self):
#         print(f"{self.name}的成绩是{self.score}")

# students = [
#     {'name': 'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel': '15300022839'},
#     {'name': 'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel': '15300022838'},
#     {'name': 'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel': '15300022837'},
#     {'name': 'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel': '15300022428'},
#     {'name': 'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel': '15300022653'},
#     {'name': 'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel': '15300022867'}]
# for i in students:
#     index = students.index(i) + 1
#     obj_name = f"stu{index}"
    
#     stu_list = list(i.values())
#     globals()[obj_name ]=Student(*stu_list)


# for i in range(1,len(students)+1):
#     stu = globals()[f"stu{i}"]
#     stu.getStudent()

# print()
# print()
# print()
# num = 0
# for i in range(1,len(students)+1):
#     stu = globals()[f"stu{i}"]
#     if stu.score <60:
#         num+=1
#         print("不及格学生是",stu.name)
#         stu.getScore()
#         print()
# print(f"不及格学生数量是{num}")



# 3.你和你的女朋友今天准备出去玩：
# 你的男朋友说要出去看电影，女朋友说要学习。
# 怎么办? 剪刀石头布游戏 3局两胜。请最后显示 获胜的是哪一方?
import random
class Boyfriend:
    def game(self):
        # choices = ['石头', '剪刀', '布']
        return  random.randint(1,100)  #石头剪刀布判断太麻烦了
    def film(self):
        print("看电影")
class Girlfriend:
    def game(self):
        # choices = ['石头', '剪刀', '布']
        return  random.randint(1,100)
    def study(self):
        print("学习")

class Game(Boyfriend,Girlfriend):
        
        def game(self):
            times = int(input("请输入游戏次数"))
            b = 0
            g = 0
            for i in range(1,times+1):
                bf=Boyfriend().game()
                gf=Girlfriend().game()
                if bf>gf:
                   b+=1
                elif bf<gf:
                    g+=1
            if b>g:
                super().film()
            elif b<g:
                super().study()
            else:
                print("平局，重玩")

Boyfriend()
Girlfriend()
game = Game()
game.game()
