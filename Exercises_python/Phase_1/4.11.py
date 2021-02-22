# 4.11 Задача «Потерянная карточка»
N = int(input())
sum_r = 0
sum_i = 0
for i in range(1, N):
    sum_r += int(input())
for i in range(N + 1):
    sum_i += i
print(sum_i - sum_r)
