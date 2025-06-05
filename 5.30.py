# import numpy as np
# arr_2d = np.array([[0, 1, 2],
#                    [3, 4, 5],
#                    [6, 7, 8]])

# cow=[0,1,2]
# row=[1,2,0]
# print(arr_2d[cow,row])
# print(arr_2d[0,1,2],[1,2,0])
# print(arr_2d[:,[1,2,0]])



import numpy as np

# 创建一个随机的四维数组
arr = np.random.rand(2, 3, 4, 5)
print(arr)
# 计算沿第2轴(axis=1)的平均值
mean_along_axis_1 = np.mean(arr, axis=1)
print(mean_along_axis_1.shape) 