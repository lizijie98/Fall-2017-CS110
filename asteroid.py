import pygame
class Asteroid(pygame.sprite.Sprite):
	def __init__(self, position):
		super().__init__()
		self.position = position
		self.velocity = (-2,0)
		self.image = pygame.image.load("asteroid.png").convert()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()

	def update(self):
		#UPDATE FUNCTION FOR THE SPRITE, MOVES THE ASTEROID BASED ON ITS CURRENT VELOCITY
		self.position = (self.position[0] + self.velocity[0], self.position[1]+self.velocity[1])
		self.rect.x, self.rect.y = self.position

