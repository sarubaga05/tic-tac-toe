import random
import time

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
time.sleep(3)
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

# Правила игры
print("""Перед началом игры расскажем правила.  
Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). 
Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. 
Первый ход делает игрок, ставящий крестики.
В данной игре вы вводите номер ячейки в формате номер_строки номер_столбца.
Например, если вы введете номер ячейки 1 3, то символ будет проставлен в первой строке, третьем стобце.
""")
time.sleep(10)
print('Игра начинается, удачи!')
print('')
time.sleep(2)


# Считывание ходов игроков
def player_move(name1, name2):

    game_field = [[' ', 1, 2, 3],  # Игровое поле
                  [1, '-', '-', '-'],
                  [2, '-', '-', '-'],
                  [3, '-', '-', '-']]

    for count in range(1, 10):  # Цикл для обработки ходов игроков
        if count % 2 != 0:  # Ход первого игрока
            current_player = name1
            while True:
                cell_1 = input(f'Игрок {name1}, введите номер ячейки: ').split()  # Ввод ячейки
                if len(cell_1) == 2 and cell_1[0].isdigit() and cell_1[1].isdigit():  # Проверка введены ли числа
                    cell_1 = list(map(int, cell_1))
                else:
                    print('Номер ячейки введен некорректно')
                    continue

                if check_field(cell_1, game_field) == 1:  # Если ячейка введена корректно, добавляем её на поле
                    game_field[cell_1[0]][cell_1[1]] = 'x'
                    show_game_field(game_field)
                    print('')
                    break
                elif check_field(cell_1, game_field) == 2:  # Если ячейка введена некорректно, оповещаем об этом
                    print('Номер ячейки введен некорректно')
                else:
                    print('Данная ячейка уже была использована')
        else:  # Ход второго игрока
            current_player = name2
            while True:
                cell_2 = input(f'Игрок {name2}, введите номер ячейки: ').split()  # Ввод ячейки
                if len(cell_2) == 2 and cell_2[0].isdigit() and cell_2[1].isdigit():  # Проверка введены ли числа
                    cell_2 = list(map(int, cell_2))
                else:
                    print('Номер ячейки введен некорректно')
                    continue

                if check_field(cell_2, game_field) == 1:  # Если ячейка введена корректно, добавляем её на поле
                    game_field[cell_2[0]][cell_2[1]] = '0'
                    show_game_field(game_field)
                    print('')
                    break
                elif check_field(cell_2, game_field) == 2:  # Если ячейка введена некорректно, оповещаем об этом
                    print('Номер ячейки введен некорректно')
                else:
                    print('Данная ячейка уже была использована')

        if count >= 5 and check_status(game_field):  # Проверка текущего результата на наличие победы
            print('')
            print(f'Игрок {current_player} победил(а)!')
            time.sleep(2)
            print('')
            print('Спасибо за игру!')
            break
        elif count == 9 and not check_status(game_field):  # Проверка текущего результата на наличие ничьи
            print('')
            print('Ничья!')
            time.sleep(2)
            print('')
            print('Спасибо за игру!')


# Вывод игрового поля на экран
def show_game_field(game_field):
    for row in game_field:
        for col in row:
            print(col, end=' ')
        print()


# Проверка введенной ячейки на корректность
def check_field(cell, game_field):
    if cell[0] < 1 or cell[0] > 3:  # Проверка корректного номера ячейки
        return 2
    elif cell[1] < 1 or cell[1] > 3:  # Проверка корректного номера ячейки
        return 2
    elif game_field[cell[0]][cell[1]] != '-':  # Проверка использована ли ячейка
        return 3
    else:
        return 1


# Проверка текущего результата игры
def check_status(game_field):
    flag = False
    for i in range(1, len(game_field)):  # Проверка наличия трех символов в строке подряд
        for _ in range(1):
            if game_field[i][1] == game_field[i][2] == game_field[i][3] != '-':
                flag = True
                return flag
                #break

#    if flag:
#        return flag

    for i in range(1, len(game_field)):  # Проверка наличия трех символов в столбце подряд
        for _ in range(1):
            if game_field[1][i] == game_field[2][i] == game_field[3][i] != '-':
                flag = True
                return flag
                #break

#    if flag:
#        return flag

    if game_field[1][1] == game_field[2][2] == game_field[3][3] != '-':  # Проверка наличия трех символов по диагонали
        flag = True
        return flag

    if game_field[3][1] == game_field[2][2] == game_field[1][3] != '-':  # Проверка наличия трех символов по диагонали
        flag = True
        return flag

    return flag


if first_move == 1:
    player_move(name_1, name_2)
elif first_move == 2:
    player_move(name_2, name_1)
