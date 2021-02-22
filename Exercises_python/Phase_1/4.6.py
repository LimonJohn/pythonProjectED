# 4.6 Задача «Сумма кубов»
sum_cube = 0
n = int(input())
for i in range(1, n + 1):
    sum_cube = sum_cube + i ** 3
print(sum_cube)
