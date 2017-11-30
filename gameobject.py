class GameObject:
	def __init__(self, position, rotation, name, objtype):
		self.position = position
		self.rotation = rotation
		self.name = name
		self.objtype = objtype
	def __str__(self):
		return name
	def updatePosition(self, velocity):
		self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])

		
