import pygame, time, os, json
import threading
import server_settings
from modules import FourCellsShip, OneCellsShip, TwoCellsShip, ThreeCellsShip
from modules import Button, Screen, Field

from modules import *

pygame.init()


screen = Screen(
    size_x = 1200,
    size_y = 800,
)
field = Field(dest = (550, 150))

pygame.display.set_caption(title= 'Sea battle')


clock = pygame.time.Clock()
FPS = 1000

user = ''
scene = 'menu'

dark_blue = (0, 0, 139)

flag_message = False


position_ships = {
    "four" : (100, 50),

    "three1" : (50, 115),
    "three2" : (210, 115),
    
    "two1" : (35, 175),
    "two2" : (155, 175),
    "two3" : (275, 175),

    "one1" : (25, 250),
    "one2" : (125, 250),
    "one3" : (225, 250),
    "one4" : (325, 250),
}


matrix_x = [[0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]]

matrix_shots =  [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]


player_menu2_matrix = [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]]

player_matrix = []
for i in range(12):
    player_matrix.append([])
    for j in range(12):
        player_matrix[i].append(0)
        
enemy_matrix = []
for i in range(12):
    enemy_matrix.append([])
    for j in range(12):
        enemy_matrix[i].append(0)

one_cell_ship4 = None

list_clicked_ships = {
    "four" : 0,

    "three1" : 0,
    "three2" : 0,
    
    "two1" : 0,
    "two2" : 0,
    "two3" : 0,

    "one1" : 0,
    "one2" : 0,
    "one3" : 0,
    "one4" : 0,
}

rotation_ships = {
    "four" : 1,

    "three1" : 1,
    "three2" : 1,
    
    "two1" : 1,
    "two2" : 1,
    "two3" : 1,

    "one1" : 1,
    "one2" : 1,
    "one3" : 1,
    "one4" : 1,
}

flag = "menu1"

flag_start = False

flag_first_while = True

first_coordinate = ""

rotate_button = None
button_submit_ships = None

server_x, server_y = (255, 350)

client_x, client_y = (750, 350)

ships_x, ships_y = (190, 500)
screen.game_window.fill(color= "dark blue")

first_flag = False
second_flag = False
third_flag = False

