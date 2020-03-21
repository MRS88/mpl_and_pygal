import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
plt.plot(input_values, cubes, linewidth=5)

# Назначение заголовка диаграммы и мето осей
plt.title('Cubes Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)

plt.show()
