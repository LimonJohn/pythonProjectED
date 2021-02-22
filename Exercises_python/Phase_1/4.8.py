# 4.9 Задача «Сумма факториалов»
def sum_factorial(number):
    f_num = 1
    sum_f = 0
    for n in range(1, number + 1):
        f_num *= n
        sum_f += f_num
    return sum_f


N = int(input())
print(sum_factorial(N))
