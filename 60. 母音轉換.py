eg = input("請輸入一串小寫英文:")
vo = ["a", "e", "i", "o", "u"]
ans = ""
for char in eg:
    if char in vo: eg = eg.replace(char, ".")
print(eg)