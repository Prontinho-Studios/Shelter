import pygame
from support import canvas_path

class AmmoCounter(pygame.sprite.Sprite):
    def __init__(self, path, pos, size):
        super().__init__()

        self.image = pygame.image.load(canvas_path + path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)

        # Quantity Text
        self._quantity = 0
        self.font_quantity = pygame.font.Font("assets/fonts/prstart.ttf", 13)
        self.quantity_text = self.font_quantity.render(str(self.quantity), True, 'black')


    def update(self, win):
        pos = (self.rect.x + 27 - self.quantity_text.get_width(), self.rect.y + 60 - self.quantity_text.get_height())
        win.blit(self.quantity_text, pos) # (self.rect.width - 245, self.rect.height - 195)
        

    # Get Lives Value Function
    @property
    def quantity(self):
        return self._quantity


    # Set Lives Value
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

        # Update the Text Element
        self.quantity_text = self.font_quantity.render(str(self._quantity), True, 'black')