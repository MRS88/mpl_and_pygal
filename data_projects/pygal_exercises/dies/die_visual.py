import pygal
from die import Die

# Создание кубиков D8
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_nub in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Анализ результатов
frequincies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results + 1):
    frequincy = results.count(value)
    frequincies.append(frequincy)

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling three D6 5000 times."
hist.x_labels = [str(i) for i in range(3, max_results + 1)]
hist.x_title = 'Results'
hist.y_title = 'Frequincy of Result'

hist.add('D6 + D6 + D6', frequincies)
hist.render_to_file('die_visual.svg')
