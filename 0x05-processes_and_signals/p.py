#!/usr/bin/python3
from enum import Enum, auto

class Chess(Enum):
    QUEEN = 300
    KING = auto()

new = Chess.KING
print(new.value)