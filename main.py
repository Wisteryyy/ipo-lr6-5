import random

k = [random.randint(-50, 50) for _ in range(25)]

p = 0
o = 0
n = 0

for num in k:
    if num > 0:
        p += 1
    elif num < 0:
        o += 1
    else:
        n += 1

vse = len(k)
perP = (p / vse) * 100
perO = (o / vse) * 100
perN = (n / vse) * 100

maxi = max(k)
mini = min(k)

print(f"Положительные элементы: {p} ({perP}%)")
print(f"Отрицательные элементы: {o} ({perO}%)")
print(f"Нулевые элементы: {n} ({perN}%)")
print(f"Самое большое значение: {maxi}")
print(f"Самое маленькое значение: {mini}")
