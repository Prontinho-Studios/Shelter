import pygame, os
from utilis import import_folder, get_all_folder_animations

enemy_path = 'assets/sprites/enemies/'

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos, win):
        super().__init__()

        # Render Properties
        self.win = win
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        # Animation Properties
        self.import_character_assets("slime")
        self.status = "idle"
        self.animation_speed = 0.075
        self.frame_index = 0

        # Enemy UI
        self.health_bar = pygame.image.load(os.path.join("assets/sprites/ui/health_bar.png")).convert_alpha()


    def update(self, x_shift):   
        self.rect.x += x_shift
        self.animate()

        self.win.blit(self.health_bar, self.rect)


    def import_character_assets(self, name):
        character_path = enemy_path + name + "/"
        self.animations = get_all_folder_animations(character_path, name)

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        