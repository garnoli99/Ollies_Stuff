from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    wheels: int
    doors: int
    engine_size: float
