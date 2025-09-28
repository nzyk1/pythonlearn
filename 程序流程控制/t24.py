# 使用牛顿迭代法解平方根

E = 1e-15
a = float(input('输入正实数a:'))
t = a
while abs(t -a/t) > (E*t):
    t = (a/t + t) / 2.0
print(t)

