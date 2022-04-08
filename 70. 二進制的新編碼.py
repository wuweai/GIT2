def ten2two(two):
    ten = 0
    for idx in range(1, len(two)):
        if "0" not in two[:idx]:
            ten += 1
    ten *= 2
    if two[-1] == "1":
        ten += 1
    return str(ten)

num1, num2 = input().split()
new_num = int(ten2two(num1)+ten2two(num2))
if new_num + 67 == 91:
    print("A")
elif new_num + 67 == 92:
    print("B")
elif new_num + 67 == 93:
    print("C")
else:
    print(chr(new_num + 67))