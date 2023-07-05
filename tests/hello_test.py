from assertpy import assert_that

from knn import hello


class HelloFunctionTest:

    def should_return_hello(self):
        assert_that(hello.message()).is_equal_to("hello worldd")
