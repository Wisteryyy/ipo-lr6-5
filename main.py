import random # библиотека random

random_numbers = [random.randint(-50, 50) for _ in range(25)] # список из 25 случайных чисел в диапазоне от -50 до 50

count_positive = 0 # количество положительных чисел
count_negative = 0 # количество отрицательных чисел
count_zero = 0 # количество нулевых

for number in random_numbers: # перебираем числа в сгенерированном списке
    if number > 0: # если число положительное
        count_positive += 1 # увеличиваем счетчик положительных чисел
    elif number < 0: # если отрицательное
        count_negative += 1 # увеличиваем счетчик отрицательных чисел
    else: # если нулевое
        count_zero += 1 # увеличиваем счетчик нулевых

total_count = len(random_numbers) # количество чисел в списке
percentage_positive = (count_positive / total_count) * 100 # вычисляем процент положительных
percentage_negative = (count_negative / total_count) * 100 # отрицательных
percentage_zero = (count_zero / total_count) * 100 # и нулевых

max_value = max(random_numbers) # находим максимальный
min_value = min(random_numbers) # и минимальный

print(f"Положительные элементы: {count_positive} ({percentage_positive}%)") # выводим
print(f"Отрицательные элементы: {count_negative} ({percentage_negative}%)") # выводим
print(f"Нулевые элементы: {count_zero} ({percentage_zero}%)") # выводим
print(f"Самое большое значение: {max_value}") # выводим
print(f"Самое маленькое значение: {min_value}") # выводим
