# 6.4 Задача «Утренняя пробежка»
x = int(input())
y = int(input())
i = 1
while y > x:
    x *= 1.1
    i += 1
print(i)
