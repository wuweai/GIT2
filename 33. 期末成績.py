suject_list = ["國文", "英文", "微積分", "體育", "程式設計"]
total_score, maxScore, minScore = 0, 0, 100
for suject in suject_list:
    score = int(input(suject+":"))
    total_score += score
    if score > maxScore:
        maxScore = score
        maxSuject = suject
    if score < minScore:
        minScore = score
        minSuject = suject
print("\n平均分數：%.2f"%(total_score/len(suject_list)))
print(f"最高分科目：{maxSuject}{maxScore}分")
print(f"最低分科目：{minSuject}{minScore}分")