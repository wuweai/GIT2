use_kwh = int(input())
summer, non_summer = 0,0
cost = {120: [[2.1, 2.1], 0],
        330: [[3.02, 2.68], 120],
        500: [[4.39, 3.61], 330],
        700: [[4.97, 4.01], 500]}
for kwh in cost:
    if use_kwh <= kwh:
        summer += (use_kwh-cost[kwh][1])*cost[kwh][0][0]
        non_summer += (use_kwh-cost[kwh][1])*cost[kwh][0][1]
        break
    else:
        summer += (kwh-cost[kwh][1])*cost[kwh][0][0]
        non_summer += (kwh-cost[kwh][1])*cost[kwh][0][1]
print(f"Summer months:{summer}")
print(f"Non-Summer months:{non_summer}")