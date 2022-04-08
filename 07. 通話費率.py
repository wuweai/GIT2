input_plan, time = map(int,input("輸入月租費型式及通話時間為:").split(","))
plans = {186: 0.09, 386: 0.08, 586: 0.07, 986: 0.06}
for plan in plans:
    if input_plan == plan:
        total = time * plans[plan]
        total *= plans[plan]*10-0.1 if time * plans[plan] > input_plan else plans[plan]*10
print("通話費為：%.0f"%total)