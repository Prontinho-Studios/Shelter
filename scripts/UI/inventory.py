import pygame
from pygame import sprite
from support import canvas_path, get_item_by_id
from UI.button import Button


class Inventory(pygame.sprite.Sprite):
    def __init__(self, path, pos, size, close_event):
        super().__init__()

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
        self.slots = []

        # Put the items in the inventory
        self.setup_storage(pos, (6, 4))


    # Create the Slots and put the items there
    def setup_storage(self, pos, size):

        for y in range(size[1]):
            for x in range(size[0]):
                temp = (pos[0] + x * 100 + 70, pos[1] + y * 76 + 105)
                slot = Slot(temp, None)
                self.slots.append(slot)


    def add(self, id, amount):
        pass
        
        found = False

        # Find the first compatible element
        for slot in self.slots:
            if slot.item != None and slot.item.id == id:
                found = True
                slot.item.quantity += 1

        # Otherwise use an empty slot
        if not found:
            for slot in self.slots:
                if slot.item == None:
                    found = True
                    print(amount)
                    item = Item(slot.rect.center, id, amount)
                    slot.item = item
                    break
        
    def refresh_inventory(self):
        pass


    def update(self, win):

        for slot in self.slots:
            win.blit(slot.image, slot.rect)
            slot.update(win)

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
            self.item = item
        except:
            pass
    
    def update(self, win):

        try:
            win.blit(self.item.image, self.item.rect)
            self.item.update(win)
        except:
            pass
        
    # Missing Hover Event


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, id, amount):
        super().__init__()

        # Render Properties
        self.id = id
        self.image = pygame.image.load(get_item_by_id(id)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect(center = pos) # self.rect.center
        self._quantity = amount

        # Quantity Text
        self.font_quantity = pygame.font.Font("assets/fonts/prstart.ttf", 11)
        self.quantity_text = self.font_quantity.render(str(self.quantity), True, 'black')


    def update(self, win):
        pos = (self.rect.x + 40 - self.quantity_text.get_width(), self.rect.y + 42 - self.quantity_text.get_height())
        win.blit(self.quantity_text, pos) # (self.rect.width - 245, self.rect.height - 195)
        

    # Get Lives Value Function
    @property
    def quantity(self):
        return self._quantity


    # Set Lives Value
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self.quantity_text = self.font_quantity.render(str(self.quantity), True, 'black')

