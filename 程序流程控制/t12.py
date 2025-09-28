# 使用while循环求1~100的和，以及1~100的所有奇数和、偶数和
i = 0; sum = 0
sum_odd = 0; sum_even = 0

while i <= 100:
    sum += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    i = i + 1

print(f'1到100的和:{sum},奇数和:{sum_odd},偶数和:{sum_even}')