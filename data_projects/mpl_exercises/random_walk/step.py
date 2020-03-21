from random import choice

def get_step():
    """Определение направления и длины перемещения"""
    direction = choice([1, -1])
    distance = choice(list(range(8)))
    step = direction * distance
    return step
