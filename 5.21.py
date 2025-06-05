# 对 nums=[11,33,22,66,44,88,99] 升序排， 要求使用选择排序来实现
def choice(num):
    for i in range(0,len(num)):
        min = i
        for x in range(i+1,len(num)):
            if num[min]> num[x]:
                min = x
        num[i],num[min]=num[min],num[i] 
    return num
nums=[11,33,22,66,5,44,88,99]
print(choice(nums)) 


# # 1、对 nums=[11,33,22,66,44,88,99] 降序排， 要求使用冒泡排序来实现
# def sort(num):
#     for i in range(0,len(num)):
#         for x in range(0,len(num)-i-1):
#             if num[x]<num[x+1]:
#                 num[x],num[x+1]=num[x+1],num[x] 
        
#     return num
# nums=[11,33,22,66,44,88,99]
# print(sort(nums)) 

# def sort(nums):
#     for j in range(len(nums) - 1):
#         for i in range(0, len(nums) - 1 - j):
#             if nums[i] < nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#     return nums
# nums=[11,33,22,66,44,88,99]
# print(sort(nums)) 

# 3、求前 K 个高频元素设计对应的函数
# nums7 = [2, 3, 1, 2, 3, 3, 3, 4, 4, 4]
# 前 K=2 个高频元素: [3, 4]


# def  find(nums,num):
#     total={}
#     list=[]
#     for i in nums :
#         if i in total:
#             total[i]+=1
#         else :
#             total[i] = 1
#     print(total)
#     for x in range(1,num+1):
#         freequece = 0
#         keys = 0
#         for  key,v in total.items():
#             if total[key]>freequece:
#                 freequece=total[key]
#                 keys =key
#         total.pop(keys)
#         list.append(keys)
#     return list
# nums7 = [2, 3, 1, 2, 3, 3, 3, 4, 4, 4]
# print(find(nums7,2))