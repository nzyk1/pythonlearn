# 使用continue语句跳过循环。输入学生成绩（按Q或q结束），成绩<0,重新输入。统计学生人数和平均成绩。

total = 0
count = 0

while True:
    score = input("输入成绩(Q或q结束): ")
    
    if score.lower() == 'q':
        break
    
    if float(score) < 0:
        print("成绩无效，重新输入")
        continue
    
    total += float(score)
    count += 1

if count > 0:
    print(f"人数: {count}")
    print(f"平均分: {total/count:.1f}")
else:
    print("没有输入成绩")
