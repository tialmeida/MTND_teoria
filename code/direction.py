from enum import Enum


class Direction(Enum):
    L = 'E'
    R = 'D'
    I = 'I'

    @staticmethod
    def get_from_value(value):
        if Direction.L.value == value:
            return Direction.L
        elif Direction.R.value == value:
            return Direction.R
        else:
            return Direction.I
