num_list = input("輸入值為:").split(",")
smallest = int("".join(sorted(num_list)))
biggest = int("".join(sorted(num_list,reverse=True)))
print("最大值數列與最小值數列差值為：" + str(biggest - smallest))