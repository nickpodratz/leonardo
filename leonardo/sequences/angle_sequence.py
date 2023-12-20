from typing import cast, overload

from ..geometry import Angle
from .arithmetic_sequence import ArithmeticSequence


class AngleSequence(ArithmeticSequence):
    """An arithmetic sequence that revolves."""

    def __init__(self, angle: Angle) -> None:
        super().__init__(common_difference=angle.radians, initial_term=0.0)

    @overload
    def __getitem__(self, subscript: int) -> Angle:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[Angle]:
        ...

    def __getitem__(self, subscript: int | slice) -> Angle | list[Angle]:
        item = super().__getitem__(subscript)
        if isinstance(subscript, int):
            radians = cast(float, item)
            return Angle(radians)
        if isinstance(subscript, slice):
            list_of_radians = cast(list[float], item)
            return list(map(lambda radians: Angle(radians), list_of_radians))
