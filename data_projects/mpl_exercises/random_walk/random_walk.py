from step import get_step

class RandomWalk():
    """Класс для генерирования случайных блужданий"""
    def __init__(self, num_points=50000):
        """Инициализирует атрибуты блуждания"""
        self.num_points = num_points

        # Все блуждания начинаются с точкии (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания"""
        # Шаги генерируются для достижения нужной длины
        while len(self.x_values) < self.num_points:
            x_step = get_step()
            y_step = get_step()

            # Отклонение нулевых перемещений
            if x_step ==0 and y_step == 0:
                continue

            # Вычисление значений x и y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
