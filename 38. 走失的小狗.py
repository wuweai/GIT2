place = int(input())
distance = [int(input()) for i in range(place)]
for idx, dis in enumerate(distance):
    if dis % 9 == 0 or dis % 11 == 0:
        print(f"第{idx+1}個點 {dis}")