info = {}
for i in range(int(input("輸入 n 值:"))):
    name = input("請輸入姓名:")
    email = input("請輸入電子郵件:")
    info[name] = email
search = input("請輸入要查詢電子郵件的姓名:")
print(f"{search} 電子郵件帳號為 {info[search]}")