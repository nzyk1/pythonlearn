# map函数和循环

print(list(map(abs,[-1, -2, -3])))

print(list(map(pow,range(2),range(2))))

print(list(map(ord, 'abc')))

print(list(map(lambda x,y: x +y , 'a', 'b')))
