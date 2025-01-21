import pygame
import os

class ThreeCellsShip():
    def __init__(self, matrix_x, x, y, rotation=True, killed = False):

        if killed:
            self.ship_surf = pygame.image.load(os.path.abspath(__file__ + "/../../images/three_cells_ship_killed.png"))
        else:
            self.ship_surf = pygame.image.load(os.path.abspath(__file__ + "/../../images/3_cells_ship.png"))


        self.ship_surf = pygame.transform.scale(self.ship_surf, (145, 45))


        if not rotation: 
            self.ship_surf = pygame.transform.rotate(self.ship_surf, 90) 

        self.ship_rect = self.ship_surf.get_rect()


        self.ship_rect.topleft = (x, y)


        self.matrix_x = matrix_x
        self.rotation = rotation

        self.x = x
        self.y = y

    def rotate_down(self):

        self.ship_surf = pygame.transform.rotate(self.ship_surf, 90)  
        self.ship_rect = self.ship_surf.get_rect(topleft=self.ship_rect.topleft) 

    def get_clicked(self, mouse_position):

        return self.ship_rect.collidepoint(mouse_position)