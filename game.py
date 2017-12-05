import pygame
import random
import ship

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Lunar Lander")
clock = pygame.time.Clock()

player1 = ship.Ship()
gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP or event.key == pygame.K_w):
                self.ship.forward()
            elif(event.key == pygame.K_LEFT):
                self.ship.turn(1)
            elif(event.key == pygame.K_RIGHT):
                self.ship.turn(-1)
            elif(event.key == pygame.K_a):
                self.ship.left()
            elif(event.key == pygame.K_d):
                self.ship.right()
            elif(event.key == pygame.K_SPACE):
                self.ship.accelerate((0,-1))
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
