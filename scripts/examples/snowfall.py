
import pygame
import random
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN  = [0,255,0]
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Programming World of GFG")
 
 
def getNewSpeed():
    return random.randrange(5, 8)


snowFall = []
for i in range(100):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowFall.append({"x": x, "y": y, "speed": getNewSpeed()})
 
clock = pygame.time.Clock()
done = False
while not done:
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    screen.fill(BLACK)
    for i in range(len(snowFall)):
        pygame.draw.circle(screen, WHITE, [snowFall[i]["x"], snowFall[i]["y"]], 2)
 
        snowFall[i]["y"] += snowFall[i]["speed"]
        snowFall[i]["x"] -= snowFall[i]["speed"]/3
        if snowFall[i]["y"] > 400:
            y = random.randrange(-50, -10)
            snowFall[i]["y"] = y
        
            x = random.randrange(50, 500)
            snowFall[i]["x"] = x

            snowFall[i]["speed"] = getNewSpeed()
 
    pygame.display.flip()
    clock.tick(20)
pygame.quit()