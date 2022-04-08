amount = int(input("測試的資料量:"))
possible_blood = {"O O":["O"],"O A":["A","O"],"O B":["B","O"],"O AB":["A","B"],
                  "A A":["A","O"],"A B":["A","B","O","AB"],"A AB":["A","B","AB"],
                  "B B":["B","O"],"B AB":["A","B","AB"],"AB AB":["A","B","AB"]}
for i in range(amount):
    blood = input()
    if blood[:3] in possible_blood:
        print("YES") if blood[-1] in possible_blood[blood[:3]] else print("IMPOSSIBLE")