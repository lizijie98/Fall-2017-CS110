import planet
import ship
def main():
	plan = planet.Planet(10, 100)
	print(plan.nodes)

	player = ship.Ship((0,0), 10, 500, "image")
	player.forward()
	print(player.velocity)
	player.turn(90)
	print(player.object.rotation)
	player.accelerateDown(10)
	print(player.velocity)
main()
