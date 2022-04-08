amount = int(input("組數為:"))
total = []
for i in range(amount):
    full, half = map(int, input(f"第 {i+1} 組:").split())
    total.append(full*250+half*175)
print()
for group in range(amount):
    print(f"第 {group+1} 組應收費用:{total[group]}")