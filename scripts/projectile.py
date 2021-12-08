import pygame, os
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, destination):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(os.path.join("assets/sprites/player/rock-projectile.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        # Pysics Properties
        self.gravity = 0.05
        self.distance = 0
        self.destination = destination
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4
        self.previousLocation = pygame.math.Vector2(pos)


    def update(self, x_shift):   #

        # Background Movement
        self.rect.x += x_shift

        if not self.distance:

            radians = math.atan2(self.destination.y - self.previousLocation.y, self.destination.x - self.previousLocation.y)
            distance = math.hypot(self.destination.x - self.previousLocation.x, self.destination.y - self.previousLocation.y) / self.speed
            self.distance = int(distance)

            self.direction.x = math.cos(radians) * self.speed
            self.direction.y = math.sin(radians) * self.speed

            self.previousLocation = self.rect.x, self.rect.y

        if self.distance:
            self.rect.x += self.direction.x
            self.rect.y += self.direction.y

        self.apply_gravity()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def detect_collision(self):
        pass