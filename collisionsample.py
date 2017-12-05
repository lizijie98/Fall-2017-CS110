import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Collision Detection")

black = (0,0,0)
white = (255, 255, 255)
red = (255, 25, 25)
gray = (127,127,127)

clock = pygame.time.Clock()

def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if y2<=(y1+h1):
        if x2<=x1 and ((x2+w2)>(x1+w1)):
            return True
    else:
        return False

class ship:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def render(self, collision):
        if (collision == True):
            pygame.draw.rect(window, red, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))

class landZone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 1
    def render(self):
        pygame.draw.line(window,gray,(self.x,self.y),((self.x+self.width),self.y), self.height)

Ship = ship(400,50,25,25)
LandZone = landZone(300,500)

moveX, moveY = 0,0

gameLoop = True
while gameLoop:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                moveX = -4
            if (event.key == pygame.K_RIGHT):
                moveX = 4
            if (event.key == pygame.K_UP):
                moveY = -4
            if (event.key == pygame.K_DOWN):
                moveY = 4
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT):
                moveX = 0
            if (event.key == pygame.K_RIGHT):
                moveX = 0
            if (event.key == pygame.K_UP):
                moveY = 0
            if (event.key == pygame.K_DOWN):
                moveY = 0

    window.fill(white)
    Ship.x += moveX
    Ship.y += moveY
    collisions = detectCollisions(Ship.x, Ship.y, Ship.width, Ship.height, LandZone.x, LandZone.y, LandZone.width, LandZone.height)
    Ship.render(collisions)
    LandZone.render()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
