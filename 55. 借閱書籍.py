shelfs = {"書架 A ":["飢餓遊戲 3","解憂雜貨店","怪獸與牠們的產地","哈利波特 6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"],
        "書架 B ":["房思琪的初戀樂園","等一個人咖啡","鬼滅之刃 14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]}
book = input("請輸入欲租借的書籍：")
for shelf in shelfs:
    if book in shelfs[shelf]:
        print(f"在{shelf}的第 {shelfs[shelf].index(book)+1} 本")
        exit()
print("查無此書籍")