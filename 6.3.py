# import numpy as np

# arr=np.ones(shape=(5,5))
# print(arr)
# arr[1:4][1:4] = 0
# print(arr)



# import numpy as np
# # """
# # 现在给定两个矩形区域的坐标 分别使用box 和 boxes表示
# # 元素对应表示为[x1, y1, x2, y2], x1,y1表示矩形左上角的点 x2, y2表示矩形右下角的点
# # box = np.array([2, 2, 20, 15])
# # boxes = np.array([15, 12, 25, 21])
# # """


# box = np.array([2, 2, 20, 15])
# boxes = np.array([15, 12, 25, 21])


# def area(array):
#     x1 = array[0]
#     x2 = array[2]
#     y1 = array[1]
#     y2 = array[3]
#     wide = x2-x1
#     high = y2-y1
#     return wide*high

# def uarea(array1,array2):
#     if array1[2]<array2[0]  or array1[0]>array2[2]:
#         return "没有交集"
#     else:
#         x = sorted([array1[0],array1[2],array2[0],array2[2]])
#         y = sorted([array1[1],array1[3],array2[1],array2[3]])
#         new_array=[x[1],y[1],x[2],y[2]]
#         return new_array


# if __name__ =="__main__":
#     a = area(box)
#     print(f"面积是:{a}")
#     b = area(boxes)
#     print(f"面积是:{b}")
#     u = uarea(box,boxes)
#     print("交集面积是：",area(u))




# import numpy as np
# a = input("请输入A点坐标:")
# a = np.array([int(x) for x in a.split(',')], dtype=np.int32)
# b = input("请输入B点坐标:")
# b = np.array([int(x) for x in b.split(',')], dtype=np.int32)
# c = input("请输入C点坐标:")
# c = np.array([int(x) for x in c.split(',')], dtype=np.int32)
# ba = a-b
# bc = c-b

# ba_modulus = np.sqrt((ba*ba).sum())
# bc_modulus = np.sqrt((bc*bc).sum())

# dot = np.dot(ba,bc)
# cos = dot/(ba_modulus*bc_modulus)
# print(cos)



# import numpy as np
# target_vector = np.array([1, 2])
# names = ['sy', 'qq', 'lm', 'mgt']
# vector_sy = np.array([4, 6])
# vector_qq = np.array([1, 2])
# vector_lm = np.array([10, 11])
# vector_mgt = np.array([1, 3])

# a = []
# name1 = []
# for x in names:
#     name = globals()[f'vector_{x}']
#     diff = name - target_vector             # 计算差值向量
#     a.append(np.linalg.norm(diff,ord=2))
#     name1.append(x)
# nearest = sorted(zip(name1, a), key=lambda item: item[1])[:2]
# print(nearest)



# import numpy as np
# import ast


# path = r"D:\homework\data\data5\feat.txt"
# target_path = r"D:\homework\data\data5\target_feat.txt"

# def dic(path):
#     dict = {}
#     with open(path,"r",encoding="UTF-8") as f1:
#         lines = [line.strip() for line in f1.readlines()]
#         for i in lines:
#             parts = i.split('|')
#             key = parts[1]
#             value = parts[2].strip()
#             vector = np.array(ast.literal_eval(value), dtype=np.float32)
#             dict[key]=vector
#     return dict

# with open(target_path,"r",encoding="UTF-8") as f2:
#     line = f2.readline().strip()
#     target_vector = np.array(ast.literal_eval(line), dtype=np.float32)
#     new_dict = dic(path)
#     diff_dict=[]
#     for k,v in new_dict.items():
#         diff = np.linalg.norm(v - target_vector) 
#         diff_dict.append((k, diff))
#     new_dict=sorted(diff_dict, key=lambda item: item[1])[:3]
#     print("最接近的三个：")
#     for key, diff in new_dict:
#         print(f"Key: {key}, 差值: {diff}")
    
import numpy as np

a = np.array([
[1, 4, 2, 5],
[5, 6, 7, 8],
[9, 10, 12, 13]
])


c = np.array([
[8, 7, 255, 6],
[5, 255, 255, 255],
[3, 5, 255, 255]
])
     
arr = np.where(c==255,c,a)
print(arr)