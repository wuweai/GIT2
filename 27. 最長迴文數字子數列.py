def palindrome(nums, left, right, res, resLen):
    while left >= 0 and right < len(nums) and nums[left] == nums[right]:
        if (right - left + 1) > resLen:
            res = nums[left:right+1]
            resLen = right - left + 1
        left -= 1
        right += 1
    return res, resLen

nums = input("輸入整數列(end結束): ")
while nums != "end":
    even_res, odd_res = "0", "0"
    even_resLen, odd_resLen = 0, 0
    for num in range(len(nums)):
        left, right = num, num
        even_res, even_resLen = palindrome(nums, left, right, even_res, even_resLen)
        left, right = num, num+1
        odd_res, odd_resLen = palindrome(nums, left, right, odd_res, odd_resLen)
        
    print("最長迴文數字子數列為:%d"%max(int(even_res), int(odd_res)))
    nums = input("輸入整數列(end結束): ")