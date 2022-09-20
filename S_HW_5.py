# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')


# Создайте программу для игры в ""Крестики-нолики"".

maps = [1,2,3,
        4,5,6,
        7,8,9]

victories = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

def print_maps():     
    print(maps[0], end =" ")       
    print(maps[1], end =" ")
    print(maps[2])

    print(maps[3], end =" ")
    print(maps[4], end =" ")
    print(maps[5])

    print(maps[6], end =" ")
    print(maps[7], end =" ")
    print(maps[8])
     
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol    

def get_result():
    win = ""
    for i in victories:
        if maps [i[0]] == "X" and maps[i[1]] == "X" and maps [i[2]] == "X":
            win = "Игрок 1"
        if maps [i[0]] == "O" and maps[i[1]] == "O" and maps [i[2]] == "O":         
            win = "Игрок 2"
    return win
game_over = False
player1 = True
while game_over == False:
    print_maps()
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
    step_maps(step,symbol)
    win = get_result()
    if win !="":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)
print_maps()
print("Победил", win)    
        



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")