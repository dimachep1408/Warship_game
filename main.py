import pygame, time, os, json, random, requests, socket, ast
import threading
import server_settings
from modules import FourCellsShip, OneCellsShip, TwoCellsShip, ThreeCellsShip
from modules import Button, Screen, Field, get_ships_position, auto_ship
from modules import *


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)



# coin_flip = random.randint(2)

# print(coin_flip)



pygame.init()

pygame.mixer.init()

screen = Screen(
    size_x = 1200,
    size_y = 800,
)
field = Field(dest = (550, 150))

pygame.display.set_caption(title= 'Sea battle')


clock = pygame.time.Clock()
FPS = 60

user = ''
scene = 'menu'

dark_blue = (0, 0, 139)

flag_message = False


animation_coin_count = 0


btn_click_sound = pygame.mixer.Sound(os.path.abspath(__file__ + "/../sounds/click_sound2.ogg"))
expload_sound = pygame.mixer.Sound(os.path.abspath(__file__ + "/../sounds/exploation.ogg"))


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


kill_position_ships = {
    "four" : [],

    "three1" : [],
    "three2" : [],
    
    "two1" : [],
    "two2" : [],
    "two3" : [],

    "one1" : [],
    "one2" : [],
    "one3" : [],
    "one4" : [],
}


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

button_3x3 = None
attack_3x3 = False

button_aimed_strike = None
aimed_strike = False
list_strikes = []

flag_start = False

flag_first_while = True

first_coordinate = ""

rotate_button = None
button_submit_ships = None
auto_button = None

server_x, server_y = (255, 350)

client_x, client_y = (750, 350)

ships_x, ships_y = (190, 500)

wait = True
first_flag = False
second_flag = False
third_flag = False

enemy_ships_rotation = None

closed_flag = False

bg = pygame.image.load(os.path.abspath(__file__ + "/../images/background_1.jpg"))
bg = pygame.transform.scale(bg, (1200, 800))

blackout_screen_y = -800

blackout_screen = pygame.image.load(os.path.abspath(__file__ + "/../images/black.jpg"))
blackout_screen = pygame.transform.scale(blackout_screen, (1200, 800))

blackout_screen.set_alpha(155)


coinflip = random.randint(1, 2)




animation_coin = [
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip1.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip2.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip3.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip4.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip5.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip6.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip7.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip8.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip9.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip10.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip11.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip5.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip4.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip3.png")),
    pygame.image.load(os.path.abspath(__file__ + "/../images/coinflip2.png")),
]    



ip = ""

name = ""


buttons_position = {
    "red" : [10, 110],
    "green" : [60, 110]
}



pvo_count = 2



war_plane_image = pygame.image.load(os.path.abspath(__file__ + "/../images/war_plane.png"))
war_plane_image = pygame.transform.scale(war_plane_image, (100, 100))

war_plane_rect = war_plane_image.get_rect(topleft = (950, 0))


war_plane_text = Button(screen.game_window, position=(1100, 100), color = "#6ab1db", size= (100, 50))


green_cirlce = pygame.image.load(os.path.abspath(__file__ + "/../images/green_circle.png"))
green_cirlce = pygame.transform.scale(green_cirlce, (30, 30))

green_cirlce_rect = green_cirlce.get_rect(topleft = (buttons_position["red"][0], buttons_position["red"][1]))     

red_circle = pygame.image.load(os.path.abspath(__file__ + "/../images/red_circle.png"))
red_circle = pygame.transform.scale(red_circle, (30, 30))

red_circle_rect = red_circle.get_rect(topleft = (buttons_position["red"][0], buttons_position["red"][1]))   

coins = 50


coins_btn = Button(screen.game_window, position=(0, 0), color = "#6ab1db", size= (100, 50))


wrong_wire_image = pygame.image.load(os.path.abspath(__file__ + "/../images/wrong_wire.png"))
wrong_wire_image = pygame.transform.scale(wrong_wire_image, (100, 90))

wrong_wire_rect = wrong_wire_image.get_rect(topleft = (550, 10))   

wrong_wire_text = Button(screen.game_window, position=(550, 10), color = "#6ab1db", size= (100, 50))




pvo_image = pygame.image.load(os.path.abspath(__file__ + "/../images/pvo.png"))
pvo_image = pygame.transform.scale(pvo_image, (100, 100))

pvo_rect = pvo_image.get_rect(topleft = (450, 10))   

pvo_text = Button(screen.game_window, position=(450, 10), color = "#6ab1db", size= (100, 50))

pvo_coordinates = (0, 0)

pvo_for_cursor = pygame.image.load(os.path.abspath(__file__ + "/../images/pvo.png"))
pvo_for_cursor = pygame.transform.scale(pvo_image, (50, 50))

