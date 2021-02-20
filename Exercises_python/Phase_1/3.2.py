# 3.2 Задача «МКАД»
m_kad = 109
v = int(input())
t = int(input())
s = v * t
while s < 0:
    s = s + m_kad
while s > 108:
    s = s - m_kad
print(s)
