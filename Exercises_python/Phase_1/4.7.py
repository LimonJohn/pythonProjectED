# 4.7 Задача «Факториал»
def factorial(number):
    f_num = 1
    for n in range(1, number + 1):
        f_num *= n
    return f_num


N = int(input())
print(factorial(N))
