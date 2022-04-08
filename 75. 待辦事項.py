matter = ""
ans = []
while matter != "end":
    matter = input("請輸入事項(若已無事項，請輸入 end)：")
    ans.append(matter)

for i in ans[:-1]:
    print(f"{ans.index(i)+1}. {i}")