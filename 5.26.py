# class A:
#     count = 0
#     def __init__(self):
#         A.count +=1
# A()
# A()
# A()
# print(A.count)


# print("""请选择:
#             1.登录
#             2.注册""")
# choice = int(input())
# match choice:
#     case 1:
#         account=input("请输入账号：")
#         Password=input("请输入密码：")
#         verify1=open("account.txt","r",encoding='utf-8')
#         list=verify1.readlines()
#         print(type(list))

           


#     case 2:
#         account=input("请输入账号：")
#         Password=input("请输入密码：")
#         verify=open("account.txt","a")
#         verify.write(f"{account}:{Password}\n")
#         verify.close
#         print("注册成功")

# import os
# dirs = os.listdir("./images")
# # print(type(dirs))
# print(dirs)
# for i in dirs:
#     type_path =os.path.join("./images",i)
#     if bool(os.path.isdir(type_path)):
#         for y in type_path:
#             pass

# import os
# dirs = os.listdir("D:\homework\data")
# for i in dirs:
#     type_path =os.path.join("D:\homework\data",i)
#     if os.path.isdir(type_path):
#         print(i)
 

# import os
# x = 1
# dirs = os.listdir("D:\homework\data")
# print(dirs)
# for i in dirs:
#     type_path =os.path.join(r"D:\homework\data",i)
#     if not os.path.isdir(type_path):
#         new_name = f"文档{x}.doc"
#         new_path = os.path.join(r"D:\homework\data", new_name)
#         os.rename(type_path,new_path )
#         x+=1
# print(os.listdir("D:\homework\data"))


# import os
# dir=r"D:\homework\data\data1\mnist-top24"
# trainList = []
# testList = []
# dir_name = os.listdir(dir)
# for i in dir_name:     #遍历所有文件
#     type_path =os.path.join(dir,i)
#     dir_new_name=os.listdir(type_path)
#     for x in dir_new_name: 
#         if os.path.isdir(type_path):
#             type_new_path =os.path.join(type_path,x)
#             dir_new1_name=os.listdir(type_new_path)
#             for y in dir_new1_name:
#                 type_new1_path =os.path.join(type_new_path,y)
#                 if i =="train":
#                     trainList.append(type_new1_path)
#                 else:
#                     testList.append(type_new1_path)
# print(trainList)
# print(testList)

# import os
# print("""请选择节点种类
#             1.左眼
#             2.右眼
# """)
# choice= int(input())
# match choice:
#     case 1:
#         point=input("请输入左眼坐标：")
#         eye_type = "leftEye"
#         coordinate = point
#     case 2:
#         point1=input("请输入右眼坐标：")
#         eye_type = "rightEye"
#         coordinate = point1
    
# with open('key.txt','a+',encoding='utf-8') as file:
#     file.write(f"{eye_type}{coordinate}\n")
#     file.seek(0)
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

import os
import json
with open('D:\homework\data\data2\label_train.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
for line in lines:
    parts = line.strip().split('\t') 
    # print(parts)
    name = parts[0]
    another = parts[1]
    result=json.loads(another)
    car_num = result[0]["transcription"]
    points = result[0]["points"]
    print(f"名字{name},车牌号{car_num},节点{points}")
 



import yaml

yaml.add_constructor