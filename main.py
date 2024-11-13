import pygame
import threading
import server_settings

from modules import *

pygame.init()


screen = Screen(
    size_x = 1200,
    size_y = 800,
)
field = Field(dest = (350, 150))

pygame.display.set_caption(title= 'Sea battle')

button_server = Button(screen.game_window, position = (250, 350), color = 'gray')
button_client = Button(screen.game_window, position = (750, 350), color = 'gray')
play_button = Button(screen.game_window, position = (1000, 700), color = 'gray')



button_server.Font(text = 'start server')
button_client.Font(text = 'join server')
play_button.Font(text = 'play', font_size = 60)


screen.game_window.blit(button_server.text, dest= (275, 380))   
screen.game_window.blit(button_client.text, dest= (785, 380))
screen.game_window.blit(play_button.text, dest= (1030, 720))
scene = 'menu'

dark_blue = (0, 0, 139)

flag_message = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # server_settings.start_server(start_server= False)


                if scene == 'menu':

                    if button_server.button_clicked(event.pos):
                        threading.Thread(target= server_settings.start_server).start()
                        screen.game_window.fill(color = "dark blue")
                        
                    
                        

                    elif button_client.button_clicked(event.pos):
                        threading.Thread(server_settings.connect_client(ip = "192.168.0.106", port = 8000)).start()
                        server_settings.client.client_socket.send("connected".encode())
                        flag_message = True
                        screen.game_window.fill(color = "dark blue")
                        

                    elif play_button.button_clicked(event.pos):
                        scene = 'game'


        
            if server_settings.server.message == "connected":
                screen.game_window.blit(field.field_surf, dest = (350, 150))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_cell = field.get_clicked_cell(event.pos)
                    if clicked_cell:
                        server_settings.start_server(start_server= False)
                        # print(clicked_cell)

            
            if flag_message:
                screen.game_window.blit(field.field_surf, dest = (350, 150))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_cell = field.get_clicked_cell(event.pos)

                    if clicked_cell:
                        
                        server_settings.connect_client(server_settings= False, ip = "192.168.0.106", port = 8000)

            
        pygame.display.flip()
        