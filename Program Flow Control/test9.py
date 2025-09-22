#输入三个数从大到小顺序排序

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if(a < b):
    a, b = b, a
if(a < c):
    a, c = c, a
if(b < c):
    b, c = c, b

print("abc从大到小:", a, b,c)