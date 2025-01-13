import pygame
import os

class TwoCellsShip():
    def __init__(self, matrix_x, x, y, rotation=True, screen = None, killed = False):
        # Загрузка изображения

        if killed:
            self.ship_surf = pygame.image.load(os.path.abspath(__file__ + "/../../images/two_cells_ship_killed.png"))
        else:
            self.ship_surf = pygame.image.load(os.path.abspath(__file__ + "/../../images/2_cells_ship.png"))

        # Масштабирование
        self.ship_surf = pygame.transform.scale(self.ship_surf, (95, 45))

        # Поворот изображения, если rotation == False
        if not rotation:  # Если rotation = False
            self.ship_surf = pygame.transform.rotate(self.ship_surf, 90)  # Повернуть вниз

        # Получение прямоугольника
        self.ship_rect = self.ship_surf.get_rect()

        # Установка начальных координат
        self.ship_rect.topleft = (x, y)

        # Сохранение других параметров
        self.matrix_x = matrix_x
        self.rotation = rotation
        
        self.x = x
        self.y = y

    def rotate_down(self):

        self.ship_surf = pygame.transform.rotate(self.ship_surf, 90)  # Поворот на 90 градусов
        self.ship_rect = self.ship_surf.get_rect(topleft=self.ship_rect.topleft)  # Обновляем прямоугольник

    def get_clicked(self, mouse_position):

        return self.ship_rect.collidepoint(mouse_position)