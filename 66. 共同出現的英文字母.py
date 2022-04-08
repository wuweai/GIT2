a = set(list(input("請輸入string_a：")))
b = set(list(input("請輸入string_b：")))
ans_list = []
for char in a:
    if char in b:
        ans_list.append(char)
ans_list.sort()
if ans_list:
    for ans in ans_list:
        print(ans, end="")
else:
    print("N")