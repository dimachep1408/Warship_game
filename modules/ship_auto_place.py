from random import *


list_ships = []
for i in range(12):
    list_ships.append([])
    for j in range(12):
        list_ships[i].append(0)

def auto_ship():
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    def get_random_number():
        global r1, r2, r3
        r1 = randint(1, 10)
        r2 = randint(1, 10)
        r3 = randint(0, 1)
    while w1 < 4:
        get_random_number()
        if list_ships[r1][r2] == 0:
            for i in range(2):
                list_ships[r1 + i][r2] = 1
                list_ships[r1 + i][r2 + 1] = 1
                list_ships[r1 + i][r2 - 1] = 1
            list_ships[r1][r2] = 2
            list_ships[r1 - 1][r2] = 1
            list_ships[r1 - 1][r2 - 1] = 1
            list_ships[r1 - 1][r2 + 1] = 1
            w1 += 1
    while w2 < 3:
        get_random_number()
        if r3 == 0:
            if r1 != 1:
                if list_ships[r1][r2] == 0 and list_ships[r1 - 1][r2] == 0:
                    for i in range(3):
                        list_ships[r1 - i][r2] = 1
                        list_ships[r1 - i][r2 - 1] = 1
                        list_ships[r1 - i][r2 + 1] = 1
                    list_ships[r1][r2] = 2
                    list_ships[r1 - 1][r2] = 2
                    list_ships[r1 + 1][r2] = 1
                    list_ships[r1 + 1][r2 - 1] = 1
                    list_ships[r1 + 1][r2 + 1] = 1
                    w2 += 1
        elif r3 == 1:
            if r2 != 10:
                if list_ships[r1][r2] == 0 and list_ships[r1][r2 + 1] == 0:
                    for i in range(3):
                        list_ships[r1][r2 + i] = 1
                        list_ships[r1 - 1][r2 + i] = 1
                        list_ships[r1 + 1][r2 + i] = 1
                    list_ships[r1][r2] = 2
                    list_ships[r1][r2 + 1] = 2
                    list_ships[r1][r2 - 1] = 1
                    list_ships[r1 - 1][r2 - 1] = 1
                    list_ships[r1 + 1][r2 - 1] = 1
                    w2 += 1
    while w3 < 2:
        get_random_number()
        if r3 == 0:
            if r1 != 1 and r1 != 2:
                if list_ships[r1][r2] == 0 and list_ships[r1 - 1][r2] == 0 and list_ships[r1 - 2][r2] == 0:
                    for i in range(4):
                        list_ships[r1 - i][r2] = 1
                        list_ships[r1 - i][r2 - 1] = 1
                        list_ships[r1 - i][r2 + 1] = 1
                    list_ships[r1][r2] = 2
                    list_ships[r1 - 1][r2] = 2
                    list_ships[r1 - 2][r2] = 2
                    list_ships[r1 + 1][r2] = 1
                    list_ships[r1 + 1][r2 - 1] = 1
                    list_ships[r1 + 1][r2 + 1] = 1
                    w3 += 1
        elif r3 == 1:
            if r2 != 10 and r2 != 9:
                if list_ships[r1][r2] == 0 and list_ships[r1][r2 + 1] == 0 and list_ships[r1][r2 + 2] == 0:
                    for i in range(4):
                        list_ships[r1][r2 + i] = 1
                        list_ships[r1 - 1][r2 + i] = 1
                        list_ships[r1 + 1][r2 + i] = 1   
                    list_ships[r1][r2] = 2
                    list_ships[r1][r2 + 1] = 2
                    list_ships[r1][r2 + 2] = 2
                    list_ships[r1][r2 - 1] = 1
                    list_ships[r1 - 1][r2 - 1] = 1
                    list_ships[r1 + 1][r2 - 1] = 1
                    w3 += 1 
    while w4 < 1:
        get_random_number()
        if r3 == 0:
            if r1 != 1 and r1 != 2 and r1 != 3:
                if list_ships[r1][r2] == 0 and list_ships[r1 - 1][r2] == 0 and list_ships[r1 - 2][r2] == 0 and list_ships[r1 - 3][r2] == 0:
                    for i in range(5):
                        list_ships[r1 - i][r2] = 1
                        list_ships[r1 - i][r2 - 1] = 1
                        list_ships[r1 - i][r2 + 1] = 1
                    list_ships[r1][r2] = 2
                    list_ships[r1 - 1][r2] = 2
                    list_ships[r1 - 2][r2] = 2
                    list_ships[r1 - 3][r2] = 2
                    list_ships[r1 + 1][r2] = 1
                    list_ships[r1 + 1][r2 - 1] = 1
                    list_ships[r1 + 1][r2 + 1] = 1
                    w4 += 1
        elif r3 == 1:
            if r2 != 10 and r2 != 9 and r2 != 8:
                if list_ships[r1][r2] == 0 and list_ships[r1][r2 + 1] == 0 and list_ships[r1][r2 + 2] == 0 and list_ships[r1][r2 + 3] == 0:
                    for i in range(5):
                        list_ships[r1][r2 + i] = 1
                        list_ships[r1 - 1][r2 + i] = 1
                        list_ships[r1 + 1][r2 + i] = 1
                    list_ships[r1][r2] = 2
                    list_ships[r1][r2 + 1] = 2
                    list_ships[r1][r2 + 2] = 2
                    list_ships[r1][r2 + 3] = 2
                    list_ships[r1 - 1][r2 - 1] = 1
                    list_ships[r1][r2 - 1] = 1
                    list_ships[r1 + 1][r2 - 1] = 1
                    w4 += 1 
auto_ship()
del list_ships[0]
del list_ships[10]
for i in range(10):
    del list_ships[i][0]
    del list_ships[i][10]
for i in list_ships:
    print(i)