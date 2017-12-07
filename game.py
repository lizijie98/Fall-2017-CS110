##STEVEN LANDER BY HAYDEN, JACK, AND DILLON
##PROPOSAL DOCUMENT LINK https://docs.google.com/a/binghamton.edu/document/d/13P1opyWf36rsluvURYljHppWx61UWksmms042lXPTgI/edit?usp=sharing
import pygame
import random
import ship
import planet
import math
import fuelpod
import asteroid
class Controller:
        def __init__(self, width=800, height=800):
                #SETS UP PYGAME WINDOW AND SETS STARTING VARIABLES TO BE USED LATER ON		

		#GENERAL PYGAME SETUP
                pygame.init()
                pygame.display.set_caption("Steven Lander")
                self.width = width
                self.height = height
                self.window = pygame.display.set_mode((width,height))
                self.background = pygame.Surface(self.window.get_size()).convert()
                self.clock = pygame.time.Clock()
                
                #FONTS USED IN THE GUI
                self.titleFont = pygame.font.SysFont("monospace", 45)
                self.mainFont = pygame.font.SysFont("monospace",22)

		#HIGHSCORE INFORMATION
                scoreFile = open("score.txt", "r")
                self.highscore = float(scoreFile.readline())
                scoreFile.close()

		#VARIABLES FOR GAMESTATE AND LOGIC
                self.win = False
                self.died = False
                self.menu = True
                self.enableInput = True
                self.score = 0
                self.difficulty = 0 #used for score calculation
                self.spawnRate = 5 #used to determine the spawn rate of asteroids and fuelpods

                #SPRITES AND OBJECTS
                self.planet = planet.Planet(.1,20)
                self.asteroids = []#lists to keep track of objects on the screen
                self.fuelpods = []
                self.sprites = pygame.sprite.Group()
                self.terrain = pygame.Rect(0,0,0,0)

        def mainLoop(self):	
                while True:
                    ##THIS SECTION IS USED TO DRAW THE MAIN MENU##
                    tColor = (255,255,0)
                    while self.menu:
                        title = self.titleFont.render("STEVEN LANDER", 1, tColor)
                        names = self.mainFont.render("By: Hayden, Jack, and Dillon", 1,tColor)
                        choiceEasy = self.mainFont.render("1. Easy",1,tColor)
                        choiceMid = self.mainFont.render("2. Hard",1,tColor)
                        choiceHard = self.mainFont.render("3. Impossible",1,tColor)
                        choiceQuit = self.mainFont.render("4. Quit",1,tColor)
                        self.window.blit(title, (250, 150))
                        self.window.blit(names, (250, 200))
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
                                    self.spawnRate = 2
                                    self.difficulty = 1
                                    self.menu = False
                                elif(event.key == pygame.K_2):
                                    self.ship = ship.Ship(200)
                                    self.sprites.add(self.ship)
                                    self.spawnRate = 5
                                    self.difficulty = 5 
                                    self.menu = False
                                elif(event.key == pygame.K_3):
                                    self.ship = ship.Ship(100)
                                    self.sprites.add(self.ship)
                                    self.spawnRate = 10
                                    self.difficulty = 15
                                    self.menu = False
                                elif(event.key == pygame.K_4):
                                    pygame.quit()
                        pygame.display.flip()
                        self.window.blit(self.background, (0, 0))
                    ##################################################


                    ##HANDLES DRAWING LABELS ON THE SCREEN##
                    if(self.win and not self.died):
                        self.enableInput = False
                        winLab = self.titleFont.render("YOU WIN!", 1, tColor)
                        resetLab = self.mainFont.render("Press Space to return to menu", 1,tColor)
                        self.window.blit(resetLab, (350, 100))
                        self.window.blit(winLab, (300, 50))
                    if(self.died and not self.win):
                        self.enableInput = False
                        deadLab = self.titleFont.render("YOU CRASHED!", 1, tColor)
                        resetLab = self.mainFont.render("Press Space to return to menu", 1,tColor)
                        self.window.blit(resetLab, (350, 100))
                        self.window.blit(deadLab, (350, 50))
                    pygame.key.set_repeat(1,50)
                    self.background.fill((0,0,0))
                    
                    if(self.ship.velMagnitude() > 0):
                        self.score = round(self.ship.fuel / self.ship.velMagnitude() * self.difficulty,2)
                    scoreFile = open("score.txt", "r")
                    self.highscore = float(scoreFile.readline())
                    scoreFile.close()
                    fuelLab = self.mainFont.render("Fuel: " + str(self.ship.fuel), 1, tColor)
                    velocityLab = self.mainFont.render("Velocity: " + str(round(self.ship.velMagnitude(),2)), 1, tColor)
                    scoreLab = self.mainFont.render("Score: " + str(self.score), 1,tColor)
                    hscoreLab = self.mainFont.render("Highscore: " + str(self.highscore), 1,tColor)
                    self.window.blit(fuelLab, (0, 50))
                    self.window.blit(velocityLab, (0,100))
                    self.window.blit(scoreLab, (0,150))
                    self.window.blit(hscoreLab, (0,200))
                    #########################


                    #ASTEROID SPAWNING
                    if(random.randrange(1,500) <= self.spawnRate):
                        ast = asteroid.Asteroid((770, random.randrange(0,400)))
                        self.asteroids.append(ast)
                        self.sprites.add(ast)
                    #FUEL SPAWNING
                    if(random.randrange(1,2000) <= self.spawnRate):
                        fuelObj = fuelpod.FuelPod((770, random.randrange(0,400)))
                        self.fuelpods.append(fuelObj)
                        self.sprites.add(fuelObj)


		    #APPLIES A CONSTANT GRAVITY
                    self.ship.accelerate((0,self.planet.gravity),"world")

                    ##DRAWS THE TERRAIN
                    self.terrain = pygame.draw.lines(self.window, (255,255,255), False, self.planet.nodes)
                    self.platform = pygame.draw.line(self.window, (255,0,0),self.planet.plat[0], self.planet.plat[1], 10)
                    pygame.draw.line(self.window, (255,0,0), self.planet.platStand[0], self.planet.platStand[1])
                    #########################


                    ##HANDLE POSITION UPDATES HERE##
                    self.sprites.update()

                    #Checks to make sure the ship is still on the screen
                    if(self.ship.position[0] > self.width - self.ship.rect.width):
                        self.ship.position = (self.width - self.ship.rect.width, self.ship.position[1])
                        self.ship.velocity = (0, self.ship.velocity[1])
                    if(self.ship.position[0] < self.ship.rect.width):
                        self.ship.position = (self.ship.rect.width, self.ship.position[1])
                        self.ship.velocity = (0, self.ship.velocity[1])
                    if(self.ship.position[1] < 0):
                        self.ship.position = (self.ship.position[0], 0)
                        self.ship.velocity = (self.ship.velocity[0], 0)
                    self.sprites.draw(self.window)
                    #########################

                    ##CHECK FOR COLLISIONS##
                    for i in self.asteroids:
                        if(self.ship.rect.colliderect(i) and not self.win):
                            self.died = True
                            self.sprites.remove(self.ship)
                    for i in self.fuelpods:
                        if(self.ship.rect.colliderect(i)):
                            self.ship.fuel += 50
                            self.sprites.remove(i)
                            self.fuelpods.remove(i)
                            del i
                    if(self.ship.rect.colliderect(self.terrain) and not self.win):
                        self.died = True
                        self.ship.velocity = (0,0)
                    if(self.ship.rect.colliderect(self.platform)):
                        if(self.ship.velMagnitude() > .7  and not self.win):
                            self.died = True
                        if(self.ship.rotation != 0  and not self.win):
                            self.died = True
                        elif(not self.died and not self.win):
                            self.win = True
                            self.checkHighscore()   
                        self.ship.velocity = (0,0)
                    #########################


                    #WAY TO HANDLE SEVERAL INPUTS HELD DOWN
                    keys = pygame.key.get_pressed()  #checking pressed keys
                    if(self.enableInput): #Makes sure the ship hasn't crashed or landed
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
                        if keys[pygame.K_d]:
                            self.ship.rotation = 90
                            #self.ship.image = customRotate(self.ship.image,-1)
                            curSprite += "90"
                        elif keys[pygame.K_a]:
                            #self.ship.turn(-1) 
                            self.ship.rotation = -90
                            #self.ship.image = customRotate(self.ship.image,1)
                            curSprite += "-90"
                        else:
                            self.ship.rotation = 0
                        #changes the ship sprite to the desired throttle state and rotation
                        self.ship.image = pygame.image.load(curSprite + ".png").convert_alpha()
                    #########################


                    ##NON GAMEPLAY INPUT##
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    
                        if event.type == pygame.KEYUP:
                            if(event.key == pygame.K_SPACE):
                                if(self.died or self.win):
                                    self.menu = True 
                                    self.sprites.remove(self.ship)
                                    self.planet = planet.Planet(.1,20)
                                    self.enableInput = True
                                    self.died = False
                                    self.win = False
                                    for i in self.asteroids:
                                        self.sprites.remove(i) 
                                    for i in self.fuelpods:
                                        self.sprites.remove(i)  
                                    self.fuelpods = []  
                                    self.asteroids = []   
                    #########################

                    pygame.display.flip()
                    self.window.blit(self.background, (0, 0))
                    self.clock.tick(50)
                pygame.quit()

        def checkHighscore(self):
            #Checks a saved score file to see if the player broke the highscore
            #Rewrites the file with the new score if they did.
            scoreFile = open("score.txt", "r")
            if(self.score > float(scoreFile.readline())):
                scoreFile.close()
                scoreFile = open("score.txt", "w")
                scoreFile.write(str(self.score))
            scoreFile.close()
def main():
    main_window = Controller()
    main_window.mainLoop()
main()


