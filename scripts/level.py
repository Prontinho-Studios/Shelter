import pygame
from player import Player
from tiles import Tile
from pytmx import load_pygame
from environment import Environment

class Level():
    def __init__(self, win):
        super().__init__()

        # Level Data
        self.tmxdata = load_pygame("assets/levels/level_data/level_0.tmx")
        self.win = win 

        # Create Map
        self.setup_level()

        # Create an environment
        self.environment = Environment(win)

        # Create player
        self.players = pygame.sprite.GroupSingle()
        player = Player((100, win.get_height()-150))
        self.players.add(player)

    # Draw all the map tiles
    def setup_level(self):
        self.tiles = pygame.sprite.Group()

        for layer in self.tmxdata:
            for tile in layer.tiles():
                x = tile[0] * 32
                y = tile[1] * 32
                if tile[2] != None:
                    tile = Tile((x, y), tile[2])
                    self.tiles.add(tile)

    def horizontal_movement_collision(self):
        player = self.players.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.players.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    # Run the Level
    def run(self):

        self.tiles.draw(self.win)
        self.environment.update()

        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.players.update()
        self.players.draw(self.win)
        