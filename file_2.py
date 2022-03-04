from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    wheels: int
    doors: int
    engine_size: float


class Driver:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        pass


