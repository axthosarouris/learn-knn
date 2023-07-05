from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Distance:
    left: Point
    right: Point
    value: float


@dataclass
class Point:
    x: int
    y: int
    cat: Optional[str] = field(default=None)

    @classmethod
    def parseCsvLine(cls, line: str) -> Point:
        row = line.split(",")
        return Point(int(row[0]), int(row[1]), row[2])

    @classmethod
    def fromRow(cls, row) -> Point:
        return Point(int(row[1][0]), int(row[1][1]), row[1][2])

    def distance(self: Point, other: Point) -> Distance:
        value = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return Distance(self, other, value)
