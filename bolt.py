from boltLoadCalc import BoltCalc
from math import atan

class Bolt:
    def __init__(self, size, grade, x, y, load):
        self._size = size
        self._grade = grade
        self._x = x
        self._y = y
        self._load = load
        self._plate = None
        self._bolts = None

    def add_plate(self, plate):
        self._plate = plate

    def add_bolts(self, bolts):
        self._bolts = bolts

    @property
    def areaForAllBolts(self):
        return sum([bolt.As for bolt in self._bolts])

    @property
    def n(self):
        return len(self._bolts)

    @property
    def rx(self):
        return abs(self._x - self._plate.xc)

    @property
    def ry(self):
        return abs(self.y - self._plate.yc)

    @property
    def theta(self):
            return atan(self.ry / self.rx)

    @property
    def rxy(self):
        return (self.rx**2 + self.ry**2)**0.5

    @property
    def Icx(self):
        return sum([bolt.ry**2 * bolt.As for bolt in self._bolts])

    @property
    def Icy(self):
        return sum([bolt.rx**2 * bolt.As for bolt in self._bolts])

    @property
    def Icp(self):
        return sum([bolt.rxy**2 * bolt.As for bolt in self._bolts])

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
        return min(self._plate.width - self._x, self._x)

    @property
    def ey(self):
        return min(self._plate.height - self._y, self._y)

    @property
    def px(self):
        for bolt in self._bolts:
            if self.y == bolt.y:
                px = abs(self.x - bolt.x)
                break
        return px

    @property
    def py(self):
        for bolt in self._bolts:
            if self._x == bolt.x:
                py = abs(self._y - bolt.y)
                break
        return py

    @property
    def Pz(self):
        calc = BoltCalc(self, self._load)

        return calc.getPz()

    @property
    def Pr(self):
        calc = BoltCalc(self, self._load)

        return calc.getPr()