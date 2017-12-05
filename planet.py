import random
import turtle
import gameobject
class Planet:
	def __init__(self, gravity, gradient):
		self.object = gameobject.GameObject((0,0), 0, "Planet", "planet")
		self.gravity = gravity
		#GENERATES THE TERRAIN OF THE PLANET
		#Gradient is used for the maximum change in the terrain height from one node to the 			#next
		self.nodes = []
		self.sectors = [] #list of line segment slopes that make up the terrain used for collision later
		self.nodeSpace = 800/20 #temporary values until pygame is setup to get the screen width
		self.generateTerrain(gradient)
		self.generateSectors()

	def generateTerrain(self, gradient):
		for i in range(20):
			node = [(i+1) * self.nodeSpace, (600-random.randrange(-gradient, gradient))]
			self.nodes.append(node)
		#calculates highest node 
		highestPoint = 800
		highestIndex = 0
		for i in range(len(self.nodes)):
			if(self.nodes[i][1] < highestPoint): #pygame low = higher on screen
				highestPoint = self.nodes[i][1]
				highestIndex = i
			print(highestIndex)
			print(highestPoint)
		#creates a landing platform at highest node
		self.plat = [[]]
		n=self.nodes #shorthandvariable for self.nodes
		if(highestIndex == 0):
			self.plat = [n[highestIndex][0],highestPoint],[n[highestIndex + 1][0],highestPoint]
		else:
			self.plat = [n[highestIndex - 1][0],highestPoint],[n[highestIndex][0],highestPoint]
		print(self.plat)
	def generateSectors(self):
		for i in range(len(self.nodes) - 1): #index should be 1 less than nodes
			slope = (self.nodes[i+1][1]-self.nodes[i][1])/(self.nodes[i+1][0]-self.nodes[i][0])
			self.sectors.append(slope)
	def getSector(self, ship):
		for i in self.nodes:
			if(ship.position[0] < i[0]):
				return i
		return -1 #SHOULD NEVER RETURN THIS, SOMETHING WENT WRONG IF IT DID	
	#def drawPlanet(self):
	#	#Uses turtle to draw the planet until pygame is setup
	#	turt = turtle.Turtle()
	#	wn = turtle.Screen()
	#	for i in self.nodes:
	#		turt.goto(i)
	#	wn.exitonclick()

