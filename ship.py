import pygame
import gameobject
import math
import numpy
class Ship:
	def __init__(self, position = (0,0)):
		self.object = gameobject.GameObject(position, 0, "Player", "player")
		self.velocity = (0,0)
		#two values below are actual values from apollo landing modules, might change to balance gameplay
		self.mainPower = 4.3584
		self.auxPower = 0.2748
		#also actual amount of time those boosters could be used, might change to balance gameplay
		self.mainFuel = 311
		self.auxFuel = 290
		self.image = "SillySteve.jpeg"
	def forward(self):
		print("Forward")
		self.mainFuel -= 1
		#propel forward in current direction
		self.velocity = (self.velocity[0] + self.MainPower * math.cos(self.object.rotation), self.velocity[1] + self.MainPower * math.sin(self.object.rotation))
	def left(self):
                print("Left")
                self.auxFuel -= 1
                self.velocity = (self.velocity[0] + self.auxPower, self.velocity[1])
	def right(self):
                print("Right")
                self.auxFuel -= 1
                #Move left
                self.velocity = (self.velocity[0] + self.auxPower, self.velocity[1])
	def turn(self, angle):
		#TURNS AT THE GIVEN ANGLE
		print("Turn " + str(angle))
		self.object.rotation += angle	
	def accelerate(self, direction):
		#ADDS THE DIRECTION VECTOR TO THE CURRENT VELOCITY
		rot = self.object.rotation * (math.pi / 180)
		newDir = numpy.matrix([[direction[0]],[direction[1]]])
		#rotation matrix converting input vector in screen coordinates to vector relative to ship's rotation
		mat = numpy.matrix([[math.cos(rot),-math.sin(rot)],[math.sin(rot),math.cos(rot)]])
		newDir = numpy.matmul(mat,newDir)
		print(newDir)
		self.velocity = (self.velocity[0]+float(newDir[0]), self.velocity[0]+float(newDir[1]))
		print(self.velocity)
		
