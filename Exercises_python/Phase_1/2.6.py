# 2.7 Сколько совпадает чисел
from collections import Counter

s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
mfn = Counter(s).most_common(1)
print(mfn[:1])