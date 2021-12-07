import pygame
from utilis import import_folder, animate_loop

class Object(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()

        # Render Properties
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):   
        self.rect.x += x_shift


class Animated_Object(Object):
    def __init__(self, image, pos, animation_path):
        super().__init__(image, pos)

        # Animation Properties
        self.animation_speed = 0.075
        self.frame_index = 0
        self.animation = import_folder(animation_path)

    def update(self, x_shift):   
        super().update(x_shift)
        try:
            self.animate()
        except:
            pass

    def animate(self):
        self.image, self.frame_index = animate_loop(self.animation, self.frame_index, self.animation_speed)


class Collectable_Object(Animated_Object):
    def __init__(self, image, pos, animation_path, id):
        super().__init__(image, pos, animation_path)

        # Identification of the object
        print(id)
        self.id = id