flag_wrong_wire = False


fear_and_panic_image = pygame.image.load(os.path.abspath(__file__ + "/../images/fear_and_panic.png"))
fear_and_panic_image = pygame.transform.scale(fear_and_panic_image, (150, 100))

fear_and_panic_rect = fear_and_panic_image.get_rect(topleft = (700, 10))   

fear_and_panic_text = Button(screen.game_window, position=(750, 10), color = "#6ab1db", size= (100, 50))

fear_and_panic_count = 0


flag_follow_pvo_coordinates = False





protect_shield_image = pygame.image.load(os.path.abspath(__file__ + "/../images/protect_shield.png"))
protect_shield_image = pygame.transform.scale(protect_shield_image, (150, 150))


if __name__ == "__main__":
    while True:

        screen.game_window.blit(blackout_screen, (0,  blackout_screen_y))

        
            

        if animation_coin_count == len(animation_coin):
            animation_coin_count = 0


        if flag == "menu_load_ip_server":
            screen.game_window.blit(bg, (0,0))


            
            input_ip = pygame.Rect(1500, 300, 200, 50)

            pygame.draw.rect(screen.game_window, "#00ab99", input_ip)

            

            flag = "menu2"

            


        if closed_flag:
            screen.game_window.blit(bg, (0,0))
            
            button_submit_ships.Font(text='submit', font_size=40)




        if flag == "menu1":
            screen.game_window.blit(bg, (0,0))




            coin_sprite = animation_coin[animation_coin_count]
            coin_sprite = pygame.transform.scale(coin_sprite, (100, 100))

            
            
            screen.game_window.blit(coin_sprite, (0, 0))

            

            button_server = Button(screen.game_window, position = (250, 70), color = '#01796F')
            button_client = Button(screen.game_window, position = (750, 70), color = '#01796F')

            button_server.Font(text = 'Create Game')
            button_client.Font(text = 'Join Game')

            screen.game_window.blit(button_server.text, dest= (267, 89))   
            screen.game_window.blit(button_client.text, dest= (780, 89))

            



            # button_server = pygame.transform.scale(button_server, (100, 25))



        elif flag == "menu2":

            screen.game_window.blit(bg, (0, 0))

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




            rotate_button = Button(screen.game_window, position=(610, 20), color="#01796F")
            rotate_button.Font(text='rotate', font_size=40)
            screen.game_window.blit(rotate_button.text, dest=(639, 25))
            
            auto_button = Button(screen.game_window, position=(770, 20), color="#01796F")
            auto_button.Font(text='auto', font_size=40)
            screen.game_window.blit(auto_button.text, dest=(803, 25))

            button_submit_ships = Button(screen.game_window, position = (ships_x, ships_y), color = '#01796F')
            button_submit_ships.Font(text='submit', font_size=40)
            screen.game_window.blit(button_submit_ships.text, dest=(211, 505))
            
            

        elif flag == "game":
            
            try:
                from server_settings.server import position_enemy_ships
                user = 'server'
                flag_start = True
                from server_settings.server import rotation_enemy_ships, position_shot, attack_3x3_position, aimed_strike_position
            except:
                try:
                    from server_settings.client import position_enemy_ships
                    user = 'client'
                    flag_start = True
                    from server_settings.client import rotation_enemy_ships, position_shot, attack_3x3_position, aimed_strike_position
                except:
                    pass
            try:
                field_player.click(player_matrix, screen.game_window, column = position_shot[0], row = position_shot[1])
                player_matrix2[position_shot[1]][position_shot[0]] = 0
            except:
                pass

            try:
                if attack_3x3_position != None:
                    field_player.attack_3x3(player_matrix, screen.game_window, position_attack = attack_3x3_position)
            except:
                pass
            
            try:
                aimed_strike_position[0] -= 600
                field_player.click(player_matrix, screen.game_window, mouse_pos = aimed_strike_position)
            except:
                pass
            
            try:
                if user == "server":
                    path_to_json = os.path.abspath(__file__ + "/../data_s.json")
                elif user == "client":     
                    path_to_json = os.path.abspath(__file__ + "/../data_c.json")
                
                with open(path_to_json, 'r') as f:
                    data_turn = json.load(f)
                
                turn_rect = Button(screen.game_window, position=(350, 20), color="gray", size=(200, 75))
                if data_turn['turn']:
                    turn_rect.Font(text='Your Turn', font_size=40)
                    screen.game_window.blit(turn_rect.text, dest=(380, 25))
                else:
                    turn_rect.Font(text='Enemy Turn', font_size=40)
                    screen.game_window.blit(turn_rect.text, dest=(360, 25))
            except:
                pass
            

            button_3x3 = pygame.image.load(os.path.abspath(__file__ + "/../images/3x3.png"))

            button_3x3 = pygame.transform.scale(button_3x3, (100, 100))

            button_3x3_text = Button(screen.game_window, position=(825, 10), color = "#6ab1db", size= (100, 50))
            button_3x3_text.Font(text='100', font_size=40)

            button_3x3_rect = button_3x3.get_rect(topleft = (800, 10))

            screen.game_window.blit(button_3x3, dest=(800, 10))
            screen.game_window.blit(button_3x3_text.text, dest=(825, 85))
            


            button_aimed_strike = pygame.image.load(os.path.abspath(__file__ + "/../images/aimed_strike.png"))
            
            button_aimed_strike = pygame.transform.scale(button_aimed_strike, (100, 100))

            button_strike_text = Button(screen.game_window, position=(1125,  85), color = "#6ab1db", size= (100, 50))
            button_strike_text.Font(text='200', font_size=40)

            button_aimed_strike_rect = button_aimed_strike.get_rect(topleft = (1100, 10))

            screen.game_window.blit(button_aimed_strike, dest=(1100, 10)) 
            screen.game_window.blit(button_strike_text.text, dest=(1125, 85)) 




            screen.game_window.blit(war_plane_image, (950, 10))

            war_plane_text.Font(text = "150", font_size = 40)
            screen.game_window.blit(war_plane_text.text, dest=(975, 85)) 


            text_background = pygame.Rect(10, 10, 300, 40)
            pygame.draw.rect(screen.game_window, "#6ab1db", text_background)


            coins_btn.Font(text=f'coins:{coins}', font_size=40)
            screen.game_window.blit(coins_btn.text, dest=(10, 10)) 



            if flag_start:
                try:
                    enemy_rotation_ships = rotation_enemy_ships
                except:
                    pass
                
                if len(player_matrix) > 10:
                    screen.game_window.blit(bg, (0,0))

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
                screen.game_window.blit(bg, (0,0))

                start_game_text = Button(screen.game_window, position=(-100, -100), color="dark blue")
                start_game_text.Font(text='Waiting for opponent', font_size=100)
                screen.game_window.blit(start_game_text.text, dest=(270, 50))
                
            
        
        elif flag == "win":
            screen.game_window.blit(bg, (0,0))
            win_text = Button(screen.game_window, position=(-100, -100), color="dark blue")
            win_text.Font(text='You won', font_size=100)
            screen.game_window.blit(win_text.text, dest=(450, 50))
        
        elif flag == "lose":
            screen.game_window.blit(bg, (0,0))
            win_text = Button(screen.game_window, position=(-100, -100), color="dark blue")
            win_text.Font(text='You lost', font_size=100)
            screen.game_window.blit(win_text.text, dest=(450, 50))
            

        







        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                try:
                    from server_settings.client import client_socket
                    client_socket.send("close!")
                except:
                    pass
                pygame.quit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if button_server.button_clicked(event.pos):
                    pygame.mixer.Sound.play(btn_click_sound)
                    if flag == 'menu1':
                        threading.Thread(target= server_settings.start_server).start()
                        flag = "menu2"
                        flag_message = True
                        client_x, client_y = (100000000000, 1000000000000)
                        server_x, server_y = (100000000000, 1000000000000)

                        flag = "menu1"
                        flag = "menu_load_ip_server"
                
                    

                if button_client.button_clicked(event.pos):
                    pygame.mixer.Sound.play(btn_click_sound)
                    if flag == 'menu1':
                        server_settings.connect_client('192.168.0.101', 8080)
                        from server_settings.client import client_socket
                        flag_message = True
                        client_x, client_y = (100000000000, 1000000000000)
                        server_x, server_y = (100000000000, 1000000000000)
                        flag = "menu2"



                        flag = "menu1"
                        flag = "menu2"


                

                # except Exception as e:
                #         print(e)


                        
                

                if one_cell_ship4 != None:

                    if four_cells_ship.get_clicked(event.pos):
                        print("clicked four")
                        list_clicked_ships["four"] = 1

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


                    if rotate_button and rotate_button.button_clicked(event.pos):
                        pygame.mixer.Sound.play(btn_click_sound)

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
                                
                    if auto_button and auto_button.button_clicked(event.pos):
                        pygame.mixer.Sound.play(btn_click_sound)
                        auto_ship(position_ships, rotation_ships, player_matrix)
                        

                            
                    if button_submit_ships and button_submit_ships.button_clicked(event.pos):
                        pygame.mixer.Sound.play(btn_click_sound)
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
                                    screen.game_window.blit(bg, (0,0))
                                    time.sleep(1)
                                    client_socket.send(f'rotation/{rotation_ships}'.encode())
                                # else:
                                #     screen.game_window.blit(bg, (0,0))
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
                try:
                    if field_player.get_clicked_cell_position != None and flag_follow_pvo_coordinates == True:
                        flag_draw_pvo = (field_player.get_clicked_cell(event.pos))
                except NameError:
                    pass
                    

                if flag == "game":

                                 

                    try:
                        from server_settings.server import rotation_enemy_ships, position_enemy_ships
                    except ImportError:
                        try:
                            from server_settings.client import rotation_enemy_ships, position_enemy_ships
                        except ImportError:
                            pass
                                        
                    try:

                        
                        


                        four_cells_ship = FourCellsShip(matrix_x= matrix_x, x = position_enemy_ships["four"][0] + 100, y = position_enemy_ships["four"][1], rotation= rotation_enemy_ships["four"])


                        three_cells_ship1 = ThreeCellsShip(matrix_x = matrix_x, x = position_enemy_ships["three1"][0] + 100, y = position_enemy_ships["three1"][1], rotation= rotation_enemy_ships["three1"])
                        three_cells_ship2 = ThreeCellsShip(matrix_x = matrix_x, x = position_enemy_ships["three2"][0] + 100, y = position_enemy_ships["three2"][1], rotation= rotation_enemy_ships["three2"])

                        two_cells_ship1 = TwoCellsShip(matrix_x = matrix_x, x = position_enemy_ships["two1"][0] + 100, y = position_enemy_ships["two1"][1], rotation= rotation_enemy_ships["two1"])
                        two_cells_ship2 = TwoCellsShip(matrix_x = matrix_x, x = position_enemy_ships["two2"][0] + 100, y = position_enemy_ships["two2"][1], rotation= rotation_enemy_ships["two2"])
                        two_cells_ship3 = TwoCellsShip(matrix_x = matrix_x, x = position_enemy_ships["two3"][0] + 100, y = position_enemy_ships["two3"][1], rotation= rotation_enemy_ships["two3"])


                        one_cell_ship1 = OneCellsShip(matrix_x = matrix_x, x = position_enemy_ships["one1"][0] + 100, y = position_enemy_ships["one1"][1], rotation= rotation_enemy_ships["one1"])
                        one_cell_ship2 = OneCellsShip(matrix_x = matrix_x, x = position_enemy_ships["one2"][0] + 100, y = position_enemy_ships["one2"][1], rotation= rotation_enemy_ships["one2"])
                        one_cell_ship3 = OneCellsShip(matrix_x = matrix_x, x = position_enemy_ships["one3"][0] + 100, y = position_enemy_ships["one3"][1], rotation= rotation_enemy_ships["one3"])
                        one_cell_ship4 = OneCellsShip(matrix_x = matrix_x, x = position_enemy_ships["one4"][0] + 100, y = position_enemy_ships["one4"][1], rotation= rotation_enemy_ships["one4"])

                       

                        if kill_position_ships ==  {"four" : [],"three1" : [],"three2" : [],"two1" : [],"two2" : [],"two3" : [],"one1" : [],"one2" : [],"one3" : [],"one4" : [],}:

                            if rotation_enemy_ships["four"]:
                                kill_position_ships["four"].append(position_enemy_ships["four"])
                                kill_position_ships["four"].append((position_enemy_ships["four"][0] + 50, position_enemy_ships["four"][1]))
                                kill_position_ships["four"].append((position_enemy_ships["four"][0] + 100, position_enemy_ships["four"][1]))
                                kill_position_ships["four"].append((position_enemy_ships["four"][0] + 150, position_enemy_ships["four"][1]))

                            elif rotation_enemy_ships["four"] == 0:
                                kill_position_ships["four"].append(position_enemy_ships["four"])
                                kill_position_ships["four"].append((position_enemy_ships["four"][0], position_enemy_ships["four"][1] + 50))
                                kill_position_ships["four"].append((position_enemy_ships["four"][0] , position_enemy_ships["four"][1] + 100))
                                kill_position_ships["four"].append((position_enemy_ships["four"][0], position_enemy_ships["four"][1] + 150))



                            if rotation_enemy_ships["three1"]:
                                kill_position_ships["three1"].append(position_enemy_ships["three1"])
                                kill_position_ships["three1"].append((position_enemy_ships["three1"][0] + 50, position_enemy_ships["three1"][1]))
                                kill_position_ships["three1"].append((position_enemy_ships["three1"][0] + 100, position_enemy_ships["three1"][1]))
                            elif rotation_enemy_ships["three1"] == 0:
                                kill_position_ships["three1"].append(position_enemy_ships["three1"])
                                kill_position_ships["three1"].append((position_enemy_ships["three1"][0], position_enemy_ships["three1"][1] + 50))
                                kill_position_ships["three1"].append((position_enemy_ships["three1"][0], position_enemy_ships["three1"][1] + 100))

                            if rotation_enemy_ships["three2"]:
                                kill_position_ships["three2"].append(position_enemy_ships["three2"])
                                kill_position_ships["three2"].append((position_enemy_ships["three2"][0] + 50, position_enemy_ships["three2"][1]))
                                kill_position_ships["three2"].append((position_enemy_ships["three2"][0] + 100, position_enemy_ships["three2"][1]))
                            elif rotation_enemy_ships["three2"] == 0:
                                kill_position_ships["three2"].append(position_enemy_ships["three2"])
                                kill_position_ships["three2"].append((position_enemy_ships["three2"][0], position_enemy_ships["three2"][1] + 50))
                                kill_position_ships["three2"].append((position_enemy_ships["three2"][0], position_enemy_ships["three2"][1] + 100))


                            if rotation_enemy_ships["two1"]:
                                kill_position_ships["two1"].append(position_enemy_ships["two1"])
                                kill_position_ships["two1"].append((position_enemy_ships["two1"][0] + 50, position_enemy_ships["two1"][1]))
                            elif rotation_enemy_ships["two1"] == 0:
                                kill_position_ships["two1"].append(position_enemy_ships["two1"])
                                kill_position_ships["two1"].append((position_enemy_ships["two1"][0], position_enemy_ships["two1"][1] + 50))

                            if rotation_enemy_ships["two2"]:
                                kill_position_ships["two2"].append(position_enemy_ships["two2"])
                                kill_position_ships["two2"].append((position_enemy_ships["two2"][0] + 50, position_enemy_ships["two2"][1]))
                            elif rotation_enemy_ships["two2"] == 0:
                                kill_position_ships["two2"].append(position_enemy_ships["two2"])
                                kill_position_ships["two2"].append((position_enemy_ships["two2"][0], position_enemy_ships["two2"][1] + 50))


                            if rotation_enemy_ships["two3"]:
                                kill_position_ships["two3"].append(position_enemy_ships["two3"])
                                kill_position_ships["two3"].append((position_enemy_ships["two3"][0] + 50, position_enemy_ships["two3"][1]))
                            elif rotation_enemy_ships["two3"] == 0:
                                kill_position_ships["two3"].append(position_enemy_ships["two3"])
                                kill_position_ships["two3"].append((position_enemy_ships["two3"][0], position_enemy_ships["two3"][1] + 50))




                            kill_position_ships["one1"].append(position_enemy_ships["one1"])

                            kill_position_ships["one2"].append(position_enemy_ships["one2"])

                            kill_position_ships["one3"].append(position_enemy_ships["one3"])

                            kill_position_ships["one4"].append(position_enemy_ships["one4"])


                        
                        if user == "server":

                            path_to_json = os.path.abspath(__file__ + "/../data_s.json")

                        elif user == "client":
                            
                            path_to_json = os.path.abspath(__file__ + "/../data_c.json")

                        with open(path_to_json, 'r') as f:
                            data_turn = json.load(f)

                        if data_turn['turn']:
                            if attack_3x3:
                                column_3x3, row_3x3 = field_enemy.attack_3x3(enemy_matrix, screen.game_window, event.pos)
                                attack_3x3 = False
                                client_socket.send(f'attack_3x3/{(column_3x3, row_3x3)}'.encode())
                                
                            elif aimed_strike:
                                hit = field_enemy.aimed_strike(enemy_matrix, screen.game_window, event.pos)
                                client_socket.send(f'aimed_strike/{hit.split('%')[-1]}'.encode())
                                list_strikes.append(hit)
                                if len(list_strikes) > 4:
                                    for i in list_strikes:
                                        if 'circle' in i:
                                            screen.game_window.blit(field_enemy.circle, ast.literal_eval(i.split('%')[-1]))
                                        elif 'cross' in i:
                                            screen.game_window.blit(field_enemy.cross, ast.literal_eval(i.split('%')[-1]))

                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["four"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            if len(kill_position_ships["four"]) == 1:
                                                kill_position_ships["four"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["four"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass

                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["three1"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            if len(kill_position_ships["three1"]) == 1:
                                                kill_position_ships["three1"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["three1"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass

                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["three2"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            if len(kill_position_ships["three2"]) == 1:
                                                kill_position_ships["three2"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["three2"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass



                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two1"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            if len(kill_position_ships["two1"]) == 1:
                                                kill_position_ships["two1"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["two1"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass
                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two2"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            if len(kill_position_ships["two2"]) == 1:
                                                kill_position_ships["two2"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["two2"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass
                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two3"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            if len(kill_position_ships["two3"]) == 1:
                                                kill_position_ships["two3"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["two3"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass



                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one1"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                            
                                            kill_position_ships["one1"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(one_cell_ship1.ship_surf, one_cell_ship1.ship_rect)

                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one2"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                      
                                            kill_position_ships["one2"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(one_cell_ship2.ship_surf, one_cell_ship2.ship_rect)

                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one3"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                   
                                            kill_position_ships["one3"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(one_cell_ship3.ship_surf, one_cell_ship3.ship_rect)
                                            
                                        if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one4"]:
                                            pygame.mixer.Sound.play(expload_sound)
                                          
                                            
                                            kill_position_ships["one4"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(one_cell_ship4.ship_surf, one_cell_ship4.ship_rect)
                                            


                                        print(kill_position_ships)
                                        print((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))


                                        if kill_position_ships["four"] == []:
                                            kill_position_ships["four"].append("pass")
                                            coins += 25                         
                                            screen.game_window.blit(four_cells_ship.ship_surf, four_cells_ship.ship_rect)
                                            print(position_enemy_ships["four"])
                                            field_enemy.fill_after_destroy(enemy_matrix, 4, position_enemy_ships["four"], rotation_enemy_ships["four"], screen.game_window)



                                        if kill_position_ships["three1"] == []:
                                            kill_position_ships["three1"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(three_cells_ship1.ship_surf, three_cells_ship1.ship_rect)
                                            field_enemy.fill_after_destroy(enemy_matrix, 3, position_enemy_ships["three1"], rotation_enemy_ships["three1"], screen.game_window)

                                        if kill_position_ships["three2"] == []:
                                            kill_position_ships["three2"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(three_cells_ship2.ship_surf, three_cells_ship2.ship_rect)
                                            field_enemy.fill_after_destroy(enemy_matrix, 3, position_enemy_ships["three2"], rotation_enemy_ships["three2"], screen.game_window)





                                        if kill_position_ships["two1"] == []:
                                            kill_position_ships["two1"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(two_cells_ship1.ship_surf, two_cells_ship1.ship_rect)
                                            field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two1"], rotation_enemy_ships["two1"], screen.game_window)
                                            
                                            
                                        if kill_position_ships["two2"] == []:
                                            kill_position_ships["two2"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(two_cells_ship2.ship_surf, two_cells_ship2.ship_rect)
                                            field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two2"], rotation_enemy_ships["two2"], screen.game_window)

                                        if kill_position_ships["two3"] == []:
                                            kill_position_ships["two3"].append("pass")
                                            coins += 25
                                            screen.game_window.blit(two_cells_ship3.ship_surf, two_cells_ship3.ship_rect)
                                            field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two3"], rotation_enemy_ships["two3"], screen.game_window)

                                        
                                    aimed_strike = False
                                    list_strikes = []
                            
                            elif button_3x3_rect != None and button_3x3_rect.collidepoint(event.pos) and coins >= 100:
                                attack_3x3 = True

                                coins -= 100
                            
                            elif button_aimed_strike_rect.collidepoint(event.pos) and coins >= 200:
                                aimed_strike = True

                                coins -= 200

                            elif wait:
                                if war_plane_image != None:
                                    if war_plane_rect.collidepoint(event.pos) and coins >= 150:
                                        

                                        all_random_coordinates = []
                                        


                                        while len(all_random_coordinates) != 5:
                                            print("hello")

                                            random_row = random.randint(0, 9)
                                            random_column = random.randint(0, 9)

                                            print(random_row)
                                            print(random_column)                                

                                            if [random_column, random_row] in all_random_coordinates:
                                                pass
                                            else:
                                                all_random_coordinates.append([random_column, random_row])
                                                field_enemy.click(enemy_matrix, screen.game_window, column = random_column, row = random_row)
                                                client_socket.send(f'/{[random_column, random_row]}'.encode())
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["four"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["three1"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                    if len(kill_position_ships["three1"]) == 1:
                                                        kill_position_ships["three1"].pop()
                                                    coins += 15
                                                    try:
                                                        kill_position_ships["three1"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                                    except:
                                                        pass

                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["three2"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                    if len(kill_position_ships["three2"]) == 1:
                                                        kill_position_ships["three2"].pop()
                                                    coins += 15
                                                    try:
                                                        kill_position_ships["three2"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                                    except:
                                                        pass



                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two1"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                    if len(kill_position_ships["two1"]) == 1:
                                                        kill_position_ships["two1"].pop()
                                                    coins += 15
                                                    try:
                                                        kill_position_ships["two1"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                                    except:
                                                        pass
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two2"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                    if len(kill_position_ships["two2"]) == 1:
                                                        kill_position_ships["two2"].pop()
                                                    coins += 15
                                                    try:
                                                        kill_position_ships["two2"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                                    except:
                                                        pass
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two3"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                    if len(kill_position_ships["two3"]) == 1:
                                                        kill_position_ships["two3"].pop()
                                                    coins += 15
                                                    try:
                                                        kill_position_ships["two3"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                                    except:
                                                        pass



                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one1"]:
                                                    pygame.mixer.Sound.play(expload_sound)

                                                    kill_position_ships["one1"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(one_cell_ship1.ship_surf, one_cell_ship1.ship_rect)
                                                    print('shbjbvfhjjxvbbfgvdjbhjzz fygugzfyd guzgudguzgfduguzgfgyyyugz')
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one2"]:
                                                    pygame.mixer.Sound.play(expload_sound)

                                                    kill_position_ships["one2"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(one_cell_ship2.ship_surf, one_cell_ship2.ship_rect)
                                                    print('shbjbvfhjjxvbbfgvdjbhjzz fygugzfyd guzgudguzgfduguzgfgyyyugz')
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one3"]:
                                                    pygame.mixer.Sound.play(expload_sound)

                                                    kill_position_ships["one3"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(one_cell_ship3.ship_surf, one_cell_ship3.ship_rect)
                                                    print('shbjbvfhjjxvbbfgvdjbhjzz fygugzfyd guzgudguzgfduguzgfgyyyugz')
                                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one4"]:
                                                    pygame.mixer.Sound.play(expload_sound)
                                                    
                                                    print('shbjbvfhjjxvbbfgvdjbhjzz fygugzfyd guzgudguzgfduguzgfgyyyugz')
                                                    kill_position_ships["one4"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(one_cell_ship4.ship_surf, one_cell_ship4.ship_rect)
                                                    


                                                print(kill_position_ships)
                                                print((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))


                                                if kill_position_ships["four"] == []:
                                                    kill_position_ships["four"].append("pass")
                                                    coins += 25                         
                                                    screen.game_window.blit(four_cells_ship.ship_surf, four_cells_ship.ship_rect)
                                                    print(position_enemy_ships["four"])
                                                    field_enemy.fill_after_destroy(enemy_matrix, 4, position_enemy_ships["four"], rotation_enemy_ships["four"], screen.game_window)



                                                if kill_position_ships["three1"] == []:
                                                    kill_position_ships["three1"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(three_cells_ship1.ship_surf, three_cells_ship1.ship_rect)
                                                    field_enemy.fill_after_destroy(enemy_matrix, 3, position_enemy_ships["three1"], rotation_enemy_ships["three1"], screen.game_window)

                                                if kill_position_ships["three2"] == []:
                                                    kill_position_ships["three2"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(three_cells_ship2.ship_surf, three_cells_ship2.ship_rect)
                                                    field_enemy.fill_after_destroy(enemy_matrix, 3, position_enemy_ships["three2"], rotation_enemy_ships["three2"], screen.game_window)





                                                if kill_position_ships["two1"] == []:
                                                    kill_position_ships["two1"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(two_cells_ship1.ship_surf, two_cells_ship1.ship_rect)
                                                    field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two1"], rotation_enemy_ships["two1"], screen.game_window)
                                                    
                                                    
                                                if kill_position_ships["two2"] == []:
                                                    kill_position_ships["two2"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(two_cells_ship2.ship_surf, two_cells_ship2.ship_rect)
                                                    field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two2"], rotation_enemy_ships["two2"], screen.game_window)

                                                if kill_position_ships["two3"] == []:
                                                    kill_position_ships["two3"].append("pass")
                                                    coins += 25
                                                    screen.game_window.blit(two_cells_ship3.ship_surf, two_cells_ship3.ship_rect)
                                                    field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two3"], rotation_enemy_ships["two3"], screen.game_window)
                                            if len(kill_position_ships["four"]) == 1:
                                                kill_position_ships["four"].pop()
                                            coins += 15
                                            try:
                                                kill_position_ships["four"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                            except:
                                                pass




                                        coins -= 150

                                        client_socket.send('turn'.encode())
                                        data_turn['turn'] = False
                                        with open(path_to_json, 'w') as f:
                                            json.dump(data_turn, f, indent = 4)
                                            
                                        print(all_random_coordinates)
                                wait = False
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
                                
                                clicked_cell = [field_enemy.get_clicked_cell(event.pos)[0], field_enemy.get_clicked_cell(event.pos)[1]]

                                matrix_shots[clicked_cell[0]][clicked_cell[1]] = 2
                                print(enemy_matrix[clicked_cell[0]][clicked_cell[1] + 1])
                                print(clicked_cell)

                                # ship.ship_surf, four_cells_ship.ship_rect)
                                
                                    




                                
                                
                                
                                
                                
                                


                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["four"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    if len(kill_position_ships["four"]) == 1:
                                        kill_position_ships["four"].pop()
                                    coins += 15
                                    try:
                                        kill_position_ships["four"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                    except:
                                        pass

                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["three1"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    if len(kill_position_ships["three1"]) == 1:
                                        kill_position_ships["three1"].pop()
                                    coins += 15
                                    try:
                                        kill_position_ships["three1"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                    except:
                                        pass

                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["three2"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    if len(kill_position_ships["three2"]) == 1:
                                        kill_position_ships["three2"].pop()
                                    coins += 15
                                    try:
                                        kill_position_ships["three2"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                    except:
                                        pass



                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two1"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    if len(kill_position_ships["two1"]) == 1:
                                        kill_position_ships["two1"].pop()
                                    coins += 15
                                    try:
                                        kill_position_ships["two1"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                    except:
                                        pass
                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two2"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    if len(kill_position_ships["two2"]) == 1:
                                        kill_position_ships["two2"].pop()
                                    coins += 15
                                    try:
                                        kill_position_ships["two2"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                    except:
                                        pass
                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["two3"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    if len(kill_position_ships["two3"]) == 1:
                                        kill_position_ships["two3"].pop()
                                    coins += 15
                                    try:
                                        kill_position_ships["two3"].remove((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))
                                    except:
                                        pass



                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one1"]:
                                    pygame.mixer.Sound.play(expload_sound)

                                    kill_position_ships["one1"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(one_cell_ship1.ship_surf, one_cell_ship1.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 1, position_enemy_ships["one1"], rotation_enemy_ships["one1"], screen.game_window)
                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one2"]:
                                    pygame.mixer.Sound.play(expload_sound)

                                    kill_position_ships["one2"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(one_cell_ship2.ship_surf, one_cell_ship2.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 1, position_enemy_ships["one2"], rotation_enemy_ships["one2"], screen.game_window)
                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one3"]:
                                    pygame.mixer.Sound.play(expload_sound)

                                    kill_position_ships["one3"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(one_cell_ship3.ship_surf, one_cell_ship3.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 1, position_enemy_ships["one3"], rotation_enemy_ships["one3"], screen.game_window)
                                if (clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150) in kill_position_ships["one4"]:
                                    pygame.mixer.Sound.play(expload_sound)
                                    
                                    print('fygugzfyd guzgudguzgfduguzgfgyyyugz')
                                    kill_position_ships["one4"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(one_cell_ship4.ship_surf, one_cell_ship4.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 1, position_enemy_ships["one4"], rotation_enemy_ships["one4"], screen.game_window)
                                    


                                print(kill_position_ships)
                                print((clicked_cell[0] * 50 + 550, clicked_cell[1] * 50 + 150))


                                if kill_position_ships["four"] == []:
                                    kill_position_ships["four"].append("pass")
                                    coins += 25                         
                                    screen.game_window.blit(four_cells_ship.ship_surf, four_cells_ship.ship_rect)
                                    print(position_enemy_ships["four"])
                                    field_enemy.fill_after_destroy(enemy_matrix, 4, position_enemy_ships["four"], rotation_enemy_ships["four"], screen.game_window)



                                if kill_position_ships["three1"] == []:
                                    kill_position_ships["three1"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(three_cells_ship1.ship_surf, three_cells_ship1.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 3, position_enemy_ships["three1"], rotation_enemy_ships["three1"], screen.game_window)

                                if kill_position_ships["three2"] == []:
                                    kill_position_ships["three2"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(three_cells_ship2.ship_surf, three_cells_ship2.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 3, position_enemy_ships["three2"], rotation_enemy_ships["three2"], screen.game_window)





                                if kill_position_ships["two1"] == []:
                                    kill_position_ships["two1"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(two_cells_ship1.ship_surf, two_cells_ship1.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two1"], rotation_enemy_ships["two1"], screen.game_window)
                                    
                                    
                                if kill_position_ships["two2"] == []:
                                    kill_position_ships["two2"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(two_cells_ship2.ship_surf, two_cells_ship2.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two2"], rotation_enemy_ships["two2"], screen.game_window)

                                if kill_position_ships["two3"] == []:
                                    kill_position_ships["two3"].append("pass")
                                    coins += 25
                                    screen.game_window.blit(two_cells_ship3.ship_surf, two_cells_ship3.ship_rect)
                                    field_enemy.fill_after_destroy(enemy_matrix, 2, position_enemy_ships["two3"], rotation_enemy_ships["two3"], screen.game_window)


                            
                                if not hit:
                                    print('idk')
                                    client_socket.send('turn'.encode())
                                    data_turn['turn'] = False

                                    
                                with open(path_to_json, 'w') as f:
                                    json.dump(data_turn, f, indent = 4)
                                wait = True
                





                        
                        else:
                            pass
                    except Exception as e:
                        wait = True
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


    
        animation_coin_count += 1

        pygame.display.update()
        pygame.display.flip()
        # pygame.time.delay(160)
        clock.tick(FPS)

        