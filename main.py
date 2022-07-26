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

    for _ in range(9):
        if first_move % 2 != 0:  # Ход первого игрока
            while True:
                cell_1 = input(f'Игрок {name1}, введите номер ячейки: ').split()
                if len(cell_1) == 2 and cell_1[0].isdigit() and cell_1[1].isdigit():
                    cell_1 = list(map(int, cell_1))
                else:
                    print('Номер ячейки введен некорректно')
                    continue

                if check_field(cell_1, game_field) == 1:
                    game_field[cell_1[0]][cell_1[1]] = 'x'
                    show_game_field(game_field)
                    break
                elif check_field(cell_1, game_field) == 2:
                    print('Номер ячейки введен некорректно')
                else:
                    print('Данная ячейка уже была использована')
        else:  # Ход второго игрока
            while True:
                cell_2 = input(f'Игрок {name2}, введите номер ячейки: ').split()
                if len(cell_2) == 2 and cell_2[0].isdigit() and cell_2[1].isdigit():
                    cell_2 = list(map(int, cell_2))
                else:
                    print('Номер ячейки введен некорректно')
                    continue

                if check_field(cell_2, game_field) == 1:
                    game_field[cell_2[0]][cell_2[1]] = '0'
                    show_game_field(game_field)
                    break
                elif check_field(cell_2, game_field) == 2:
                    print('Номер ячейки введен некорректно')
                else:
                    print('Данная ячейка уже была использована')

        first_move += 1
        if check_status(game_field):
            pass


def show_game_field(game_field):  # Вывод игрового поля на экран
    for row in game_field:
        for col in row:
            print(col, end=' ')
        print()


def check_field(cell, game_field):  # Проверка введенной ячейки на корректность
    if cell[0] < 1 or cell[0] > 3:
        return 2
    elif cell[1] < 1 or cell[1] > 3:
        return 2
    elif game_field[cell[0]][cell[1]] != '-':
        return 3
    else:
        return 1


def check_status(game_field):  # Проверка текущего результата игры
    flag = False
    for i in range(1, len(game_field) - 1):
        for _ in range(1):
            if game_field[i][1] == game_field[i][2] == game_field[i][3]:
                flag = True
                break

    if flag:
        return flag

    for i in range(1, len(game_field) - 1):
        for _ in range(1):
            if game_field[1][i] == game_field[2][i] == game_field[3][i]:
                flag = True
                break

    if flag:
        return flag


'''
if first_move == 1:
    player_move(name_1, name_2, first_move)
elif first_move == 2:
    player_move(name_2, name_1, first_move)
'''

player_move(name_1, name_2, first_move)
