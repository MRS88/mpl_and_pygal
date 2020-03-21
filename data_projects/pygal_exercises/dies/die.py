from random import randint

class Die():
    """Класс, представляющий один кубик"""
    def __init__(self, num_sides=6):
        """По умолчанию используется 6-гранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число от 1 до 6"""
        return randint(1, self.num_sides)
