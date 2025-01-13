import pygame 


def valid_arrangment(player_matrix):
    numbers_in_matrix = []

    for row in player_matrix:
        for number in row:
            numbers_in_matrix.append(number)

    if 5 in numbers_in_matrix:
        return True
    elif 5 not in numbers_in_matrix:
        return False
    