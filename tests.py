import ship
def main():
    print("######## Testing player model#########")
    test_ship = ship.Ship();

    print("=====Standard Input Test=====")
    test_ship.Forward(5)
    assert  test_ship.x, test_ship.y == (5, 0)
main()
