# .zip函数并循环示例

odds = [1, 3, 5]
evens = [2, 4, 6]

for each_odd, each_even in zip(odds, evens):
    print(f'{each_odd} * {each_even} = {each_odd*each_even}')