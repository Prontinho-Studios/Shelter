import pygame, os
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(os.path.join("assets/sprites/player/rock-projectile.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        # Pysics Properties
        self.initial_pos = (self.rect.x, self.rect.y)
        destination = pygame.mouse.get_pos()
        self.time = 0

        # The distance between point A and B
        self.power = math.sqrt((destination[1] - pos[1])**2 + (destination[0] - pos[0])**2)/8
        self.angle = self.findAngle(destination)


    def update(self, x_shift):   #

        # Background Movement
        self.rect.x += x_shift

        self.time += 0.15
        po = self.ballPath(self.initial_pos[0], self.initial_pos[1], self.power, self.angle, self.time)
        self.rect.x = po[0]
        self.rect.y = po[1]


    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)


        return (newx, newy)
        

    def findAngle(self, pos):
        sX = self.rect.x
        sY = self.rect.y
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle

        return angle

