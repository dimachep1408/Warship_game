import pygame


def test_valid_arrangment(self, player_matrix):
    list_numbers = []

    for row in player_matrix:
        for number in row:
            list_numbers.append(number)


    if 5 in list_numbers:   
        return True
    else:
        return False