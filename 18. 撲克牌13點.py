cards = input().split()
eg = {"A":1,"J":11,"Q":12,"K":13}
ans = 0
for card in cards: ans += eg[card] if card in eg else int(card)
print(ans)