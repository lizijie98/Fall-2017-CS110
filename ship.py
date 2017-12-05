import pygame
import gameobject
import math
import numpy
class Ship(pygame.sprite.Sprite):
	def __init__(self, position = (0,800)):
		super().__init__()
		self.position = position
		self.rotation = 0
		self.velocity = (0,0)
		#NAME FILE FORMAT ship_*angle*.png
		self.image = pygame.image.load("normal.png").convert()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		print(self.rect)
		#two values below are actual values from apollo landing modules, might change to balance gameplay
		self.mainPower = .1
		self.auxPower = 0.2748
		#also actual amount of time those boosters could be used, might change to balance gameplay
		self.mainFuel = 311
		self.auxFuel = 290

	def turn(self, angle):
		#TURNS AT THE GIVEN ANGLE
		print("Turn " + str(angle))
		self.rotation += angle	
	def accelerate(self, direction, space):
		#ADDS THE DIRECTION VECTOR TO THE CURRENT VELOCITY
		direction = (direction[0] * self.mainPower, direction[1] * self.mainPower)
		if(space == "world"):
			#THIS LINE USES MOMENTUM
			self.velocity = (self.velocity[0]+direction[0], self.velocity[1]+direction[1]) 
			#self.velocity = direction #NO MOMENTUM

		else:
			rot = self.rotation * (math.pi / 180)
			newDir = numpy.matrix([[direction[0]],[direction[1]]])
			newDir = newDir * self.mainPower
			#rotation matrix converting input vector in screen coordinates to vector relative to ship's rotation
			mat = numpy.matrix([[math.cos(rot),-math.sin(rot)],[math.sin(rot),math.cos(rot)]])
			newDir = numpy.matmul(mat,newDir)
			print(newDir)
			self.velocity = (self.velocity[0]+float(newDir[0]), self.velocity[0]+float(newDir[1]))
			print(self.velocity)
	def velMagnitude(self):
		return math.sqrt(self.velocity[0] ** 2 + self.velocity[1] **2)
		
		
