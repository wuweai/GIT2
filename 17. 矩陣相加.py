arr = []
for i in range(2):
    size = input().split()
    for i in range(int(size[0])):
        arr.append(list(map(int, input().split())))

outside = []
for idx1 in range(len(arr)//2):
    # print(len(arr[idx1]), )
    if len(arr[idx1]) != len(arr[idx1+len(arr)//2]):
        print("兩個矩陣無法相加")
        exit()
    inside = []
    for idx2 in range(len(arr[idx1])):
        addNum = arr[idx1][idx2] + arr[idx1+len(arr)//2][idx2]
        inside.append(addNum)
    outside.append(inside)

print()
for row in outside:
    for num in row:
        print(num, end=" ")
    print()