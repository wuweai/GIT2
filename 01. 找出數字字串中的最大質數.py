def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

nums = input("請輸入正整數：")
biggest = 0
for num1 in range(len(nums)):
    for num2 in range(num1,len(nums)):
        is_prime = prime(int(nums[num1:num2+1]))
        if is_prime and int(nums[num1:num2+1]) > biggest: biggest = int(nums[num1:num2+1])
if biggest: print(f"子字串中最大的質數為：{biggest}")
else: print("No prime found")