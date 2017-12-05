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
		self.nodeSpace = 800/50 #temporary values until pygame is setup to get the screen width
		self.generateTerrain(gradient)
		self.generateSectors()

	def generateTerrain(self, gradient):
		for i in range(50):
			node = ((i+1) * self.nodeSpace, (600-random.randrange(-gradient, gradient)))
			self.nodes.append(node)

	def generateSectors(self):
		for i in range(9): #index should be 1 less than nodes
			slope = (self.nodes[i+1][1]-self.nodes[i][1])/(self.nodes[i+1][0]-self.nodes[i][0])
			self.sectors.append(slope)		
	#def drawPlanet(self):
	#	#Uses turtle to draw the planet until pygame is setup
	#	turt = turtle.Turtle()
	#	wn = turtle.Screen()
	#	for i in self.nodes:
	#		turt.goto(i)
	#	wn.exitonclick()

