import pygame, os
from .button import Button

class Field():
    def __init__(self, width = 500, height = 500, color = "light gray", dest = (0, 0)):
        self.dest = dest
        self.field_surf = pygame.Surface((width, height))
        self.field_surf.fill(color)
        self.draw_grid()

    def draw_grid(self):
        for i in range(10):
            for j in range(10):
                cell = Button(
                    self.field_surf,
                    color = "black",
                    position = (i * 50, j * 50),
                    size = (50, 50),
                    border_size = 1,
                )

    def get_clicked_cell(self, mouse_pos):
        x, y = mouse_pos
        i = (x - self.dest[0]) // 50
        j = (y - self.dest[1]) // 50
        if 0 <= i < 10 and 0 <= j < 10:
            return (i, j)
        return None
    
    def get_clicked_cell_position(self, mouse_pos):
        x, y = mouse_pos
        i = (x - self.dest[0]) // 50
        j = (y - self.dest[1]) // 50
        if 0 <= i < 10 and 0 <= j < 10:
            pixel_x = self.dest[0] + i * 50
            pixel_y = self.dest[1] + j * 50
            return (pixel_x, pixel_y)
        return None

    def matrix_fill(self, matrix, cells_count, ship_coordinates, rotation_ship):
        if rotation_ship == 1:
            for i in range(cells_count):
                try:
                    x, y = ship_coordinates
                    x = (x - self.dest[0]) // 50 + 1
                    y = (y - self.dest[1]) // 50 + 1
                    matrix[y][x + i] += 2
                except:
                    pass
                
            for i in range(cells_count):
                try:
                    matrix[y + 1][x + i] += 3
                    matrix[y - 1][x + i] += 3
                except:
                    pass
            for i in range(3):
                try:
                    i -= 1
                    matrix[y + i][x + cells_count] += 3
                    matrix[y + i][x - 1] += 3
                except:
                    pass
        elif rotation_ship == 0:
            for i in range(cells_count):
                try:
                    x, y = ship_coordinates
                    x = (x - self.dest[0]) // 50 + 1
                    y = (y - self.dest[1]) // 50 + 1
                    matrix[y + i][x] += 2
                except:
                    pass
            for i in range(cells_count):
                try:
                    matrix[y + i][x + 1] += 3
                    matrix[y + i][x - 1] += 3
                except:
                    pass
            for i in range(3):
                try:
                    i -= 1
                    matrix[y + cells_count][x + i] += 3
                    matrix[y - 1][x + i] += 3
                except:
                    pass
            
    def click(self, list_ships, screen, mouse_pos = None, column = None, row = None):
        hit = False
        if mouse_pos != None:
            column, row = self.get_clicked_cell(mouse_pos)
        if list_ships[row][column] % 3 == 0:
            self.circle = os.path.abspath(__file__ + "/../../images/circle.png")
            self.circle = pygame.transform.scale(pygame.image.load(self.circle), (50, 50)) 
            screen.blit(self.circle, ((column + self.dest[0] // 50) * 50, (row + self.dest[1] // 50) * 50))
        elif list_ships[row][column] == 2:
            hit = True
            self.cross = os.path.abspath(__file__ + "/../../images/cross.png")
            self.cross = pygame.transform.scale(pygame.image.load(self.cross), (50, 50))
            screen.blit(self.cross, ((column + self.dest[0] // 50) * 50, (row + self.dest[1] // 50) * 50))
        return hit
