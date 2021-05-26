# 7.7 Задача «Шеренга»
height = [int(digits) for digits in input().split()]
x = int(input())
j = 1
for i in range(0, len(height)):
    if height[i] >= x:
        j += 1
print(j)
