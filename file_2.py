

class Car:
    def __init__(self, wheels, doors, engine_size, speed=0):
        self.wheels: int = wheels
        self.doors: int = doors
        self.engine_size: float = engine_size
        self.speed: float = speed

    def accelerate_1(self):
        self.speed += 1

