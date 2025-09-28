# 显示Fibonacci数列前20项,每行显示4项

f1 = 1
f2 = 1

for i in range(1, 11) :
    print(f'{f1:6d}, {f2:6d}', end=' ')
    
    if i % 2 == 0:
        print()

    f1 += f2
    f2 += f1
