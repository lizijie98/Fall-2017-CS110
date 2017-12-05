import pygame
import random
import ship
import planet
class Controller:
        def __init__(self, width=800, height=800):
                pygame.init()
                pygame.display.set_caption("Lunar Lander")
                self.window = pygame.display.set_mode((width,height))
                self.background = pygame.Surface(self.window.get_size()).convert()
                self.clock = pygame.time.Clock()

                self.ship = ship.Ship((300,300))
                self.planet = planet.Planet(10,20)
                self.sprites = pygame.sprite.Group()
                self.sprites.add(self.ship)
        def mainLoop(self):	
                while True:
                    pygame.key.set_repeat(1,50)
                    #print(self.ship.velocity)
                    self.background.fill((0,0,0))
                    #self.ship.accelerate((0,.1),"world")
                    pygame.draw.lines(self.window, (250,250,250), False, self.planet.nodes)
                    self.ship.position = (self.ship.position[0] + self.ship.velocity[0], self.ship.position[1]+self.ship.velocity[1])
                    self.ship.rect.x, self.ship.rect.y = self.ship.position
                    self.sprites.draw(self.window)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if(event.key == pygame.K_UP or event.key == pygame.K_w):
                                self.ship.accelerate((0,-1),"local")
                            elif(event.key == pygame.K_q):
                                self.ship.turn(-5)
                                self.ship.image = pygame.transform.rotozoom(self.ship.image, 5, 1)
                            elif(event.key == pygame.K_e):
                                self.ship.turn(5)
                                self.ship.image = pygame.transform.rotozoom(self.ship.image, -5, 1)
                            #elif(event.key == pygame.K_a):
                            #    self.ship.accelerate((-1,0))
                            #elif(event.key == pygame.K_d):
                            #    self.ship.accelerate((1,0))
                            #elif(event.key == pygame.K_SPACE):
                            #    self.ship.accelerate((0,-1))
                    pygame.display.flip()
                    self.window.blit(self.background, (0, 0))
                    #self.clock.tick(50)
                pygame.quit()
def main():
    main_window = Controller()
    main_window.mainLoop()
main()
