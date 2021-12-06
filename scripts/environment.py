import pygame, os
from random import randint, random
from utilis import import_folder_with_scale

# This class manage all the environment in the map
class Environment():
    def __init__(self, win):

        # Properties
        self.win = win
        self.max_clouds = 10
        self.clouds = pygame.sprite.Group()
        self.max_sunflowers = 10
        self.sunflowers = pygame.sprite.GroupSingle()

        # Create Clouds
        for _ in range(self.max_clouds):
            cloud = Cloud((randint(0, win.get_width()), randint(0,100)), win.get_width())
            self.clouds.add(cloud)

        # Create Sunflowers
        sunflower = Sunflower((600, win.get_height()-290))
        self.sunflowers.add(sunflower)


    def update(self, x_shift):
        
        self.clouds.update()
        self.clouds.draw(self.win)

        self.sunflowers.update(x_shift)
        self.sunflowers.draw(self.win)


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


# Sunflower Object
class Sunflower(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(os.path.join("assets/sprites/environment/sunflower/sunflower1.png"))
        self.image = pygame.transform.scale(self.image, (26, 38))
        self.rect = self.image.get_rect(topleft = pos)

        # Animation Properties
        self.animation_speed = 0.075
        self.frame_index = 0
        self.import_animation()

    # 
    def update(self, x_shift):   
        
        self.rect.x += x_shift
        
        self.animate()


    def import_animation(self):
        path = 'assets/sprites/environment/sunflower/'
        self.animation = import_folder_with_scale(path, (26, 38))


    def animate(self):
        
		# Loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index = 0

        self.image = self.animation[int(self.frame_index)]
