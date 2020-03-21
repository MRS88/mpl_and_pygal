import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайного блуждания и нанемения точек на диаграмму
    rw = RandomWalk()
    rw.fill_walk()

    # Назначение размера области просмотра
    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(rw.x_values, rw.y_values, linewidth=0.1)

    # Выделение первой, средней и последней точек
    plt.scatter(0, 0, c='red', edgecolors=None, s=10)
    plt.scatter(rw.x_values[len(rw.x_values) // 2], rw.y_values[len(rw.y_values) // 2], c='green', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black', edgecolors=None, s=10)

    # Удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Создать еще раз? (y/n): ')
    if keep_running == 'n':
        break
