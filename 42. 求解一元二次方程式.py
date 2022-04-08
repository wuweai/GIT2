a = int(input())
b = int(input())
c = int(input())

# 方法一 -> numpy
# import numpy
# ans = numpy.roots([a,b,c])
# print(int(ans[1]))
# print(int(ans[0]))

# 方法二
res = b**2 - 4*a*c
if res > 0:
    print(int((-b + pow(b**2 - 4*a*c,0.5))/(2*a)))
    print(int((-b - pow(b**2 - 4*a*c,0.5))/(2*a)))
elif res == 0:
    print(int(-b / (2*a)))
else:
    print("無解")
