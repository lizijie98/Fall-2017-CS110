class Ship:
	def __init__(self, position, power, fuel, image):
		self.x, self.y = position
		self.direction = 0
		self.power = power
		self.fuel = fuel
		self.image = image
	def forward(self):
		#lower fuel
		#propel forward in current direction
	def turn(self, angle):
		self.direction += angle
	def moveTowards(self, point, force):
		#do math to figure this out
	
		