if __name__ == "__main__":
    while True:

        

        if flag == "menu1":
            screen.game_window.fill(color= "dark blue")
            button_server = Button(screen.game_window, position = (server_x, server_y), color = 'gray')
            button_client = Button(screen.game_window, position = (client_x, client_y), color = 'gray')

            button_server.Font(text = 'start server')
            button_client.Font(text = 'join server')


            screen.game_window.blit(button_server.text, dest= (275, 380))   
            screen.game_window.blit(button_client.text, dest= (785, 380))


        elif flag == "menu2":
            screen.game_window.fill(color= "dark blue")


            screen.game_window.blit(field.field_surf, dest = (550, 150))


            
            four_cells_ship = FourCellsShip(matrix_x= matrix_x, x = position_ships["four"][0], y = position_ships["four"][1], rotation= rotation_ships["four"])


            three_cells_ship1 = ThreeCellsShip(matrix_x = matrix_x, x = position_ships["three1"][0], y = position_ships["three1"][1], rotation= rotation_ships["three1"])
            three_cells_ship2 = ThreeCellsShip(matrix_x = matrix_x, x = position_ships["three2"][0], y = position_ships["three2"][1], rotation= rotation_ships["three2"])

            two_cells_ship1 = TwoCellsShip(matrix_x = matrix_x, x = position_ships["two1"][0], y = position_ships["two1"][1], rotation= rotation_ships["two1"])
            two_cells_ship2 = TwoCellsShip(matrix_x = matrix_x, x = position_ships["two2"][0], y = position_ships["two2"][1], rotation= rotation_ships["two2"])
            two_cells_ship3 = TwoCellsShip(matrix_x = matrix_x, x = position_ships["two3"][0], y = position_ships["two3"][1], rotation= rotation_ships["two3"])


            one_cell_ship1 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one1"][0], y = position_ships["one1"][1], rotation= rotation_ships["one1"])
            one_cell_ship2 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one2"][0], y = position_ships["one2"][1], rotation= rotation_ships["one2"])
            one_cell_ship3 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one3"][0], y = position_ships["one3"][1], rotation= rotation_ships["one3"])
            one_cell_ship4 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one4"][0], y = position_ships["one4"][1], rotation= rotation_ships["one4"])



            screen.game_window.blit(field.field_surf, dest = (550, 150))
            screen.game_window.blit(four_cells_ship.ship_surf, four_cells_ship.ship_rect)

            screen.game_window.blit(three_cells_ship1.ship_surf, three_cells_ship1.ship_rect)
            screen.game_window.blit(three_cells_ship2.ship_surf, three_cells_ship2.ship_rect)

            screen.game_window.blit(two_cells_ship1.ship_surf, two_cells_ship1.ship_rect)
            screen.game_window.blit(two_cells_ship2.ship_surf, two_cells_ship2.ship_rect)
            screen.game_window.blit(two_cells_ship3.ship_surf, two_cells_ship3.ship_rect)

            screen.game_window.blit(one_cell_ship1.ship_surf, one_cell_ship1.ship_rect)
            screen.game_window.blit(one_cell_ship2.ship_surf, one_cell_ship2.ship_rect)
            screen.game_window.blit(one_cell_ship3.ship_surf, one_cell_ship3.ship_rect)
            screen.game_window.blit(one_cell_ship4.ship_surf, one_cell_ship4.ship_rect)




            rotate_button = Button(screen.game_window, position=(190, 375), color="gray")
            rotate_button.Font(text='rotate')
            screen.game_window.blit(rotate_button.text, dest=(245, 410))


            button_submit_ships = Button(screen.game_window, position = (ships_x, ships_y), color = 'gray')
            button_submit_ships.Font(text='submit', font_size=40)
            screen.game_window.blit(button_submit_ships.text, dest=(215, 530))

        elif flag == "game":
            try:
                from server_settings.server import position_enemy_ships
                user = 'server'
                flag_start = True
                from server_settings.server import rotation_enemy_ships, position_shot
            except:
                try:
                    from server_settings.client import position_enemy_ships
                    user = 'client'
                    flag_start = True
                    from server_settings.client import rotation_enemy_ships, position_shot
                except:
                    pass
            try:
                field_player.click(player_matrix, screen.game_window, column = position_shot[0], row = position_shot[1])
                player_matrix2[position_shot[1]][position_shot[0]] = 0
            except:
                pass

            if flag_start:
                if len(player_matrix) > 10:
                    screen.game_window.fill(color="dark blue")
                    field_player = Field(dest = (50, 150))    
                    field_enemy = Field(dest = (650, 150))
                    screen.game_window.blit(field_player.field_surf, dest = (50, 150))
                    screen.game_window.blit(field_enemy.field_surf, dest = (650, 150))
                    four_cells_ship = FourCellsShip(matrix_x= matrix_x, x = position_ships["four"][0] - 500, y = position_ships["four"][1], rotation= rotation_ships["four"])


                    three_cells_ship1 = ThreeCellsShip(matrix_x = matrix_x, x = position_ships["three1"][0] - 500, y = position_ships["three1"][1], rotation= rotation_ships["three1"])
                    three_cells_ship2 = ThreeCellsShip(matrix_x = matrix_x, x = position_ships["three2"][0] - 500, y = position_ships["three2"][1], rotation= rotation_ships["three2"])

                    two_cells_ship1 = TwoCellsShip(matrix_x = matrix_x, x = position_ships["two1"][0] - 500, y = position_ships["two1"][1], rotation= rotation_ships["two1"])
                    two_cells_ship2 = TwoCellsShip(matrix_x = matrix_x, x = position_ships["two2"][0] - 500, y = position_ships["two2"][1], rotation= rotation_ships["two2"])
                    two_cells_ship3 = TwoCellsShip(matrix_x = matrix_x, x = position_ships["two3"][0] - 500, y = position_ships["two3"][1], rotation= rotation_ships["two3"])


                    one_cell_ship1 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one1"][0] - 500, y = position_ships["one1"][1], rotation= rotation_ships["one1"])
                    one_cell_ship2 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one2"][0] - 500, y = position_ships["one2"][1], rotation= rotation_ships["one2"])
                    one_cell_ship3 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one3"][0] - 500, y = position_ships["one3"][1], rotation= rotation_ships["one3"])
                    one_cell_ship4 = OneCellsShip(matrix_x = matrix_x, x = position_ships["one4"][0] - 500, y = position_ships["one4"][1], rotation= rotation_ships["one4"])
                    
                    screen.game_window.blit(four_cells_ship.ship_surf, four_cells_ship.ship_rect)

                    screen.game_window.blit(three_cells_ship1.ship_surf, three_cells_ship1.ship_rect)
                    screen.game_window.blit(three_cells_ship2.ship_surf, three_cells_ship2.ship_rect)

                    screen.game_window.blit(two_cells_ship1.ship_surf, two_cells_ship1.ship_rect)
                    screen.game_window.blit(two_cells_ship2.ship_surf, two_cells_ship2.ship_rect)
                    screen.game_window.blit(two_cells_ship3.ship_surf, two_cells_ship3.ship_rect)

                    screen.game_window.blit(one_cell_ship1.ship_surf, one_cell_ship1.ship_rect)
                    screen.game_window.blit(one_cell_ship2.ship_surf, one_cell_ship2.ship_rect)
                    screen.game_window.blit(one_cell_ship3.ship_surf, one_cell_ship3.ship_rect)
                    screen.game_window.blit(one_cell_ship4.ship_surf, one_cell_ship4.ship_rect)

                    field.matrix_fill(player_matrix, 4, position_ships["four"], rotation_ships['four'])
                    field.matrix_fill(player_matrix, 3, position_ships["three1"], rotation_ships['three1'])
                    field.matrix_fill(player_matrix, 3, position_ships["three2"], rotation_ships['three2'])
                    field.matrix_fill(player_matrix, 2, position_ships["two1"], rotation_ships['two1'])
                    field.matrix_fill(player_matrix, 2, position_ships["two2"], rotation_ships['two2'])
                    field.matrix_fill(player_matrix, 2, position_ships["two3"], rotation_ships['two3'])
                    field.matrix_fill(player_matrix, 1, position_ships["one1"], rotation_ships['one1'])
                    field.matrix_fill(player_matrix, 1, position_ships["one2"], rotation_ships['one2'])
                    field.matrix_fill(player_matrix, 1, position_ships["one3"], rotation_ships['one3'])
                    field.matrix_fill(player_matrix, 1, position_ships["one4"], rotation_ships['one4'])
                    del player_matrix[0]
                    del player_matrix[10]
                    for i in range(10):
                        del player_matrix[i][0]
                        del player_matrix[i][10]
                    print('Player:')
                    for i in player_matrix:
                        print(i)
                    print('')
                try:
                    if len(enemy_matrix) > 10:
                        field.matrix_fill(enemy_matrix, 4, position_enemy_ships["four"], rotation_enemy_ships["four"])
                        for i in range(2):
                            field.matrix_fill(enemy_matrix, 3, position_enemy_ships[f"three{i + 1}"], rotation_enemy_ships[f"three{i + 1}"])
                        for i in range(3):
                            field.matrix_fill(enemy_matrix, 2, position_enemy_ships[f"two{i + 1}"], rotation_enemy_ships[f"two{i + 1}"])
                        for i in range(4):
                            field.matrix_fill(enemy_matrix, 1, position_enemy_ships[f"one{i + 1}"], rotation_enemy_ships[f"one{i + 1}"])
                        del enemy_matrix[0]
                        del enemy_matrix[10]
                        for i in range(10):
                            del enemy_matrix[i][0]
                            del enemy_matrix[i][10]
                        print('Enemy:')
                        for i in enemy_matrix:
                            print(i)
                        enemy_matrix2 = [row[:] for row in enemy_matrix]
                        player_matrix2 = [row[:] for row in player_matrix]
                except:
                    pass
                if len(enemy_matrix) == 10:
                    win = True
                    for i in enemy_matrix2:
                        for j in i:
                            if j == 2:
                                win = False
                                break
                    if win:
                        flag = "win"
                    lose = True
                    for i in player_matrix2:
                        for j in i:
                            if j == 2:
                                lose = False
                                break
                    if lose:
                        flag = "lose"
            else:
                screen.game_window.fill(color="dark blue")
                start_game_text = Button(screen.game_window, position=(150, 150), color="dark blue")
                start_game_text.Font(text='Wait for opponent', font_size=100)
                screen.game_window.blit(start_game_text.text, dest=(300, 350))
                
            
        
        elif flag == "win":
            screen.game_window.fill(color="dark blue")
            win_text = Button(screen.game_window, position=(150, 150), color="dark blue")
            win_text.Font(text='You won', font_size=100)
            screen.game_window.blit(win_text.text, dest=(450, 350))
        
        elif flag == "lose":
            screen.game_window.fill(color="dark blue")
            win_text = Button(screen.game_window, position=(150, 150), color="dark blue")
            win_text.Font(text='You lost', font_size=100)
            screen.game_window.blit(win_text.text, dest=(450, 350))
            
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:


                if button_server.button_clicked(event.pos):
                    if flag == 'menu1':
                        threading.Thread(target= server_settings.start_server).start()
                        flag = "menu2"
                        flag_message = True
                        client_x, client_y = (100000000000, 1000000000000)
                        server_x, server_y = (100000000000, 1000000000000)

                        flag = "menu1"
                        flag = "menu2"
                
                    

                elif button_client.button_clicked(event.pos):
                    if flag == 'menu1':
                        server_settings.connect_client('192.168.0.103', 8080)
                        from server_settings.client import client_socket
                        flag_message = True
                        client_x, client_y = (100000000000, 1000000000000)
                        server_x, server_y = (100000000000, 1000000000000)
                        flag = "menu2"

                        flag = "menu1"
                        flag = "menu2"
 

                if one_cell_ship4 != None:

                    if four_cells_ship.get_clicked(event.pos):
                        print("clicked four")
                        list_clicked_ships["four"] = 1

                        if position_ships["four"] != (150, 50):
                            position_ships["four"] = field.get_clicked_cell_position(event.pos)

                    if three_cells_ship1.get_clicked(event.pos):
                        print("clicked three 1")
                        list_clicked_ships["three1"] = 1                       
                    if three_cells_ship2.get_clicked(event.pos):
                        print("clicked three 2")

                        list_clicked_ships["three2"] = 1

                    if two_cells_ship1.get_clicked(event.pos):
                        print("clicked two 1")
                        list_clicked_ships["two1"] = 1
                    if two_cells_ship2.get_clicked(event.pos):
                        print("clicked two 2")
                        list_clicked_ships["two2"] = 1
                    if two_cells_ship3.get_clicked(event.pos):
                        print("clicked two 3")
                        list_clicked_ships["two3"] = 1

                    if one_cell_ship1.get_clicked(event.pos):
                        print("clicked one 1")
                        list_clicked_ships["one1"] = 1
                    if one_cell_ship2.get_clicked(event.pos):
                        print("clicked one 2")
                        list_clicked_ships["one2"] = 1
                    if one_cell_ship3.get_clicked(event.pos):
                        print("clicked one 3")
                        list_clicked_ships["one3"] = 1
                    if one_cell_ship4.get_clicked(event.pos):
                        print("clicked one 4")
                        list_clicked_ships["one4"] = 1


                # if server_settings.server.message == "connected":
                #     screen.game_window.blit(field.field_surf, dest = (350, 150))
                #     flag = "menu2"

                #     client_x, client_y = (100000000000, 1000000000000)
                #     server_x, server_y = (100000000000, 1000000000000)

                
                if flag_message:
                    try:
                        from server_settings.server import client_socket
                    except:
                        pass
                    
                    if rotate_button != None:
                        screen.game_window.blit(rotate_button.text, dest= (155, 475))


                    if rotate_button and rotate_button.button_clicked(event.pos):


                        ''' position_ships = {
                            "four" : (150, 50),

                            "three1" : (100, 115),
                            "three2" : (260, 115),
                            
                            "two1" : (85, 175),
                            "two2" : (205, 175),
                            "two3" : (325, 175),

                            "one1" : (75, 250),
                            "one2" : (175, 250),
                            "one3" : (275, 250),
                            "one4" : (375, 250),
                        }
                        '''
    
                                


                        if position_ships["four"] == (100, 50) or position_ships["four"] == (50, 100):
                            if rotation_ships["four"]:
                                rotation_ships["four"] = 0
                                position_ships["four"] = (50, 100)

                            else:
                                rotation_ships["four"] = 1
                                position_ships["four"] = (100, 50)


                        if position_ships["three1"] == (50, 115) or  position_ships["three1"] == (115, 50):
                            if rotation_ships["three1"]:
                                rotation_ships["three1"] = 0
                                position_ships["three1"] = (115, 50)
                            else:
                                rotation_ships["three1"] = 1
                                position_ships["three1"] = (50, 115)
                        
                        if position_ships["three2"] == (210, 115) or  position_ships["three2"] == (115, 210):
                            if rotation_ships["three2"]:
                                rotation_ships["three2"] = 0
                                position_ships["three2"] = (115, 210)
                                
                            else:
                                rotation_ships["three2"] = 1
                                position_ships["three2"] = (210, 115)



                        if position_ships["two1"] == (35, 175) or position_ships["two1"] == (175, 35):
                            if rotation_ships["two1"]:
                                rotation_ships["two1"] = 0
                                position_ships["two1"] = (175, 35)
                            else:
                                rotation_ships["two1"] = 1
                                position_ships["two1"] = (35, 175)

                        if position_ships["two2"] == (155, 175) or position_ships["two2"] == (175, 155):
                            if rotation_ships["two2"]:
                                rotation_ships["two2"] = 0
                                position_ships["two2"] = (175, 155)
                            else:
                                rotation_ships["two2"] = 1
                                position_ships["two2"] = (155, 175)

                        if position_ships["two3"] == (275, 175) or position_ships["two3"] == (175, 275):
                            if rotation_ships["two3"]:
                                rotation_ships["two3"] = 0
                                position_ships["two3"] = (175, 275)
                            else:
                                rotation_ships["two3"] = 1
                                position_ships["two3"] = (275, 175)



                        if position_ships["one1"] == (25, 250) or position_ships["one1"] == (250, 25):
                            if rotation_ships["one1"]:
                                rotation_ships["one1"] = 0
                                position_ships["one1"] = (250, 25)
                            else:
                                rotation_ships["one1"] = 1
                                position_ships["one1"] = (25, 250)

                        if position_ships["one2"] == (125, 250) or position_ships["one2"] == (250, 125):
                            if rotation_ships["one2"]:
                                rotation_ships["one2"] = 0
                                position_ships["one2"] = (250, 125)                                
                            else:
                                rotation_ships["one2"] = 1
                                position_ships["one2"] = (125, 250)
                        if position_ships["one3"] == (225, 250) or position_ships["one3"] == (250, 225):
                            if rotation_ships["one3"]:
                                rotation_ships["one3"] = 0
                                position_ships["one3"] = (250, 225)
                                        
                            else:
                                rotation_ships["one3"] = 1
                                position_ships["one3"] = (225, 250)
        

                        if position_ships["one4"] == (325, 250) or position_ships["one4"] == (250, 325):
                            if rotation_ships["one4"]:
                                rotation_ships["one4"] = 0
                                position_ships["one4"] = (250, 325)

                            else:
                                rotation_ships["one4"] = 1
                                position_ships["one4"] = (325, 250)

                            
                    if button_submit_ships and button_submit_ships.button_clicked(event.pos):
                        matrix_ships = [
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        ]
                        

                        numbers_matrix_ships = []


                        field.matrix_fill(matrix_ships, 4, position_ships["four"], rotation_ships['four'])
                        field.matrix_fill(matrix_ships, 3, position_ships["three1"], rotation_ships['three1'])
                        field.matrix_fill(matrix_ships, 3, position_ships["three2"], rotation_ships['three2'])
                        field.matrix_fill(matrix_ships, 2, position_ships["two1"], rotation_ships['two1'])
                        field.matrix_fill(matrix_ships, 2, position_ships["two2"], rotation_ships['two2'])
                        field.matrix_fill(matrix_ships, 2, position_ships["two3"], rotation_ships['two3'])
                        field.matrix_fill(matrix_ships, 1, position_ships["one1"], rotation_ships['one1'])
                        field.matrix_fill(matrix_ships, 1, position_ships["one2"], rotation_ships['one2'])
                        field.matrix_fill(matrix_ships, 1, position_ships["one3"], rotation_ships['one3'])
                        field.matrix_fill(matrix_ships, 1, position_ships["one4"], rotation_ships['one4'])


                        
                        for row in matrix_ships:
                            print(row)
                            for number in row:
                                numbers_matrix_ships.append(number)
                        
                        if 5 not in numbers_matrix_ships:
                            if position_ships["four"] == (100, 50) or position_ships["four"] == (50, 100) or position_ships["three1"] == (50, 115) or  position_ships["three1"] == (115, 50) or position_ships["three2"] == (210, 115) or  position_ships["three2"] == (115, 210) or position_ships["two2"] == (155, 175) or position_ships["two2"] == (175, 155) or position_ships["two1"] == (35, 175) or position_ships["two1"] == (175, 35)or position_ships["two3"] == (275, 175) or position_ships["two3"] == (175, 275)or position_ships["one1"] == (25, 250) or position_ships["one1"] == (250, 25)or position_ships["one2"] == (125, 250) or position_ships["one2"] == (250, 125)or position_ships["one3"] == (225, 250) or position_ships["one3"] == (250, 225) or position_ships["one4"] == (325, 250) or position_ships["one4"] == (250, 325):
                                position_ships = {
                                    "four" : (100, 50),

                                    "three1" : (50, 115),
                                    "three2" : (210, 115),
                                    
                                    "two1" : (35, 175),
                                    "two2" : (155, 175),
                                    "two3" : (275, 175),

                                    "one1" : (25, 250),
                                    "one2" : (125, 250),
                                    "one3" : (225, 250),
                                    "one4" : (325, 250),
                                }
                                rotation_ships = {
                                    "four" : 1,

                                    "three1" : 1,
                                    "three2" : 1,
                                    
                                    "two1" : 1,
                                    "two2" : 1,
                                    "two3" : 1,

                                    "one1" : 1,
                                    "one2" : 1,
                                    "one3" : 1,
                                    "one4" : 1,
                                }
                            else:


                                # if flag_start:
                                    client_socket.send(f'position/{position_ships}'.encode())
                                    flag_message = False
                                    flag = "game"
                                    screen.game_window.fill(color= "dark blue")
                                    time.sleep(1)
                                    client_socket.send(f'rotation/{rotation_ships}'.encode())
                                # else:
                                #     screen.game_window.fill(color="dark blue")
                                #     start_game_text = Button(screen.game_window, position=(150, 150), color="dark blue")
                                #     start_game_text.Font(text='Wait for opponent connect', font_size=100)
                                #     screen.game_window.blit(start_game_text.text, dest=(200, 350))
                        else:
                            position_ships = {
                                "four" : (100, 50),

                                "three1" : (50, 115),
                                "three2" : (210, 115),
                                
                                "two1" : (35, 175),
                                "two2" : (155, 175),
                                "two3" : (275, 175),

                                "one1" : (25, 250),
                                "one2" : (125, 250),
                                "one3" : (225, 250),
                                "one4" : (325, 250),
                            }
                            rotation_ships = {
                                "four" : 1,

                                "three1" : 1,
                                "three2" : 1,
                                
                                "two1" : 1,
                                "two2" : 1,
                                "two3" : 1,

                                "one1" : 1,
                                "one2" : 1,
                                "one3" : 1,
                                "one4" : 1,
                            }

                if flag == "game":

                    try:
                        from server_settings.server import rotation_enemy_ships
                    except ImportError:
                        try:
                            from server_settings.client import rotation_enemy_ships
                        except ImportError:
                            pass

                    print(rotation_enemy_ships)
                                        
                    try:
                        if user == "server":
                            path_to_json = os.path.abspath(__file__ + "/../data_s.json")
                        elif user == "client":
                            path_to_json = os.path.abspath(__file__ + "/../data_c.json")
                        with open(path_to_json, 'r') as f:
                            data_turn = json.load(f)
                        if data_turn['turn']:
                            hit = field_enemy.click(enemy_matrix, screen.game_window, event.pos)
                            column, row = field_enemy.get_clicked_cell(event.pos)
                            print(enemy_matrix[row][column])
                            print(enemy_matrix2[row][column])
                            enemy_matrix2[row][column] = 0
                            print(enemy_matrix[row][column])
                            print(enemy_matrix2[row][column])
                            pygame.display.flip()
                            client_socket.send(f'/{field_enemy.get_clicked_cell(event.pos)}'.encode())
                            time.sleep(1)
                            
                            clicked_cell = [field_enemy.get_clicked_cell(event.pos)[1], field_enemy.get_clicked_cell(event.pos)[0]]

                            matrix_shots[clicked_cell[0]][clicked_cell[1]] = 2
                            print(enemy_matrix[clicked_cell[0]][clicked_cell[1] + 1])
                            print(clicked_cell)

                            if matrix_shots[clicked_cell[0]][clicked_cell[1]] == enemy_matrix[clicked_cell[0]][clicked_cell[1]] and first_flag and second_flag and third_flag:
                                four_cells_ship = FourCellsShip(matrix_x= matrix_x, x = first_coordinates[0], y = first_coordinates[1], rotation= rotation_ships["four"], killed = True)
                                screen.game_window.blit(four_cells_ship.ship_surf, four_cells_ship.ship_rect)
                                print("")
                                first_flag = False
                                second_flag = False
                                third_flag = False
                            if matrix_shots[clicked_cell[0]][clicked_cell[1]] == enemy_matrix[clicked_cell[0]][clicked_cell[1]] and first_flag and second_flag and not third_flag:
                                if enemy_matrix[clicked_cell[0]][clicked_cell[1] + 1] % 3 == 0:
                                    first_flag = False
                                    second_flag = False
                                    third_flag = False
                                    three_cells_ship = ThreeCellsShip(matrix_x = matrix_x, x = first_coordinates[0], y = first_coordinates[1], rotation= rotation_ships["three1"], killed = True)
                                    screen.game_window.blit(three_cells_ship.ship_surf, three_cells_ship.ship_rect)
                                else:
                                    print("")
                                    third_flag = True

                            if matrix_shots[clicked_cell[0]][clicked_cell[1]] == enemy_matrix[clicked_cell[0]][clicked_cell[1]] and first_flag and not second_flag:
                                if enemy_matrix[clicked_cell[0]][clicked_cell[1] + 1] % 3 == 0:
                                    first_flag = False
                                    second_flag = False
                                    third_flag = False
                                    two_cells_ship1 = TwoCellsShip(matrix_x = matrix_x, x = first_coordinates[0], y = first_coordinates[1], rotation= rotation_ships["two1"], killed = True)
                                    screen.game_window.blit(two_cells_ship1.ship_surf, two_cells_ship1.ship_rect)
                                else:
                                    print("")
                                    second_flag = True

                            if matrix_shots[clicked_cell[0]][clicked_cell[1]] == enemy_matrix[clicked_cell[0]][clicked_cell[1]] and not first_flag:
                                if enemy_matrix[clicked_cell[0]][clicked_cell[1] + 1] % 3 == 0:
                                    one_cell_ship1 = OneCellsShip(matrix_x = matrix_x, x = field_enemy.get_clicked_cell_position(event.pos)[0], y = field_enemy.get_clicked_cell_position(event.pos)[1], rotation= rotation_ships["one1"], killed = True)
                                    screen.game_window.blit(one_cell_ship1.ship_surf, one_cell_ship1.ship_rect)
                                    print("aefimpehajgoui")
                                
                                else:
                                    first_flag = True

                                    first_coordinates = [field_enemy.get_clicked_cell_position(event.pos)[0], field_enemy.get_clicked_cell_position(event.pos)[1]]




                            if not hit:
                                client_socket.send('turn'.encode())
                                data_turn['turn'] = False
                            with open(path_to_json, 'w') as f:
                                json.dump(data_turn, f, indent = 4)
                    except Exception as e:
                        print(e)
 
            if event.type == pygame.MOUSEMOTION:

                if one_cell_ship4 != None:
                    
                    if flag == "menu2":
                        if list_clicked_ships["four"] == 1:
                            position_ships["four"] = (event.pos[0], event.pos[1])


                        if list_clicked_ships["three1"] == 1:
                            position_ships["three1"] = (event.pos[0], event.pos[1])
                        if list_clicked_ships["three2"] == 1:
                            position_ships["three2"] = (event.pos[0], event.pos[1])



                        if list_clicked_ships["two1"] == 1:
                            position_ships["two1"] = (event.pos[0], event.pos[1])
                        if list_clicked_ships["two2"] == 1:
                            position_ships["two2"] = (event.pos[0], event.pos[1])
                        if list_clicked_ships["two3"] == 1:
                            position_ships["two3"] = (event.pos[0], event.pos[1])


                        if list_clicked_ships["one1"] == 1:
                            position_ships["one1"] = (event.pos[0], event.pos[1])
                        if list_clicked_ships["one2"] == 1:
                            position_ships["one2"] = (event.pos[0], event.pos[1])
                        if list_clicked_ships["one3"] == 1:
                            position_ships["one3"] = (event.pos[0], event.pos[1])
                        if list_clicked_ships["one4"] == 1:
                            position_ships["one4"] = (event.pos[0], event.pos[1])


            if event.type == pygame.MOUSEBUTTONUP:

                if flag == 'menu2':

                    if list_clicked_ships["four"]:
                        print(field.get_clicked_cell_position(event.pos))

                        if rotation_ships["four"]:
                            if field.get_clicked_cell(event.pos)[0] > 6:
                                
                                position_ships["four"] = (150, 50)


                            else:
                                old_position_ship = ()
                                position_ships["four"] = field.get_clicked_cell_position(event.pos)
                                for count in range(4):
                                    start_field = (field.get_clicked_cell(event.pos)[1] + 1, field.get_clicked_cell(event.pos)[0])
                                    old_position_ship = start_field
                                    

                                
                                for string in matrix_x:
                                    print(string)
                                print("work")
                                    
                        else:
                            if field.get_clicked_cell(event.pos)[1] > 6:

                                position_ships["four"] = (150, 50)
                            else:
                                position_ships["four"] = field.get_clicked_cell_position(event.pos)




                                


                    
                    if list_clicked_ships["three1"]:
                        if rotation_ships["three1"]:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[0] > 7 :
                                position_ships["three1"] = (100, 115)
                            else:
                                position_ships["three1"] = field.get_clicked_cell_position(event.pos)

                        else:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[1] > 7:
                                position_ships["three1"] = (100, 115)
                            else:
                                position_ships["three1"] = field.get_clicked_cell_position(event.pos)



                        print(position_ships)
                    if list_clicked_ships["three2"]:
                        if rotation_ships["three2"]:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[0] > 7 :
                                position_ships["three2"] = (260, 115)

                            else:
                                position_ships["three2"] = field.get_clicked_cell_position(event.pos)
                        else:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[1] > 7:
                                position_ships["three2"] = (260, 115)

                            else:
                                position_ships["three2"] = field.get_clicked_cell_position(event.pos)



                    if list_clicked_ships["two1"]:
                        if rotation_ships["two1"]:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[0] > 8 :
                                position_ships["two1"] = (85, 175)
                            else:
                                position_ships["two1"] = field.get_clicked_cell_position(event.pos)

                        else:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[1] > 8:
                                position_ships["two1"] = (85, 175)
                            else:
                                position_ships["two1"] = field.get_clicked_cell_position(event.pos)


                    if list_clicked_ships["two2"]:

                        if rotation_ships["two2"]:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[0] > 8 :
                                position_ships["two2"] = (205, 175)
                            else:
                                position_ships["two2"] = field.get_clicked_cell_position(event.pos)

                        else:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[1] > 8:
                                position_ships["two2"] = (205, 175)
                            else:
                                position_ships["two2"] = field.get_clicked_cell_position(event.pos)



                    if list_clicked_ships["two3"]:
                        if rotation_ships["two3"]:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[0] > 8 :
                                position_ships["two3"] = (325, 175)
                            else:
                                position_ships["two3"] = field.get_clicked_cell_position(event.pos)

                        else:
                            print(field.get_clicked_cell_position(event.pos))

                            if field.get_clicked_cell(event.pos)[1] > 8:
                                position_ships["two3"] = (325, 175)
                            else:
                                position_ships["two3"] = field.get_clicked_cell_position(event.pos)



                    if list_clicked_ships["one1"]:
                        print(field.get_clicked_cell_position(event.pos))

                        position_ships["one1"] = field.get_clicked_cell_position(event.pos)


                        print(position_ships)
                    if list_clicked_ships["one2"]:
                        print(field.get_clicked_cell_position(event.pos))

                        position_ships["one2"] = field.get_clicked_cell_position(event.pos)


                        print(position_ships)
                    if list_clicked_ships["one3"]:
                        print(field.get_clicked_cell_position(event.pos))

                        position_ships["one3"] = field.get_clicked_cell_position(event.pos)


                        print(position_ships)
                    if list_clicked_ships["one4"]:
                        print(field.get_clicked_cell_position(event.pos))

                        position_ships["one4"] = field.get_clicked_cell_position(event.pos)


                        print(position_ships)

                    


                    list_clicked_ships = {
                        "four" : 0,

                        "three1" : 0,
                        "three2" : 0,
                        
                        "two1" : 0,
                        "two2" : 0,
                        "two3" : 0,

                        "one1" : 0,
                        "one2" : 0,
                        "one3" : 0,
                        "one4" : 0,
                    } 



            

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        