def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return "N"
    return "Y"

num1 = int(input("請輸入第一個要判斷的數字："))
num2 = int(input("請輸入第二個要判斷的數字："))
if num2 != num1+2:
    print("N")
else:
    print(prime(num1) and prime(num2))