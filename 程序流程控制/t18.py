# 显示100到200中不能被3整除的数，一行显示10个数

count = 0
for i in range(100, 201):
    if i % 3 != 0 :
        print(i, end=' ')
        count += 1

        if count % 10 == 0:
            print()

