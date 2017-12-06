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
                
                #FONTS USED IN THE GUI
                self.titleFont = pygame.font.SysFont("monospace", 45)
                self.mainFont = pygame.font.SysFont("monospace",22)


                self.win = False
                self.died = False
                self.menu = True
                self.enableInput = True

                self.planet = planet.Planet(.1,20)
                self.sprites = pygame.sprite.Group()
                self.terrain = pygame.Rect(0,0,0,0)
        def mainLoop(self):	
                while True:
                    while self.menu:
                        title = self.titleFont.render("LUNAR LANDER", 1, (255,255,0))
                        choiceEasy = self.mainFont.render("1. Easy",1,(255,255,0))
                        choiceMid = self.mainFont.render("2. Hard",1,(255,255,0))
                        choiceHard = self.mainFont.render("3. Impossible",1,(255,255,0))
                        choiceQuit = self.mainFont.render("4. Quit",1,(255,255,0))
                        self.window.blit(title, (250, 150))
                        self.window.blit(choiceEasy, (250, 250))
                        self.window.blit(choiceMid, (250, 300))
                        self.window.blit(choiceHard, (250, 350))
                        self.window.blit(choiceQuit, (250, 400))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
            
                            if event.type == pygame.KEYUP:
                                if(event.key == pygame.K_1):
                                    self.ship = ship.Ship(500)
                                    self.sprites.add(self.ship)
                                    self.menu = False
                                elif(event.key == pygame.K_2):
                                    self.ship = ship.Ship(200)
                                    self.sprites.add(self.ship)
                                    self.menu = False
                                elif(event.key == pygame.K_3):
                                    self.ship = ship.Ship(100)
                                    self.sprites.add(self.ship)
                                    self.menu = False
                                elif(event.key == pygame.K_4):
                                    pygame.quit()
                        pygame.display.flip()
                        self.window.blit(self.background, (0, 0))
                    if(self.win):
                        self.enableInput = False
                        winLab = self.titleFont.render("YOU WIN!", 1, (255,255,0))
                        resetLab = self.mainFont.render("Press Space to return to menu", 1,(255,255,0))
                        self.window.blit(resetLab, (350, 100))
                        self.window.blit(winLab, (300, 50))
                    if(self.died):
                        self.enableInput = False
                        deadLab = self.titleFont.render("YOU CRASHED!", 1, (255,255,0))
                        resetLab = self.mainFont.render("Press Space to return to menu", 1,(255,255,0))
                        self.window.blit(resetLab, (350, 100))
                        self.window.blit(deadLab, (350, 50))
                    pygame.key.set_repeat(1,50)
                    self.background.fill((0,0,0))

                    fuelLab = self.mainFont.render("Fuel: " + str(self.ship.fuel), 1, (255,255,0))
                    velocityLab = self.mainFont.render("Velocity: " + str(self.ship.velMagnitude()), 1, (255,255,0))
                    self.window.blit(fuelLab, (0, 50))
                    self.window.blit(velocityLab, (0,100))
		    #APPLIES A CONSTANT GRAVITY
                    self.ship.accelerate((0,self.planet.gravity),"world")

                    ##DRAWS THE TERRAIN
                    self.terrain = pygame.draw.lines(self.window, (250,250,250), False, self.planet.nodes)
                    self.platform = pygame.draw.line(self.window, (250,0,0),self.planet.plat[0], self.planet.plat[1], 10)
                    pygame.draw.line(self.window, (250,0,0), self.planet.plat[0], self.planet.platStand)

                    ##HANDLE POSITION UPDATES HERE
                    self.ship.position = (self.ship.position[0] + self.ship.velocity[0], self.ship.position[1]+self.ship.velocity[1])
                    self.ship.rect.x, self.ship.rect.y = self.ship.position
                    self.sprites.draw(self.window)

                    ##CHECK FOR COLLISION
                    if(self.ship.rect.colliderect(self.terrain)):
                        self.died = True
                        self.ship.velocity = (0,0)
                    if(self.ship.rect.colliderect(self.platform)):
                        if(self.ship.velMagnitude() > .7):
                            self.died = True
                            self.ship.velocity = (0,0)
                        elif(not self.died):
                            self.win = True
                            self.ship.velocity = (0,0)


                    #WAY TO HANDLE SEVERAL INPUTS HELD DOWN
                    keys = pygame.key.get_pressed()  #checking pressed keys
                    if(self.enableInput):
                        if keys[pygame.K_w]:
                            self.ship.fuel -= 1
                            x=(self.ship.rotation / 90)
                            if(self.ship.rotation != 0):
                                 y=0
                            else:
                                 y=-1
                            if(self.ship.fuel > 0):
                                 self.ship.accelerate((x,y),"world")
                                 curSprite = random.choice(["yellow","red"])
                            else:
                                 curSprite = "normal"
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
                    
                        if event.type == pygame.KEYUP:
                            if(event.key == pygame.K_SPACE):
                                if(self.died or self.win):
                                    self.menu = True 
                                    self.sprites.remove(self.ship)
                                    self.enableInput = True
                                    self.died = False
                                    self.win = False        
                    pygame.display.flip()
                    self.window.blit(self.background, (0, 0))
                    self.clock.tick(50)
                pygame.quit()
def main():
    main_window = Controller()
    main_window.mainLoop()
main()


