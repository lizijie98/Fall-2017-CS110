import random
import turtle
class Planet:
	def __init__(self, gravity, gradient):
		self.gravity = gravity
		#GENERATES THE TERRAIN OF THE PLANET
		#Gradient is used for the maximum change in the terrain height from one node to the 			#next
		self.nodes = []
		nodeSpace = 500/10 #temporary values until pygame is setup to get the screen width
		
		for i in range(10):
			node = ((i+1) * nodeSpace, random.randrange(-gradient, gradient))
			self.nodes.append(node)
	def drawPlanet(self):
		#Uses turtle to draw the planet until pygame is setup
		turt = turtle.Turtle()
		wn = turtle.Screen()
		for i in self.nodes:
			turt.goto(i)
		wn.exitonclick()

