num_list = [int(input(f"請輸入第 {i+1} 個數字：")) for i in range(10)]
num_list.sort()
for i in range(len(num_list)): num_list[i] = str(num_list[i])
print("最大的 3 個數字為：" + ",".join(num_list[7:]))
print("最小的 3 個數字為：" + ",".join(num_list[:3]))