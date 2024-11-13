import pygame

class Button():
    def __init__(self, surface, position = (0, 0), color = "gray", border_size = 0, size = (150, 75)):
        
        self.button_surf = pygame.Rect(position[0], position[1], size[0], size[1])
        pygame.draw.rect(surface, color = color, rect = self.button_surf, width = border_size)
        
    def Font(self, color = "black", text = "Hello", font_size = 24):
        
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(f"{text}", True, color)
        
    def button_clicked(self, mouse_position):

        return self.button_surf.collidepoint(mouse_position)
