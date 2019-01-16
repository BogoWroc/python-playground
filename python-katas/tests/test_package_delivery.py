import unittest
from assertpy import assert_that, fail

from kata.package_delivery import Package, DimensionsOutOfBoundError


class TestPackageDelivery(unittest.TestCase):

    def test_package_creation(self):
        package = Package(1,1,1)
        assert_that(package).is_not_none()

    def test_should_raise_exception_when_value_is_out_of_range(self):
        try:
            Package.validate("length", 351, lower=0, upper=350)
        except DimensionsOutOfBoundError as e:
            assert_that(str(e)).is_equal_to('Package length==351 out of bounds, should be: 0 < length <= 350')

        try:
            Package.validate("length", 350, lower=0, upper=350)
        except DimensionsOutOfBoundError:
            fail()

    def test_should_raise_exception_during_object_creation_when_value_is_out_of_range(self):
        try:
            Package(351, 1, 5)
        except DimensionsOutOfBoundError as e:
            assert_that(str(e)).is_equal_to('Package length==351 out of bounds, should be: 0 < length <= 350')

        try:
            Package(350, 1, 5)
        except DimensionsOutOfBoundError:
            fail()

    def test_should_raise_exception_during_setting_value_when_value_is_out_of_range(self):
        try:
            package = Package(350, 1, 5)
            package.length = 351
        except DimensionsOutOfBoundError as e:
            assert_that(str(e)).is_equal_to('Package length==351 out of bounds, should be: 0 < length <= 350')

        try:
            package = Package(50, 1, 5)
            package.length = 350
        except DimensionsOutOfBoundError:
            fail()



