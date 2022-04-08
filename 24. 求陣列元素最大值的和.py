size = int(input("請輸入陣列大小:"))
arr = [list(map(int, input().split())) for i in range(size)]
big3 = {0:0, 1:0, 2:0}
for subArr_idx in range(len(arr)):
    for num_idx in range(len(arr[subArr_idx])):
        if arr[subArr_idx][num_idx] not in big3 and arr[subArr_idx][num_idx] > min(big3):
            big3[arr[subArr_idx][num_idx]] = (subArr_idx+1, num_idx+1)
            last = arr[subArr_idx][num_idx]
            del big3[min(big3)]

print("\n最大值為:%d\n位置為"%sum(big3), end="")
for num in big3:
    print(big3[num], end="," if num != last else "")