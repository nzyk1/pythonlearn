# 使用for语句的else子句

hobbies = ' '

for i in range(1, 4):
    s = input('输入三个爱好(按Q或q结束):')
    if s.lower == 'q':
        break
    hobbies += s + ' '
else:
    print('共输入3个爱好')
print(f'爱好有:{hobbies}')