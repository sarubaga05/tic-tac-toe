import random
import time

first_move = None
'''
print('Приветствую вас в игре крестики-нолики!')  # Вступление
time.sleep(1)
print('...')
time.sleep(1)

print('Представьтесь пожалуйста')  # Ввод имен игроков
time.sleep(1)
name_1 = input('Введите имя игрока номер 1: ')
time.sleep(1)
name_2 = input('Введите имя игрока номер 2: ')
time.sleep(1)
print('...')
time.sleep(1)

print('Сейчас определим кто ходит первым')  # Выбор за кем первый ход
time.sleep(1)
print('...')
time.sleep(1)
print('Бросаем монетку')
print('...')
time.sleep(1)
coin = random.random()
if coin < 0.5:
    print(f'Игру начинает игрок {name_1}')
    first_move = 1
else:
    print(f'Игру начинает игрок {name_2}')
    first_move = 2
time.sleep(1)
print('')
print('')
time.sleep(2)

print("""Перед началом игры напомним правила.  # Правила игры
Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). 
Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. 
Первый ход делает игрок, ставящий крестики.
""")
time.sleep(10)
print('Игра начинается, удачи!')
time.sleep(2)
'''

name_1 = 'test1'
name_2 = 'test2'


def player_move(name1, name2, first_move):  # Считывание ходов игроков
    first_move = 1

    game_field = [[' ', 1, 2, 3],  # Игровое поле
                  [1, '-', '-', '-'],
                  [2, '-', '-', '-'],
                  [3, '-', '-', '-']]

    for i in range(9):
        if first_move % 2 != 0:  # Ход первого игрока
            while True:
                cell_1 = list(map(int, (input(f'Игрок {name1}, введите номер ячейки: ').split())))
                if check_field(cell_1):
                    game_field[cell_1[0]][cell_1[1]] = 'x'
                    show_game_field(game_field)
                else:
                    pass
        else:  # Ход второго игрока
            while True:
                cell_2 = list(map(int, (input(f'Игрок {name2}, введите номер ячейки: ').split())))
                if check_field(cell_2):
                    game_field[cell_2[0]][cell_2[1]] = '0'
                    show_game_field(game_field)
                else:
                    pass

        check_status(game_field)
        first_move += 1


def show_game_field(game_field):  # Вывод игрового поля на экран
    for row in game_field:
        for col in row:
            print(col, end=' ')
        print()


def check_field(cell):  # Проверка введенной ячейки на корректность
    pass


def check_status(game_field):  # Проверка текущего результата игры
    pass


'''
if first_move == 1:
    player_move(name_1, name_2, first_move)
elif first_move == 2:
    player_move(name_2, name_1, first_move)
'''

player_move(name_1, name_2, first_move)
