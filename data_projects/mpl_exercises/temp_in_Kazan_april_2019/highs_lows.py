"""
В файле kazan_weather_2019_04.csv замер температуры происходит 8 раз в сутки.
Тем самым количество записей также 8 с текущей температурой (в выислениях не участвуют). В 14 и 15 столбце таблицы указаны температурные минимум и максимум дня. Даты записаны в обратном порядке, т.е с 30 по 1 апреля, поэтому в коде будет реверс списка.
"""

import csv

from datetime import datetime
from matplotlib import pyplot as plt

# Чтение температурных максимумов из файла
filename = 'kazan_weather_2019_04.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    # для получения первой строки файла, содержащей заголовки
    header_row = next(reader)

    unsorted_highs, highs_with_comma, highs = [], [], []
    for row in reader:
        # макс.температура указана по индексу 15 в файле
        unsorted_highs.append(row[15])
        # удаляем пустые строки
        highs_with_comma = [max_temp for max_temp in unsorted_highs if max_temp]

    # замен запятых на точки и реверс списка
    for not_comma in highs_with_comma:
        not_comma = float(not_comma.replace(',', '.'))
        highs.append(not_comma)
        highs.reverse()

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Форматирование диаграммы
plt.title('Температурные максимумы, Август 2019', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Температура (С)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
