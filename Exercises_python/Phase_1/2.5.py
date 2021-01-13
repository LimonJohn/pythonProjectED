# 2.5 Минимум из трех чисел
from typing import List

a: List[int] = []
for i in range(3):
    a.append(int(input()))
print(min(a))
