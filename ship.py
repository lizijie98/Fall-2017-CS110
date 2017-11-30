import pygame
import gameobject
import math

class Ship:
	def __init__(self, position = (0,0)):
		self.object = gameobject.GameObject(position, 0, "Player", "player")
		self.velocity = (0,0)
		#trying to make the vertical velocity drop by the gravitational accel every second
		#pygame.time.set_timer(self.Vertvelo - planet.gravity, 1) #not sure how the set_timer thing works.
		#two values below are actual values from apollo landing modules, might change to balance gameplay
		self.mainPower = 4.3584
		self.auxPower = 0.2748
		#also actual amount of time those boosters could be used, might change to balance gameplay
		self.mainFuel = 311
		self.auxFuel = 290
		self.image = "SillySteve.jpeg"
	def forward(self):
		print("Forward")
		#Lower mainFuel
		self.mainFuel -= 1
		#propel forward in current direction
		self.velocity = (self.velocity[0] + self.MainPower * math.cos(self.object.rotation), self.velocity[1] + self.MainPower * math.sin(self.object.rotation))
	def left(self):
                print("Left")
                #lower auxFuel
                self.auxFuel -= 1
                #Move left
                self.velocity = (self.velocity[0] - self.auxPower, self.velocity[1])
        def right(self):
                print("Right")
                #lower auxFuel
                self.auxFuel -= 1
                #Move left
                self.velocity = (self.velocity[0] + self.auxPower, self.velocity[1])
	def turn(self, angle):
		print("Turn " + str(angle))
		self.object.rotation += angle	
