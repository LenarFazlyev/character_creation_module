<<<<<<< HEAD
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
          'квадратного корня из заданного числа')
print(message)

def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Печатает вычесленный квадратный корень."""
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {calculate_square_root(your_number)}')


print(message)
calc(25.5)
=======
# Тестовые данные.
TEST_DATA = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8

def add_rep(current_rep: float, rep_points: float, buf_effect: bool) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep

def remove_rep(current_rep: float, rep_points: float, debuf_effect: bool) -> float:
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep

def main(duel_res: list) -> None:
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return f'После {len(duel_res)} поединков, репутация персонажа — {current_rep:.3f} очков.'


# Тестовый вызов функции main.
print(main(TEST_DATA))
>>>>>>> facf83257309f98d5436fa3653b2cde9c2bc5c99
