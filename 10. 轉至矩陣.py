n,m = map(int,input("輸入 N 及 M 為:").split())
array_list = []

# 建立串列
for i in range(n):
    nums = input(f"輸入矩陣數值第 {i+1} 列為:").split()
    array_list.append(nums)

# 方法 1 -> numpy
import numpy as np
outside = np.array(array_list).T

# 方法 2
# inside = []
# outside = []
# for row in range(len(array_list[0])):
#     for col in range(len(array_list)):
#         inside.append(array_list[col][row])
#     outside.append(inside)
#     inside = []

# output
x = 1
print()
for i in outside:
    print(f"輸出矩陣數值第 {x} 列為:",end="")
    for j in i:
        print(j,end=" ")
    print()
    x += 1