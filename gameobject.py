import pygame as py
class GameObject:
	def __init__(self, position, rotation, name, objtype):
		py.init()
		self.position = position
		self.rotation = rotation
		self.name = name
		self.objtype = objtype
	def __str__(self):
		return name
	def updatePosition(self, velocity):
		self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])
	def drawTerrain(self, nodes):
		while(1==1):
			surf = py.Surface((500,300))
			if(self.objtype == "planet"):
				py.draw.lines(surf, 0xffffff, False, nodes) 
		
