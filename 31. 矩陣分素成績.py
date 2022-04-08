col, row = input("輸入矩陣的維度:").split()
arr1, arr2 = [],[]
for i in range(int(col)):
    nums = list(map(int,input().split()))
    arr1.append(nums)
for i in range(int(col)):
    nums = list(map(int,input().split()))
    arr2.append(nums)
print()

# 方法一 -> numpy
# import numpy as np
# arr1 = np.array(arr1)
# arr2 = np.array(arr2)
# fin_arr = arr1*arr2
# for sub_arr in fin_arr:
#     for num in sub_arr:
#         print(num, end=" ")
#     print()

# 方法二
for idx1 in range(len(arr1)):
    for idx2 in range(len(arr1[idx1])):
        print(arr1[idx1][idx2] * arr2[idx1][idx2], end=" ")
    print()