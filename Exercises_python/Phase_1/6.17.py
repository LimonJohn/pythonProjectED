# 6.17 Задача «Стандартное отклонение»
def mean(x):
    return sum(x) / len(x)


def variance(x):
    v = 0
    for i in range(len(x)):
        v += (x[i] - mean(x)) ** 2
    m = v / (len(x) - 1)
    return m


def sd(x):
    return variance(x) ** 0.5


s = []
s_i = int(input())
while s_i != 0:
    s.append(s_i)
    s_i = int(input())
print(sd(s))
