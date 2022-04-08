def arithmetic(num_list):
    for i in range(1, len(num_list)):
        if int(num_list[i]) - int(num_list[i-1]) != int(num_list[1]) - int(num_list[0]):
            return False
    return True

def geometric(num_list):
    for i in range(1, len(num_list)):
        if int(num_list[i]) / int(num_list[i-1]) != int(num_list[1]) / int(num_list[0]):
            return False
    return True

fre = int(input())
for i in range(fre):
    num_list = []
    for j in range(4):
        num_list.append(input())
    # 判斷等差
    if arithmetic(num_list):
        print(" ".join(num_list) + " %d"%(int(num_list[-1])+(int(num_list[1])-int(num_list[0]))) + "\n此為等差數列")
    # 判斷等比
    if geometric(num_list):
        print(" ".join(num_list) + " %d"%(int(num_list[-1])*(int(num_list[1])//int(num_list[0]))) + "\n此為等比數列")