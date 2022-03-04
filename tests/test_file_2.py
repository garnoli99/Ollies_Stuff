from file_2 import Car


def test_car_drives():
    car = Car(wheels=4, doors=4, engine_size=200, speed=0)
    car.accelerate_1()

    assert car.speed == 1
