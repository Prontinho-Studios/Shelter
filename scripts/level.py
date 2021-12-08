import pygame
from player import Player
from tiles import Tile
from pytmx import load_pygame
from environment import Environment

class Level():
    def __init__(self, win, player_ui_components):
        super().__init__()

        # Level Data
        self.tmxdata = load_pygame("assets/levels/level_data/level_0.tmx")
        self.win = win 
        
        # Background
        self.background = pygame.image.load("assets/sprites/environment/background.png").convert()
        
        # Create an environment
        self.environment = Environment(win)

        # Create Map
        self.world_shift = 0
        self.setup_level()

        # Create player
        self.players = pygame.sprite.GroupSingle()
        player = Player(win, (100, win.get_height()-150), player_ui_components)
        self.players.add(player)

    # Draw all the map tiles
    def setup_level(self):
        self.tiles = pygame.sprite.Group()
        self.background_tiles = pygame.sprite.Group()

        for layer in self.tmxdata:
            
            if layer.name == "decorations":
                for tile in layer.tiles():
                    x = tile[0] * 64
                    y = tile[1] * 64
                    if tile[2] != None:
                        self.environment.add_tree(tile[2], (x, y-50))
            elif layer.name == "foreground":
                for tile in layer.tiles():
                    x = tile[0] * 64
                    y = tile[1] * 64
                    if tile[2] != None:
                        self.environment.add_bush(tile[2], (x, y+26))
            elif layer.name == "sunflowers":
                for tile in layer.tiles():
                    x = tile[0] * 64
                    y = tile[1] * 64
                    if tile[2] != None:
                        self.environment.add_sunflower(tile[2], (x, y+27))
            elif layer.name == "rocks":
                for tile in layer.tiles():
                    x = tile[0] * 64
                    y = tile[1] * 64
                    if tile[2] != None:
                        self.environment.add_rocks(tile[2], (x, y+46))
            elif layer.name == "background":
                for tile in layer.tiles():
                    x = tile[0] * 64
                    y = tile[1] * 64
                    if tile[2] != None:
                        tile = Tile((x, y), tile[2])
                        self.background_tiles.add(tile)
            else:
                for tile in layer.tiles():
                    x = tile[0] * 64
                    y = tile[1] * 64
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

    def scroll_x(self):
        player = self.players.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        w = self.win.get_width()

        if player_x < w / 3 and direction_x < 0:
            self.world_shift = player.initial_speed
            player.speed = 0
        elif player_x > w - (w / 3) and direction_x > 0:
            self.world_shift = -player.initial_speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player.initial_speed

    # Run the Level
    def run(self):

        # Background
        self.win.blit(self.background, self.background.get_rect())

        # Pysics
        self.scroll_x()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        # Draw Tiles
        self.background_tiles.update(self.world_shift)
        self.background_tiles.draw(self.win)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.win)
        
        # Draw Environment Objects
        self.environment.update(self.world_shift)

        # Draw Player
        self.players.update(self.environment.collectibles, self.world_shift)
        self.players.draw(self.win)

        # Draw Foreground Environment Objects
        self.environment.late_update(self.world_shift)
        