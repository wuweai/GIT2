test, student = map(int, input("請輸入考試次數及學生數:").split())
percen = list(map(float, input("每次考試所佔的比率:").split()))
total = 0
for i in range(student):
    scores = list(map(int, input().split()))
    for score_idx in range(len(scores)):
        total += scores[score_idx]*percen[score_idx]
print("全班的總平均值為:%.2f"%(total/student))