animal = {}
for i in range(int(input("輸入筆數 n:"))):
    eg, ch = input().split()
    animal[eg] = ch
check = input("輸入欲查詢單字:")
if check in animal:
    print(f"{check}中文意思為{animal[check]}")
else:
    print("字典未有此單字")