class DimensionsOutOfBoundError(Exception):
    pass


class Package(object):
    def __init__(self, length, width, height, weight=1):
        Package.validate("length", length, 0, 350)
        Package.validate("width", width, 0, 300)
        Package.validate("height", height, 0, 150)
        Package.validate("weight", weight, 0, 40)

        self._weight = weight
        self._height = height
        self._width = width
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        Package.validate("length", value, 0, 350)
        self._length = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        Package.validate("weight", value, 0, 40)
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        Package.validate("height", value, 0, 150)
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        Package.validate("width", value, 0, 300)
        self._width = value

    @property
    def volume(self):
        return self.length * self.width * self.height

    @staticmethod
    def validate(variable, value, lower, upper):
        if not lower < value <= upper:
            raise DimensionsOutOfBoundError(
                "Package {variable}=={value} out of bounds, should be: {lower} < {variable} <= {upper}".format(
                    variable=variable,
                    value=value,
                    lower=lower,
                    upper=upper
                )
            )
