import pygame
from support import canvas_path

class StatsBar(pygame.sprite.Sprite):
    def __init__(self, path, pos, size):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(canvas_path + path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)

        # Values
        self._health = 100
        self._energy = 100

        # Bars
        bar_pos = (pos[0] + 57, pos[1] + 15)
        self.health_bar = HealthBar(bar_pos)
        bar_pos = (pos[0] + 57, pos[1] + 33)
        self.energy_bar = EnergyBar(bar_pos)


    def update(self, win):
        win.blit(self.health_bar.image, self.health_bar.rect)
        win.blit(self.energy_bar.image, self.energy_bar.rect)


    # Get Lives Value Function
    @property
    def energy(self):
        return self._energy


    # Set Lives Value
    @energy.setter
    def energy(self, value):
        self._energy = value
        self.energy_bar.image = pygame.transform.scale(self.energy_bar.image, (value * self.energy_bar.image.get_width() / 100, self.energy_bar.image.get_height()))


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(canvas_path + "health_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.rect = self.image.get_rect(topleft = pos)


class EnergyBar(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(canvas_path + "energy_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.rect = self.image.get_rect(topleft = pos)
