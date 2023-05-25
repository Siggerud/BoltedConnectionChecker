class Bolt:
    def __init__(self, size, grade, x, y, plate, bolts):
        self._size = size
        self._grade = grade
        self._x = x
        self._y = y
        self._plate = plate
        self._plateWidth = plate["width"]
        self._plateHeight = plate["height"]
        self._bolts = bolts

    @property
    def As(self):
        tensileStressAreas = {"M4": 8.78, "M5": 14.18, "M6": 20.12, "M8": 36.61, "M10": 58.00,
                              "M12": 84.27, "M16": 156.67, "M20": 244.79, "M22": 303.4, "M24": 352.5,
                              "M27": 459.41, "M30": 560.59, "M33": 693.55, "M36": 816.72, "M39": 976}

        return tensileStressAreas[self._size]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def ex(self):
        return min(self._plateWidth - self._x, self._x)

    @property
    def ey(self):
        return min(self._plateHeight - self._y, self._y)

    @property
    def px(self):
        for bolt in self._bolts:
            if self.y == bolt.y:
                px = abs(self.y - bolt.y)
        return px

    @property
    def py(self):
        for bolt in self._bolts:
            if self._x == bolt.x:
                py = abs(self._y - bolt.y)
        return py