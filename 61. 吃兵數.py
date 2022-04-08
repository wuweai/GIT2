minute, second = map(int,input("請輸入遊戲時間：").split(":"))
time = minute*60 + second - 75
wave = 1
soldier = 0
while time > 0:
    soldier += 7 if wave % 3 == 0 else 6
    if wave % 2 == 0: soldier -= 1
    wave += 1
    time -= 30
print(f"{soldier} 隻兵")