import pygame
from utilis import canvas_path

class StatsBar(pygame.sprite.Sprite):
    def __init__(self, path, pos, size):
        super().__init__()

        self.image = pygame.image.load(canvas_path + path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)
