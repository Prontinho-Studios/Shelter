import pygame
from utilis import import_folder_with_scale, get_all_folder_animations
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, win, pos, player_ui_components):
        super().__init__()

        # Player image and animations
        self.win = win
        self.import_character_assets()
        self.frame_index = 0
        self.status = 'idle'
        self.animation_speed = 0.1
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        # Player Movement
        self.direction = pygame.math.Vector2(0,0)
        self.initial_speed = 4
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -16
        self.feet_collider = pygame.Rect(self.rect.x, self.rect.bottom, self.rect.width, self.rect.height * 5 / 100)

        # Player Status
        self.picking_item = False
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.descend = False
        
        # Player Combat
        self.aim = pygame.sprite.GroupSingle(Aim())
        self.projectiles = pygame.sprite.Group()
        self.aiming = False
        self.attacking = False

        # Player UI
        self.inventory = player_ui_components[0]
        self.stats_bar = player_ui_components[1]
        self.ammo_counter = player_ui_components[2]


    def import_character_assets(self):
        character_path = 'assets/sprites/player/'
        self.animations = get_all_folder_animations(character_path, "player")

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder_with_scale(full_path, (23*2.5, 32*2.5))


    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            if self.status == 'pick':
                self.picking_item = False
            if self.status == 'attack':
                self.attacking = False
                self.throw_projectile()

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        # Set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)


    def get_input(self, entities):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        # Get the direction
        if keys[pygame.K_a]: # Left
            self.direction.x = -1
            self.facing_right = False
        elif keys[pygame.K_d]: # Right
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = 0

        # Descend Platforms
        self.descend = keys[pygame.K_s]

        # Jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

        # Pick Item
        if keys[pygame.K_e] and self.on_ground:
            self.picking_item = True
            self.pick_item(entities)

        # Aim
        self.aiming = mouse[0]

        # Attack
        if self.aiming:
            self.attacking = True


    def get_status(self):

        if self.picking_item:
            self.status = 'pick'
        elif self.aiming:
            self.status = 'attack-idle'
        elif self.attacking:
            self.status = 'attack'
        else:
            if self.direction.y < 0:
                self.status = 'jump'
            elif self.direction.y > 1:
                self.status = 'fall'    # fall
            else:
                if self.direction.x != 0:
                    self.status = 'run'
                else:
                    self.status = 'idle'


    def throw_projectile(self):
        self.stats_bar.energy -= 10
        projectile = Projectile((self.rect.x, self.rect.y))
        self.projectiles.add(projectile)


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def jump(self):
        self.direction.y = self.jump_speed


    def pick_item(self, entities):

        for entity in entities:
            if self.rect.colliderect(entity.rect):

                entity.kill()
                
                # Rock
                if entity.id == 2:
                    self.ammo_counter.quantity += 1
                else:
                    self.inventory.add(1, 1)
                    

    def update(self, entities, x_shift):
        self.get_input(entities)
        self.get_status()
        self.animate()

        self.projectiles.draw(self.win)
        self.projectiles.update(x_shift)

        if self.aiming:
            self.aim.draw(self.win)
            self.aim.update()

        # Feet Collider Gizmos
        #pygame.draw.rect(self.win, 'red', self.feet_collider)


class Aim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Render Properties
        self.image = pygame.image.load("assets/sprites/ui/aim.png").convert_alpha()
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())

    def update(self):   
        self.rect.center = pygame.mouse.get_pos()
