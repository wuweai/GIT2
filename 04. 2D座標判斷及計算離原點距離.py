def y_coor(y, top, down, hori=""):  # 判斷 Y 軸
    if y > 0: return top
    elif y < 0: return down
    else: return hori

x = int(input("X軸座標:"))
y = int(input("Y軸座標:"))

if x > 0:
    position = y_coor(y, "第一象限", "第四象限", "右半平面 X 軸上")
elif x < 0:
    position = y_coor(y, "第二象限", "第三象限", "左半平面 X 軸上")
else:
    position = y_coor(y, "上半平面 Y 軸上", "下半平面 Y 軸上")

distance = pow(abs(x), 2) + pow(abs(y), 2)  # 計算距離
print("該點位於原點") if distance == 0 else print(f"該點位於{position}，離原點距離為根號{distance}")