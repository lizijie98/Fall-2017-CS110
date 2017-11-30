import gameobject
import math
class Ship:
	def __init__(self, position = (0,0)):
		self.object = gameobject.GameObject(position, 0, "Player", "player")
		self.velocity = (0,0)
		self.power = 50
		self.fuel = 500
		self.image = "SillySteve.jpeg"
	def forward(self):
		#lower fuel
		print("Forward")
		self.fuel -= 1
		#propel forward in current direction
		self.velocity = (self.velocity[0] + self.power * math.cos(self.object.rotation), self.velocity[1] + self.power * math.sin(self.object.rotation))
	def turn(self, angle):
		print("Turn " + str(angle))
		self.object.rotation += angle
	def accelerateDown(self, force):
		self.velocity = (self.velocity[0],self.velocity[1] - force)
	
		
