import pygame
from UI.button import Button
from UI.inventory import Inventory
from UI.statsBar import StatsBar

class Canvas():
    def __init__(self, win):
        super().__init__()
        self.win = win
        
        # Create Buttons
        self.buttons = pygame.sprite.Group()
        self.setup_buttons()

        # Create Stats Bar
        self.stats_bar = pygame.sprite.Group()
        stats_bar = StatsBar("stats_bar.png", (20, 20), (70*3, 20*3))
        self.stats_bar.add(stats_bar)

        # Create Inventory
        self.inventory_open = False
        pos = pygame.math.Vector2(win.get_width()/2-64*5, win.get_height()/2-32*5-30)
        inventory = Inventory("inventory/inventory_background.png", pos, (128*5, 75*5), self.close_inventory)
        self.inventory = inventory


    def setup_buttons(self):
        w = self.win.get_width()

        # Inventory Button
        icon_path = "inventory/icon_animation/inventory-button-1.png"
        hover_path = "inventory/inventory-button-hover.png"
        animation_path = "inventory/icon_animation/"
        on_click_event = self.open_inventory
        bt = Button(icon_path, hover_path, animation_path, (w - 150, 20), (48, 48), on_click_event)
        self.buttons.add(bt)

        # Options Button
        icon_path = "settings_icon.png"
        hover_path = "settings_icon_hover.png"
        on_click_event = ""
        bt = Button(icon_path, hover_path, "", (w - 80, 20), (48, 48), on_click_event)
        self.buttons.add(bt)


    def open_inventory(self):
        self.inventory_open = True


    def close_inventory(self):
        self.inventory_open = False


    def run(self):
        self.buttons.update()
        self.buttons.draw(self.win)

        if self.inventory_open:
            self.win.blit(self.inventory.image, self.inventory.rect)
            self.inventory.update(self.win)

        self.stats_bar.draw(self.win)
