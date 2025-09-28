# 利用嵌套循环打印乘法表

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j :2d}', end='  ')
#     print( )

# 右下三角格式
for i in range(1, 10):
    for j in range(1, i + 1):  # 修改每行的列数等于行号
        print(f'{j}*{i}={i*j}', end='\t')  # 使用制表符对齐
    print()     


#阶梯递减格式
# for i in range(1, 10):
#     # 计算缩进空格数
#     indent = ' ' * (i - 1) * 8  # 调整空格数
#     print(indent, end='')
    
#     for j in range(i, 10):  
#         print(f'{i}*{j}={i*j :2d}', end='\t')
#     print()