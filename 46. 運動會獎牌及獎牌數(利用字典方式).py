num = int(input("輸入比數 n:"))
medal = {}
for i in range(num):
    name, value = input().split()
    medal[name] = value
for name in medal:
    print(f"{name}牌得到 {medal[name]} 面")