km = eval(input("請輸入路程公里數(km)："))
money = 75
re = 0
if km > 1.5:
    amount_250, re = divmod((km-1.5)*1000, 250)
    money += amount_250*5
if re:
    money += 5
print(f"所需車資為：{int(money)}")