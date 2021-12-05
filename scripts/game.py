import pygame, sys
from level import Level
from UI.canvas import Canvas

pygame.init()

class Game:

    # Game Setup
    def __init__(self, w, h):

        # Initial Settings
        self.width = w
        self.height = h
        self.win = pygame.display.set_mode((w, h)) #, pygame.FULLSCREEN
        self.clock = pygame.time.Clock()

        # Game Objects
        self.level = Level(self.win)
        self.canvas = Canvas(self.win)


    # Game Loop
    def run(self):
        
        # Game Loop
        while True:
            
            # Initial Loop stuff
            self.next_frame()
            self.events()

            # Update
            self.level.run()
            self.canvas.run()

    # Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Next frame procedures
    def next_frame(self):
        pygame.display.update()
        self.clock.tick(60)
        self.win.fill((32, 199, 212))

