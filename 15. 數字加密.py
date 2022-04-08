num = input("輸入一組四位數字為:")
ans = [(int(i)+7)%10 for i in num]
print(str(ans[2])+str(ans[3])+str(ans[0])+str(ans[1]))