def append_list(cards):  # 將花色與數字個別加入 list
    flower, num = [], []
    for card in cards:
        flower.append(card[0])
        num.append(card[1:])
    return flower, num

def sequence(nums, cou):  # 判斷是否為順子
    for num in nums[:-1]:
        if int(nums[nums.index(num)+1]) - int(num) != 1:
            return remain_card_type(cou)
    return 5

def card_type(flowers, nums, cou):
    f_flower = flowers[0]  # 先判斷是否為同花順
    for flower in flowers[1:]:
        if flower != f_flower:
            return sequence(nums, cou)
    return sequence(nums) + 3
        
def remain_card_type(cou):  # 剩餘牌型
    if cou.count(4) == 4 and cou.count(1) == 1:
        return 7
    elif cou.count(2) == 2 and cou.count(3) == 3:
        return 6
    elif cou.count(3) == 3 and cou.count(1) == 2:
        return 4
    elif cou.count(2) == 4 and cou.count(1) == 1:
        return 3
    elif cou.count(2) == 2 and cou.count(1) == 3:
        return 2
    elif cou.count(1) == 5:
        return 1

conti = 0
while conti != -1:
    two_card = []
    for i in range(2):
        card = input().split()
        flowers, nums = append_list(card)
        cou = [nums.count(num) for num in nums]   # get count
        cardType = card_type(flowers, nums, cou)  # judge card
        two_card.append(cardType)
        
    print(1) if two_card[0] > two_card[1] else print(0)
    conti = int(input())