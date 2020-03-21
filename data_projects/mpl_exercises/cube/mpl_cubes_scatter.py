import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors=None, s=40)

# Назначение заголовка диаграммы и мето осей
plt.title('Cubes Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси
plt.axis([0, 6000, 0, 150000000000])

plt.savefig('cubes_plot.png', bbox_inches='tight')
#plt.show()
