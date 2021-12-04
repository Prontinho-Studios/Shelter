import pygame, sys
from scripts.player import Player

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main():

    player = Player((100, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update()
        WIN.blit(player.image, player.rect)

        pygame.display.update()
        clock.tick(60)
        WIN.fill('black')


if __name__ == "__main__":
    main()