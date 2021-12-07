import pygame, os
from random import randint, random
from object import Animated_Object
from utilis import import_folder_with_scale, animate_loop
from object import Animated_Object, Collectable_Object

# This class manage all the environment in the map
class Environment():
    def __init__(self, win):

        # Properties
        self.win = win
        self.max_clouds = 10

        # All Objects
        self.clouds = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.trees = pygame.sprite.Group()
        self.bushes = pygame.sprite.Group()

        # Create Clouds
        for _ in range(self.max_clouds):
            cloud = Cloud((randint(0, win.get_width()), randint(0,100)), win.get_width())
            self.clouds.add(cloud)


    def add_sunflower(self, image, pos):
        obj = Collectable_Object(image, pos, "assets/sprites/environment/sunflower", 1)
        self.collectibles.add(obj)

    def add_rocks(self, image, pos):
        obj = Collectable_Object(image, pos, "", 2)
        self.collectibles.add(obj)

    def add_tree(self, image, pos):
        self.trees.add(Animated_Object(image, pos, "assets/sprites/environment/tree"))

    def add_bush(self, image, pos):
        self.bushes.add(Animated_Object(image, pos, "assets/sprites/environment/bush"))


    def update(self, x_shift):
        
        self.clouds.update()
        self.clouds.draw(self.win)
        
        self.trees.update(x_shift)
        self.trees.draw(self.win)
        self.collectibles.update(x_shift)
        self.collectibles.draw(self.win)

    def late_update(self, x_shift):
        self.bushes.update(x_shift)
        self.bushes.draw(self.win)


# Cloud Object
class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, screen_width):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(os.path.join("assets/sprites/environment/cloud.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (147, 69))
        self.rect = self.image.get_rect(topleft = pos)

        # Pysics Properties
        self.speed = (random() + randint(1, 3))
        self.max_width = screen_width

    # Cloud Movement
    def update(self):
        
        if self.rect.x <= self.max_width:
            self.rect.x += self.speed
        else:
            self.respawn()

    # Restart the position of the cloud
    def respawn(self):
        self.rect.x = -100
        self.rect.y = randint(0, 100)

