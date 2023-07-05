from __future__ import annotations

import pandas as pd
import functools
from typing import List

from knn.point import Distance, Point


class Knn:

    def __init__(self, filename: str):
        self.filename = filename
        self.dataset = self.__read_file__(filename)

    @staticmethod
    def __read_file__(filename: str) -> List[Point]:
        dataframe = pd.read_csv(filename,header=None)
        rows = dataframe.iterrows()
        dataset = [Point.fromRow(row) for row in rows]
        return dataset

    def calculate_distances(self, unclassified: Point) -> List[Distance]:
        return [unclassified.distance(classified) for classified in self.dataset]

    def nearest(self, unclassified: Point) -> Point:
        distances = map(lambda point: unclassified.distance(point), self.dataset)
        nearest = functools.reduce(lambda left, right: left if left.value < right.value else right, distances)
        return nearest.right