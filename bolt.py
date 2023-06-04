from boltLoadCalc import BoltLoadCalc
from math import atan

class Bolt:
    def __init__(self, size, grade, x, y, load, countersunk=False):
        self._size = size
        self._grade = grade
        self._x = x
        self._y = y
        self._load = load
        self._plate = None
        self._bolts = None
        self._countersunk = countersunk

    def checkIfEndBoltHeightDirection(self):
        min = self.plate.yc
        max = min
        for bolt in self._bolts:
            if bolt.y < min:
                min = bolt.y
            elif bolt.y > max:
                max = bolt.y

        y = self.y
        if y == min or y == max:
            return True
        return False

    def checkIfEndBoltWidthDirection(self):
        min = self.plate.xc
        max = min
        for bolt in self._bolts:
            if bolt.x < min:
                min = bolt.x
            elif bolt.x > max:
                max = bolt.x

        x = self.x
        if x == min or x == max:
            return True
        return False


    @property
    def countersunk(self):
        return self._countersunk

    def add_plate(self, plate):
        self._plate = plate

    def add_bolts(self, bolts):
        self._bolts = bolts

    @property
    def fub(self):
        return int(self.grade[0]) * 100

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
    def d0(self):
        holeSizes = {"M5": 5.5, "M6": 6.6, "M8": 9, "M10": 11, "M12": 14, "M16": 18, "M20": 22,
                     "M22": 24, "M24": 26, "M27": 30, "M30": 33, "M33": 36, "M36": 39, "M39": 42}

        return holeSizes[self._size]

    @property
    def As(self):
        tensileStressAreas = {"M5": 14.18, "M6": 20.12, "M8": 36.61, "M10": 58.00,
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
        calc = BoltLoadCalc(self, self._load)

        return calc.getPz()

    @property
    def Pr(self):
        calc = BoltLoadCalc(self, self._load)

        return calc.getPr()

    @property
    def grade(self):
        return self._grade

    @property
    def size(self):
        return self._size

    @property
    def plate(self):
        return self._plate