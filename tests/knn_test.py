from assertpy import assert_that

from knn.knn import Knn, Point

SAMPLE = "resources/sample.csv"


class KnnTest:

    @staticmethod
    def should_return_nearest_neighbor_for_unclassified_file_when_compared_to_dataset():
        knn = Knn(SAMPLE)
        actual_nn = knn.nearest(Point(3, 6))
        assert_that(actual_nn).is_equal_to(Point(1, 3, "B"))
