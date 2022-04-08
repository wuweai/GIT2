a = list(input("請輸入A的好友：").split())
b = list(input("請輸入B的好友：").split())
num = 0
for friend in a:
    if friend in b:
        num += 1
print(num)