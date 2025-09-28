# 判断输入的任意正整数是否为素数

import math

n = int(input('输入大于1的整数n:'))
m = int(math.sqrt(n))

is_flag = True
for i in range(2, m+1):
    if n % i == 0:
        is_prime = False
        break
        
if is_flag:
    print(f'{n}为素数')
else:
    print(f'{n}为合数')
