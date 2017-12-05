import pygame
import random
import ship
import planet
import math
class Controller:
        def __init__(self, width=800, height=800):
                pygame.init()
                pygame.display.set_caption("Lunar Lander")
                self.window = pygame.display.set_mode((width,height))
                self.background = pygame.Surface(self.window.get_size()).convert()
                self.clock = pygame.time.Clock()

                self.ship = ship.Ship((300,300))
                self.planet = planet.Planet(.1,20)
                self.sprites = pygame.sprite.Group()
                self.sprites.add(self.ship)
                self.terrain = pygame.Rect(0,0,0,0)
        def mainLoop(self):	
                while True:
                    pygame.key.set_repeat(1,50)
                    self.background.fill((0,0,0))

		    #APPLIES A CONSTANT GRAVITY
                    self.ship.accelerate((0,self.planet.gravity),"world")

                    ##DRAWS THE TERRAIN
                    self.terrain = pygame.draw.lines(self.window, (250,250,250), False, self.planet.nodes)
                    self.platform = pygame.draw.line(self.window, (250,0,0),self.planet.plat[0], self.planet.plat[1], 3)

                    ##HANDLE POSITION UPDATES HERE
                    self.ship.position = (self.ship.position[0] + self.ship.velocity[0], self.ship.position[1]+self.ship.velocity[1])
                    self.ship.rect.x, self.ship.rect.y = self.ship.position
                    self.sprites.draw(self.window)

                    ##CHECK FOR COLLISION
                    if(self.ship.rect.colliderect(self.terrain)):
                        if(self.ship.velMagnitude() > 1):
                            print("Died")
                        self.ship.velocity = (0,0)


                    #WAY TO HANDLE SEVERAL INPUTS HELD DOWN
                    keys = pygame.key.get_pressed()  #checking pressed keys
                    if keys[pygame.K_w]:
                        x=(self.ship.rotation / 90)
                        if(self.ship.rotation != 0):
                             y=0
                        else:
                             y=-1
                        self.ship.accelerate((x,y),"world")
                        curSprite = random.choice(["yellow","red"])
                    else:
                        curSprite = "normal"
                    if keys[pygame.K_e]:
                        self.ship.rotation = 90
                        #self.ship.image = customRotate(self.ship.image,-1)
                        curSprite += "90"
                    elif keys[pygame.K_q]:
                        #self.ship.turn(-1)
                        self.ship.rotation = -90
                        #self.ship.image = customRotate(self.ship.image,1)
                        curSprite += "-90"
                    else:
                        self.ship.rotation = 0
                        
                    self.ship.image = pygame.image.load(curSprite + ".png").convert()
                    #OLD INPUT ALGORITHM
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    
                    #    if event.type == pygame.KEYDOWN:
                    #        if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    #            self.ship.accelerate((0,-1),"local")
                    #        elif(event.key == pygame.K_q):
                    #            self.ship.turn(-5)
                    #            self.ship.image = pygame.transform.rotozoom(self.ship.image, 5, 1)
                    #        elif(event.key == pygame.K_e):
                    #            self.ship.turn(5)
                    #            self.ship.image = pygame.transform.rotozoom(self.ship.image, -5, 1)
                    pygame.display.flip()
                    self.window.blit(self.background, (0, 0))
                    self.clock.tick(50)
                pygame.quit()
def main():
    main_window = Controller()
    main_window.mainLoop()
main()


