# nuber=["1","2","3","4"]
# d = 0;
# for a in nuber:
#     for b in nuber:
#         if a != b :
#             for c in nuber:
#                 if c != b and c!=a:
#                     print(a+b+c)
#                     d+=1
# print(d)


# for a in range(5,0,-1):
#     print("*"*a)

nums = [
    [255, 255, 255, 255],
    [255, 255, 255, 255],
    [0, 255, 0, 255]
]

for a in range(len(nums) - 1,-1, -1):  
    count1 = 0
    count2 = 0
    for b in nums[a]:
        count1 += 1;
        if b == 255:
            count2 += 1
    if count1 ==count2 :    #  当列表中=255的数量与列表长度相等时，删除该列表
        del nums[a]
       
print(nums)


# count = 0
# for a in nums:
#     for b in a:
#         if b == 255:
#             count+=1
# print(count)

# count1 = 0
# count2 = 0
# for a in nums:
#     for b in a:
#         if b != 255:
#             count1 += 1
#             break
# count2 = len(nums)-count1 
# print(count2)



# import random
# shop_list = 0
# shopList = [[], [], []]
# goodsList = ['小米', '苹果', 'vivo', '华为', 'Oppo', 'Lenovo']
# for a in goodsList :
#     shop_list = random.randint(0,2)
#     shopList[shop_list].append(a)
# for i in shopList:
#     for x in  i:
#        print(x,end="")
#     print()