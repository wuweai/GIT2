ans = input("請輸入第一組數字：")
num = input("請輸入第二組數字：")
a, b = 0, 0
for i in ans:
    if i in num:
        if ans.index(i) == num.index(i):
            a += 1
        else:
            b += 1

print(f"{a}A{b}B",end=" 全對" if a == len(ans) else " 加油")