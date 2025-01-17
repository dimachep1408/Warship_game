import pygame
import os


class Button():
    def __init__(self, surface, position = (0, 0), color = "gray", border_size = 0, size = (150, 75)):
        
        self.button_rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.button_surf = surface
        self.position = position
        pygame.draw.rect(surface, color = color, rect = self.button_rect, width = border_size, border_radius= 5)

        self.x = position[0]
        self.y = position[1]
    def Font(self, color = "white", text = "Hello", font_size = 24):
        
        self.font = pygame.font.Font(os.path.abspath(__file__ + "/../../fonts/Oswald-Medium.ttf"), font_size)
        self.text = self.font.render(f"{text}", True, color)
        
    def button_clicked(self, mouse_position):

        return self.button_rect.collidepoint(mouse_position)
