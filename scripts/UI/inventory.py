import pygame
from pygame import sprite
from support import canvas_path, get_item_by_id
from UI.button import Button


class Inventory(pygame.sprite.Sprite):
    def __init__(self, path, pos, size, close_event):
        super().__init__()

        self.storage = {
        'items': [
            '1 1   ',
            '      ',
            '      ',
            '      '],
        'quantities': [
            '3 7   ',
            '      ',
            '      ',
            '      ']
        }

        # Render Properties
        self.image = pygame.image.load(canvas_path + path).convert_alpha()
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
        self.close_event = close_event
        bt = Button(icon_path, hover_path, animation_path, (pos[0] + self.image.get_width() - 32, pos[1] + 20), (48, 48), close_event)
        self.exit_button.add(bt)

        # Slots
        self.slots = pygame.sprite.Group()

        # Put the items in the inventory
        self.setup_storage(pos)


    def setup_storage(self, pos):

        for y, row in enumerate(self.storage['items']):
            for x, cell in enumerate(row):
                temp = (pos[0] + x * 100 + 35, pos[1] + y * 76 + 70)

                if cell == " ":
                    cell = -1
                else:
                    print(self.storage['quantities'][y][x])

                slot = Slot(temp, int(cell))
                self.slots.add(slot)


    def update(self, win):

        self.slots.draw(win)
        self.slots.update(win)

        win.blit(self.title, (self.rect.width - 245, self.rect.height - 195))

        self.exit_button.update()
        self.exit_button.draw(win)


class Slot(pygame.sprite.Sprite):
    def __init__(self, pos, item_id):
        super().__init__()

        # Slot Render Properties
        self.image = pygame.image.load(canvas_path + "inventory/slot.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)

        # Item Render Properties
        try:
            item = Item(self.rect.center, item_id)
            self.item = sprite.GroupSingle()
            self.item.add(item)
        except:
            pass
    
    def update(self, win):

        try:
            self.item.draw(win)
        except:
            pass
        
    # Missing Hover Event


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, id):
        super().__init__()

        self.image = pygame.image.load(get_item_by_id(id)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect(center = pos) # self.rect.center