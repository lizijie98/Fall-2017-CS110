import pygame
from math import *

pygame.init()

#colors
black = (0,0,0)
white = (255, 255, 255)
red = (255, 25, 25)
gray = (127,127,127)

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lunar Lander")
clock = pygame.time.Clock()
fps = 30

def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if y2<=(y1+h1):
        if x2<=x1 and ((x2+w2)>(x1+w1)):
            return True
    else:
        return False

class ship:
    def __init__(self):
        self.x = 400
        self.y = 50
        self.width = 25
        self.height = 25
        self.rotation = 0
        self.velocity = (0,0)
        self.MainPower = 4.3584
        self.auxPower = 0.2748
        self.mainFuel = 311
        self.auxFuel = 290
    def render(self, collision):
        if (collision == True):
            pygame.draw.rect(window, red, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))
    def forward(self):
        self.mainFuel -= 1
        self.velocity = ((self.velocity[0] + (self.MainPower * cos(self.rotation))),(self.velocity[1] + (self.MainPower * sin(self.rotation))))
    def left(self):
        self.auxFuel -= 1
        self.velocity = ((self.velocity[0] - self.auxPower), self.velocity[1])
    def right(self):
        self.auxFuel -= 1
        self.velocity = ((self.velocity[0] + self.auxPower), self.velocity[1])
    #def turn(self, angle):
        #pygame.transform.rotate(self, angle)
        #self.angle += angle

class landZone:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def render(self):
        pygame.draw.line(window,gray,(self.x,self.y),((self.x+self.width),self.y), self.height)

Lander = ship()
Zone = landZone(300,500, 100, 1)

moveX, moveY = 0,0

gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_w):
                Lander.forward()
            #elif(event.key == pygame.K_LEFT):
                #Lander.turn(-1)
            #elif(event.key == pygame.K_RIGHT):
                #Lander.turn(1)
            elif(event.key == pygame.K_a):
                Lander.left()
            elif(event.key == pygame.K_d):
                Lander.right()
        if (event.type == pygame.KEYUP):
            if(event.key == pygame.K_w):
                pass
            #elif(event.key == pygame.K_LEFT):
                #pass
            #elif(event.key == pygame.K_RIGHT):
                #pass
            elif(event.key == pygame.K_a):
                pass
            elif(event.key == pygame.K_d):
                pass
            elif(event.type == pygame.QUIT):
                gameLoop = False

    window.fill(white)
    Lander.velocity = (Lander.velocity[0], (Lander.velocity[1]+(1.622/30)))
    Lander.x += Lander.velocity[0]
    Lander.y += Lander.velocity[1]
    collisions = detectCollisions(Lander.x, Lander.y, Lander.width, Lander.height, Zone.x, Zone.y, Zone.width, Zone.height)
    Lander.render(collisions)
    Zone.render()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
