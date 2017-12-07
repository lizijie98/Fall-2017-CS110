import random
class Planet:
	def __init__(self, gravity, gradient):
		self.gravity = gravity
		#GENERATES THE TERRAIN OF THE PLANET
		#Gradient is used for the maximum change in the terrain height from one node to the next
		self.nodes = []
		self.nodeSpace = 800/20 #Based on screen width and number of nodes 
		self.generateTerrain(gradient)

	def generateTerrain(self, gradient):
                #GENERATES A TERRAIN FOR THE PLANET USING A GIVEN GRADIENT
		for i in range(20):
			node = [(i+1) * self.nodeSpace, (600-random.randrange(-gradient, gradient))]
			self.nodes.append(node)


		#CALCULATES THE HIGHEST NODE
		highestPoint = 800
		highestIndex = 0
		for i in range(len(self.nodes)):
			if(self.nodes[i][1] < highestPoint): #pygame low = higher on screen
				highestPoint = self.nodes[i][1]
				highestIndex = i


		#CREATES A LANDING PLATFORM AT THE HIGHEST NODE
		self.plat = [[]]

		n=self.nodes #shorthandvariable for self.nodes
		highestPoint -= 5 #Sets the platform slightly above the rest of the terrain
		if(highestIndex == 0): #Changes which index is used if highestIndex is 0
			self.plat = [n[highestIndex][0],highestPoint],[n[highestIndex + 1][0],highestPoint]
			self.platStand = [self.nodes[highestIndex + 1],self.plat[1]]
		else:
			self.plat = [n[highestIndex - 1][0],highestPoint],[n[highestIndex][0],highestPoint]
			self.platStand = [self.nodes[highestIndex - 1],self.plat[0]]
		print(self.plat)
		print(self.platStand)

		
		
