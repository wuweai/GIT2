num = int(input("輸入筆數 n:"))
medals = []
for i in range(num):
    medals.append(input().split())
for medal in medals:
    print(f"{medal[0]}牌得到 {medal[1]} 面")