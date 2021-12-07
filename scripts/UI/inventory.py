import pygame
from pygame import sprite
from support import canvas_path, get_item_by_id
from UI.button import Button


class Inventory(pygame.sprite.Sprite):
    def __init__(self, path, pos, size, close_event):
        super().__init__()

        # Inventory Storage
        self.storage = {
        'items': [
            '1     ',
            '      ',
            '      ',
            '      '],
        'quantities': [
            '1     ',
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


    # Create the Slots and put the items there
    def setup_storage(self, pos):

        for y, row in enumerate(self.storage['items']):
            for x, cell in enumerate(row):
                temp = (pos[0] + x * 100 + 70, pos[1] + y * 76 + 105)

                if cell == " ":
                    cell = -1
                    slot = Slot(temp, None)
                else:
                    quantity = self.storage['quantities'][y][x]
                    item = Item(temp, int(cell), quantity)
                    slot = Slot(temp, item)

                self.slots.add(slot)


    def add(self, id, amount):

        found = False

        # Find the first compatible element
        for y, row in enumerate(self.storage['items']):
            for x, cell in enumerate(row):
                if cell == str(id):
                    found = True
                    quantity = self.storage['quantities'][y][x]
                    value = int(quantity) + amount
                    self.storage['quantities'][y][x].replace(quantity, str(value))
                    # break

        # Otherwise use an empty slot
        if not found:
            for y, row in enumerate(self.storage['items']):
                for x, cell in enumerate(row):
                    if cell == " ":
                        self.storage['items'][y][x] = str(id)
                        self.storage['quantities'][y][x] = str(amount)
        
        
    def refresh_inventory(self):
        pass


    def update(self, win):

        self.slots.draw(win)
        self.slots.update(win)

        win.blit(self.title, (self.rect.width - 245, self.rect.height - 195))

        self.exit_button.update()
        self.exit_button.draw(win)


class Slot(pygame.sprite.Sprite):
    def __init__(self, pos, item):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(canvas_path + "inventory/slot.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center = pos)

        # Item
        try:
            self.item = sprite.GroupSingle(item)
        except:
            pass
    
    def update(self, win):

        try:
            self.item.draw(win)
            self.item.update(win)
        except:
            pass
        
    # Missing Hover Event


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, id, quantity):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load(get_item_by_id(id)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect(center = pos) # self.rect.center
        self.quantity = quantity

        # Quantity Text
        font_quantity = pygame.font.Font("assets/fonts/prstart.ttf", 11)
        self.quantity_text = font_quantity.render(str(self.quantity), True, 'black')


    def update(self, win):
        pos = (self.rect.x + 40 - self.quantity_text.get_width(), self.rect.y + 42 - self.quantity_text.get_height())
        win.blit(self.quantity_text, pos) # (self.rect.width - 245, self.rect.height - 195)
        

