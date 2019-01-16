import unittest
from assertpy import assert_that

from kata.final_grade import final_grade


class TestFinalGrade(unittest.TestCase):

    def test_should_return_100(self):
        # 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
        assert_that(final_grade(100,12)).is_equal_to(100)
        assert_that(final_grade(99,0)).is_equal_to(100)
        assert_that(final_grade(10,15)).is_equal_to(100)

    def test_should_return_90(self):
        # 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
        assert_that(final_grade(85, 5)).is_equal_to(90)

    def test_should_return_75(self):
        # 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
        assert_that(final_grade(55, 3)).is_equal_to(75)

    def test_should_return_0(self):
        assert_that(final_grade(55, 0)).is_equal_to(0)
        assert_that(final_grade(20, 2)).is_equal_to(0)
