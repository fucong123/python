# def sum (a,b,c):
#     sum = a+b+c
#     print("三个数之和是：",sum)
#     return sum

# num1 = int(input ("请输入数字1:"))
# num2 = int(input ("请输入数字2:"))
# num3 = int(input ("请输入数字3:"))
# sum(num1,num2,num3)


# def max (a,b,c):
#     list = [a,b,c]
#     max = 0
#     for i in list:
#         if max < i:
#             max=i
#     print("最大值是：",max)
#     return max

# num1 = int(input ("请输入数字1:"))
# num2 = int(input ("请输入数字2:"))
# num3 = int(input ("请输入数字3:"))
# max(num1,num2,num3)


# def min (a,b,c):
#     list = [a,b,c]
#     min = a
#     for i in list:
#         if min > i:
#             min=i
#     print("最小值是：",min)
#     return min

# num1 = int(input ("请输入数字1:"))
# num2 = int(input ("请输入数字2:"))
# num3 = int(input ("请输入数字3:"))
# min(num1,num2,num3)


# def locatnum(list,num):
#     addr = []  #创建空列表，存储地址
#     for idx,i in enumerate(list):
#         if i==num:
#             addr.append(idx)
#     print("地址是：",addr)

# nums = [10, 20, 30, 50, 20]
# num = int(input("请输入查找的数字："))
# locatnum(nums,num)
    


# def mul99(num1):
#     for a in range(1,num1+1) :
#         for b in range(1,a+1) :
#             print(f"{a}*{b}=",a*b,sep="",end=" ")
#         print()

# num = int(input("请输入数字：")) 
# mul99(num)    


# def factorial(num):
#     mul = 1
#     for i in range(1,num+1) :
#         mul *=i
#     return mul

# num = int(input("请输入数字：")) 
# print(factorial(num))





# def factorial(num):
#     mul = 1
#     for i in range(1,num+1) :
#         mul *=i
#     return mul


# def sum(num):
#     sum = 0
#     for i in  range(1,num+1) :
#         sum += factorial(i)
#     return sum


# num = int(input("请输入数字：")) 
# print(sum(num))




# cards = [
#   {'name':'张三','tel':'13812345678','job':'CEO','addr':'四川'}  # 字典
# ]
# 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面  cards.append(一个人的名片字典)

def addperson(cards):
    cards.append({'name':input("请输入姓名"),'tel':input("请输入电话"),'job':input("请输入工作"),'addr':input("请输入住址")})

# 显示所有名片: 遍历名片盒子输出名片信息
def query(cards):  
    for a in cards :
        print(a)
        
#  3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
#    如果找到 , 重写录入新的名片信息, 完成修改操作
def change(cards):
    result = False
    name = input("请输入修改的姓名：")
    for a in cards :
      if a['name']== name:
             result = True
             a['name'] = name
             a['tel'] = input("请输入电话")
             a['job'] =input("请输入工作")
             a['addr']= input("请输入住址")
    if result == False:
        print("未查询到该姓名")
        
# 4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.

def delete(cards):
    name = input("请输入删除的姓名：")
    result = False
    for idx,a in enumerate(cards):
        if a['name']== name :
         result = True
         cards.pop(idx)
    if result == False:
        print("未查询到该姓名")


cards = [
  {'name':'张三','tel':'13812345678','job':'CEO','addr':'四川'}  # 字典
]
result = 1
while(result):
    print("*****名片管理系统*****")   
    print(""" 
          1.增加名片
          2.修改名片
          3.删除名片
          4.显示所有名片
          5.退出系统
    """)
    A=int(input("请选择："))
    match A:
        case 1:
                addperson(cards)
        case 2:
                change(cards)
        case 3:
                delete(cards)
        case 4:
                query(cards)
        case 5:
                result = 0
        case _:
            print ("选择错误")
    print("")
