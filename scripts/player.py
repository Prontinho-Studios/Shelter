import pygame
from scripts.utilis import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Player image and animations
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        # Player Movement
        self.speed = 4
        self.direction = pygame.math.Vector2(0,0)



    def import_character_assets(self):
        character_path = 'assets/sprites/player/'
        self.animations = {'idle':[],'pick':[],'run':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def animate(self):
        animation = self.animations[self.status]

		# loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        flip = False
        if self.direction.x < 0:
            flip = True

        self.image = pygame.transform.flip(pygame.transform.scale(image, (67.5, 82.5)), flip, False)
        

    def get_input(self):
        keys = pygame.key.get_pressed()

        # Get the direction
        if keys[pygame.K_a]: # Left
            self.direction.x = -1
        if keys[pygame.K_d]: # Right
            self.direction.x = 1
        if keys[pygame.K_w]: # Up
            self.direction.y = -1
        if keys[pygame.K_s]: # Down
            self.direction.y = 1

        # Remove speed if its not moving
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direction.x = 0
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.direction.y = 0


    def get_status(self):

        if (self.direction.x < 0):
            self.status = 'run'
        elif (self.direction.x > 0):
            self.status = 'run'   
        elif (self.direction.y > 0):
            self.status = 'pick'   
        elif (self.direction.y < 0): 
            self.status = 'pick'  
        else:
            self.status = 'idle'  


    def update(self):
        self.get_input()
        self.get_status()
        self.animate()


