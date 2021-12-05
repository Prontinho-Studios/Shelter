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
        self.inventory = pygame.sprite.Group()
        pos = pygame.math.Vector2(win.get_width()/2-64*5, win.get_height()/2-32*5-30)
        inventory = Inventory("inventory/inventory_background.png", pos, (128*5, 75*5))
        self.inventory.add(inventory)


    def setup_buttons(self):
        w = self.win.get_width()

        # Inventory Button
        icon_path = "inventory/icon_animation/inventory-button-1.png"
        hover_path = "inventory/inventory-button-hover.png"
        animation_path = 'inventory/icon_animation/'
        bt = Button(icon_path, hover_path, animation_path, (w - 150, 20), (48, 48))
        self.buttons.add(bt)

        # Options Button
        icon_path = "settings_icon.png"
        hover_path = "settings_icon_hover.png"
        bt = Button(icon_path, hover_path, "", (w - 80, 20), (48, 48))
        self.buttons.add(bt)


    def run(self):
        self.buttons.update()
        self.buttons.draw(self.win)

        self.inventory.draw(self.win)
        self.inventory.update(self.win)

        self.stats_bar.draw(self.win)
