# 7.1 Задача «Четные индексы»
# digits = [int(digits) for digits in input().split()]
# evenIndex = []
# for i in range(len(digits)):
#     if i % 2 == 0:
#         evenIndex.append(digits[i])
# for elem in evenIndex:
#     print(elem, end=' ')
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
