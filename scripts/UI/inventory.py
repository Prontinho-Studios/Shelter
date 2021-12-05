import pygame
from utilis import canvas_path
from UI.button import Button


class Inventory(pygame.sprite.Sprite):
    def __init__(self, path, pos, size):
        super().__init__()

        self.image = pygame.image.load(canvas_path + path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)
        
        # Text 
        font_title = pygame.font.Font("assets/fonts/prstart.ttf", 24)
        self.title = font_title.render("Inventory", True, 'black')

        # Exit Button
        self.exit_button = pygame.sprite.GroupSingle()
        icon_path = "exit_button.png"
        hover_path = "exit_button_hover.png"
        animation_path = ""
        bt = Button(icon_path, hover_path, animation_path, (pos[0] + self.image.get_width() - 32, pos[1] + 20), (48, 48))
        self.exit_button.add(bt)

        # Slots
        self.slots = pygame.sprite.Group()
        slot_sprite = "inventory/slot.png"

        # Place all Slots
        for y in range(4):
            for x in range(6):
                temp = (pos[0] + x * 100 + 35, pos[1] + y * 76 + 70)
                slot = Slot(slot_sprite, temp)
                self.slots.add(slot)


    def update(self, win):
        self.slots.draw(win)

        win.blit(self.title, (self.rect.width - 245, self.rect.height - 195))

        self.exit_button.update()
        self.exit_button.draw(win)


class Slot(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()

        self.image = pygame.image.load(canvas_path + path)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        