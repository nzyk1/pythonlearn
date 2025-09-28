# 利用for循环求1~100中所有奇数的和以及偶数的和

sum_odd = 0; sum_even = 0

for i in range(1, 101):
    if i % 2 != 0:
        sum_odd += i
    else:
        sum_even += i

print('1到100奇数和:', sum_odd)
print('1到100偶数和:', sum_even)