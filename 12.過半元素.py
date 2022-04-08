from numpy import half


num_list = input().split()
half = "NO"
for num in num_list:
    if num_list.count(num) > len(num_list)/2:
        half = num
        break
print(f"過半元素為:{half}")