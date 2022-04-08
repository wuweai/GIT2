n = int(input("請輸入正整數n："))
add = 0
for i in range(1,n):
    if n % i == 0:
        add += i
if add == n:
    print("perfect")
else:
    if add > n:
        print("abundant")
    else:
        print("deficient")