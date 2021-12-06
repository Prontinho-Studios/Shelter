import pygame, os
from utilis import import_folder_with_scale, canvas_path

class Button(pygame.sprite.Sprite):
    def __init__(self, path_icon, path_hover, path_animation, pos, size, on_click_event):
        super().__init__()

        # Render Properties
        self.path_icon = canvas_path + path_icon
        self.path_hover = canvas_path + path_hover
        self.size = size
        self.image = pygame.image.load(os.path.join(self.path_icon)).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)

        # On Click Function
        self.on_click_event = on_click_event

        # Animation Properties
        if path_animation != "":
            self.animation_speed = 0.075
            self.frame_index = 0

            # Import Animation
            self.animation = import_folder_with_scale(canvas_path + path_animation, size)

        # States
        self.hover_changed = False
        self.hover = False
        self.clicked = False


    def update(self):
        self.hover_event()
        self.click_event()


    def hover_event(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
            self.hover_changed = True
        else:
            self.hover = False
            
        if self.hover:
            self.image = pygame.image.load(self.path_hover)
            self.image = pygame.transform.scale(self.image, self.size)

        # This code increse game performance by not loading the image every single frame
        if self.hover_changed and not self.hover:
            self.image = pygame.image.load(self.path_icon)
            self.image = pygame.transform.scale(self.image, self.size)
            self.hover_changed = False


    def click_event(self):

        if (pygame.mouse.get_pressed()[0] and self.hover):
            self.clicked = True

        if (self.clicked):
            try:
                self.animate()
            except:
                pass

            # Handle Event
            self.clicked = False
            self.on_click_event()


    # Correct this bug here <------------------------ Event not happening because of self.clicked = False
    def animate(self):
        
		# Loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
            self.clicked = False

        self.image = self.animation[int(self.frame_index)]

