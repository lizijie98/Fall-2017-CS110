import pygame
import gameobject
import math
import numpy
class Ship(pygame.sprite.Sprite):
	def __init__(self, fuel, position = (0,100)):
		super().__init__()
		self.position = position
		self.rotation = 0
		self.velocity = (0,0)
		self.image = pygame.image.load("normal.png").convert()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		print(self.rect)
		
		self.mainPower = .1
		
		self.fuel = fuel

	def turn(self, angle):
		#TURNS AT THE GIVEN ANGLE
		print("Turn " + str(angle))
		self.rotation += angle	
	def accelerate(self, direction, space):
		#DECREASES SHIPS FUEL
		if(self.fuel < 0):
			self.fuel = 0
		#ADDS THE DIRECTION VECTOR TO THE CURRENT VELOCITY
		direction = (direction[0] * self.mainPower, direction[1] * self.mainPower)
		if(space == "world"): #ACCELERATES THE SHIP USING SCREEN COORDINATES
			self.velocity = (self.velocity[0]+direction[0], self.velocity[1]+direction[1]) 

		else:  #ALLOWS FOR ACCELERATION RELATIVE TO THE SHIPS ROTATION
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
		
		
