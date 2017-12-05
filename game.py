import sys
import pygame
import random
import ship

class Controller:
    def __init__(self, width=800, height=800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        """Load the sprites that we need"""
        self.ship = ship.Ship()
        #self.sprites = pygame.sprite.Group((self.ship,))

    def mainLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill((5, 5, 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP or event.key == pygame.K_w):
                        self.ship.forward()
                    elif(event.key == pygame.K_q):
                        self.ship.turn(1)
                    elif(event.key == pygame.K_e):
                        self.ship.turn(-1)
                    elif(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        self.ship.left()
                    elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        self.ship.right()
                    elif(event.key == pygame.K_SPACE):
                        self.ship.accelerate((0,-1))
            
            #redraw the entire screen
            self.screen.blit(self.background, (0, 0))
            #self.sprites.draw(self.screen)
            pygame.display.flip()

#alternate gameloop
#gameLoop = True
#while gameLoop:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #gameLoop = False
        #if event.type == pygame.KEYDOWN:
            #if(event.key == pygame.K_UP or event.key == pygame.K_w):
                #self.ship.forward()
            #elif(event.key == pygame.K_q):
                #self.ship.turn(1)
            #elif(event.key == pygame.K_e):
                #self.ship.turn(-1)
            #elif(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                #self.ship.left()
            #elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                #self.ship.right()
            #elif(event.key == pygame.K_SPACE):
                #self.ship.accelerate((0,-1))
    #pygame.display.flip()
    #clock.tick(50)

def main():
    main_window = Controller()
    main_window.mainLoop()
main()
