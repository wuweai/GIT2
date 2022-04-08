num = int(input("輸入一正整數:"))
res = "YES" if num % 2 == 0 and num % 11 == 0 and num % 5 != 0 and num % 7 != 0 else "NO"
print(f"{num}為新公倍數?:{res}")