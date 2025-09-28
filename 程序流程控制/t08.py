#if语句嵌套结构计算分段函数

x = int(input("x:"))

if (x >= 0):
    if(x > 0):
        y = 1
    else:
        y = 0
else:
    y = -1

print("分段函数y:", y)