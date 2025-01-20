import pygame
import os

class FourCellsShip():
    def __init__(self, matrix_x, x, y, rotation=True, screen = None, area = None, killed = False):
        

        if killed:
            self.ship_surf = pygame.image.load(os.path.abspath(__file__ + "/../../images/four_cells_ship_killed.png"))
        else:
            self.ship_surf = pygame.image.load(os.path.abspath(__file__ + "/../../images/4_cells_ship.png"))

       
        self.ship_surf = pygame.transform.scale(self.ship_surf, (195, 45))

        
        if not rotation:  
            self.ship_surf = pygame.transform.rotate(self.ship_surf, 90) 
        # Получение прямоугольника
        self.ship_rect = self.ship_surf.get_rect()

        # Установка начальных координат
        self.ship_rect.topleft = (x, y)

        # Сохранение других параметров
        self.matrix_x = matrix_x
        self.rotation = rotation
        self.screen = screen
        self.area = area
  
        self.x = x
        self.y = y
        
        
    def rotate_down(self):

        self.ship_surf = pygame.transform.rotate(self.ship_surf, 90)
        
        

    def get_clicked(self, mouse_position):

        return self.ship_rect.collidepoint(mouse_position)