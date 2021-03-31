# 6.14 Задача «Числа Фибоначчи»
n = int(input())
fib = [0, 1]
for i in range(2, n + 2):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[-2])
