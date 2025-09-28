# 死循环示例

import math 

while True:
    num = float(input('输入一个正数：'))
    print(f'正数的平方根：{math.sqrt(num)}')

print('循环结束')