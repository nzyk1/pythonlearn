# 使用break语句终止循环

while 1:
    s = input('输入字符串,按Q或者q结束:')
    if s.upper() == 'Q':
        break
    print(f'字符串长度：{len(s)}')
