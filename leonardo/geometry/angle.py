import math
from dataclasses import dataclass
from typing import Self


@dataclass
class Angle:
    fraction: float = 0

    @classmethod
    def from_radians(cls, radians: float) -> Self:
        fraction = radians / math.tau
        return cls(fraction)

    @classmethod
    def from_degrees(cls, degrees: float) -> Self:
        fraction = degrees / 360
        return cls(fraction)

    @property
    def fraction_canonic(self) -> float:
        return self.fraction % 1

    @property
    def radians(self) -> float:
        return self.fraction * math.tau

    @property
    def radians_canonic(self) -> float:
        return self.radians % math.tau

    @property
    def degrees(self) -> float:
        return self.fraction * 360

    @property
    def degrees_canonic(self) -> float:
        return self.degrees % 360

    @property
    def complex(self) -> complex:
        real = math.cos(self.radians)
        imag = math.sin(self.radians)
        return complex(real, imag)

    def __str__(self) -> str:
        return f"{self.degrees:.2f}\u00B0"
