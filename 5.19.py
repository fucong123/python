

# name = " posekakaka "
# #a. 移除name 变量对应的值两边的空格，并输出移除后的内容
# print(name.strip())
# #b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
# print(name.startswith("po"))
# # c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
# print(name.endswith("a"))
# # d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
# print(name.replace("k","c"))
# # e. 将name 变量对应的值根据 “k” 分割，并输出结果。
# print(name.split("k"))
# # f. 请问，上一题 e 分割之后得到值是什么类型（可选）
# print(type(name))




students = [
	{'name':'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel':'15300022839'},
	{'name':'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel':'15300022838'},
	{'name':'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel':'15300022837'},
	{'name':'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel':'15300022428'},
	{'name':'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel':'15300022653'},
	{'name':'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel':'15300022867'} 

]
# # 3.1 遍历所有的姓名
# for a in students :
#     print (a["name"])

# # 3.1 统计不及格学生的个数
# count = 0
# for a in students :
#     if  a["score"] < 60 :
#         count+=1
# print (count)

# # 3.2 打印所有男生的信息
# for a in students :
#     if  a["sex"] == "男" :
#         print(a)
        

# # 3.3 求平均分数
# score = 0
# for a in students :
#     score += a['score']
# print(score/len(students))


# cards = [
#   {'name':'张三','tel':'13812345678','job':'CEO','addr':'四川'}  # 字典
# ]
# # 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面  cards.append(一个人的名片字典)

# cards.append({'name':input("请输入姓名"),'tel':input("请输入电话"),'job':input("请输入工作"),'addr':input("请输入住址")})

# # 显示所有名片: 遍历名片盒子输出名片信息

# for a in cards :
#         print(a)
        
# #  3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
# #    如果找到 , 重写录入新的名片信息, 完成修改操作
# name = input("请输入修改的姓名：")
# for a in cards :
#       if a['name']== name:
#              a['name'] = name
#              a['tel'] = input("请输入电话")
#              a['job'] =input("请输入工作")
#              a['addr']= input("请输入住址")
# for a in cards :
#         print(a)
        
# # 4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
# name = input("请输入删除的姓名：")
# for idx,a in enumerate(cards):
#     if a['name']== name :
#          cards.pop(idx)
# for a in cards :
#         print(a)



# letters = 'abcdabcdabcdabcefg' 
# char_count = {}   #创造一个空字典，统计次数
# for char in letters:  #遍历字符串
#         if char in char_count:   #判断是否在字典内
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
# print(char_count)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = int(input("请输入目标值："))
# for a in nums :
#     for b in nums :
#         if a +b ==target:
#         	print(a,b)


grade_01 = [{"happy": 10}, {"dispirited": 2}]
grade_02 = [{"happy": 11, "exciting": 12}, {"dispirited": 5}]
school = [grade_01, grade_02]


total = {}
for grade in school :
	for item in grade :
		for emotion, count in item.items():
			if emotion in total:
				total[emotion] += count
			else:
				total[emotion] = count
print(total)