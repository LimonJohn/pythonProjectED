# 3.5 Задача «Конец уроков»
last_lesson = int(input())
lt = 540


def time(m):
    return (m // 60), (m % 60)


def lesson_time(last_lesson, lt):
    for i in range(last_lesson - 1):
        if i % 2 == 0:
            lt += 5
        else:
            lt += 15
    return lt


x = lesson_time(last_lesson, lt) + 45 * last_lesson
h, m = time(x)
print(h, m)
