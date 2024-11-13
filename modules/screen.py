import pygame


class Screen():
    def __init__(self : pygame.display, size_x = 1200, size_y = 800, color = "dark blue"):
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.game_window = pygame.display.set_mode(size = (size_x, size_y))
        
        self.game_window.fill(self.color)
        
        