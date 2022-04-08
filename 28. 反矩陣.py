import numpy as np
a = list(map(int,input().split()))
a[1] = -(a[1])
b = list(map(int,input().split()))
b[0] = -(b[0])
arr = np.array([a, b])
det = arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0]
fin_arr = (1/det)*arr.T
for sub_arr in fin_arr:
    for num in sub_arr:
        print("%.1f"%num, end=" ")
    print()