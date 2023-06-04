from math import pi

class BoltResistanceCalc:
    def __init__(self, bolt, partialFactors):
        self._bolt = bolt
        self._partialFactors = partialFactors

    @property
    def FbRd_Y(self):
        alphaB = self._getAlphaB("y")
        k1 = self._getK1("y")
        fu = self._getTensileStrengthBearing()
        d = int(self._bolt.size[1:])
        t = self._bolt.plate.t
        ym2 = self._partialFactors.ym2

        return k1 * alphaB * fu * d * t / (ym2 * 10**3)

    @property
    def FbRd_X(self):
        alphaB = self._getAlphaB("x")
        k1 = self._getK1("x")
        fu = self._getTensileStrengthBearing()
        d = int(self._bolt.size[1:])
        t = self._bolt.plate.t
        ym2 = self._partialFactors.ym2

        return k1 * alphaB * fu * d * t / (ym2 * 10**3)

    @property
    def BpRd(self):
        dm = self._getDm()
        tp = self._bolt.plate.t
        fu = self._bolt.plate.material.tensileStrength
        ym2 = self._partialFactors.ym2

        return round(0.6 * pi * dm * tp * fu / (ym2 * 10**3), 2)

    @property
    def FtRd(self):
        k2 = self._getK2()
        fub = self._bolt.fub
        A = self._bolt.As
        ym2 = self._partialFactors.ym2

        return round(k2 * fub * A / (ym2 * 10**3), 2)

    @property
    def FvRd(self):
        alphaV = self._getAlphaV()
        fub = self._bolt.fub
        A = self._bolt.As
        ym2 = self._partialFactors.ym2

        return round(alphaV * fub * A / (ym2 * 10**3), 2)

    def _getDm(self):
        widthsAcrossFlats = {"M5": 8, "M6": 10, "M8": 13, "M10": 16,
                             "M12": 18, "M16": 24, "M20": 30, "M22": 34, "M24": 36,
                             "M27": 41, "M30": 46, "M33": 50, "M36": 55, "M39": 60}

        s = widthsAcrossFlats[self._bolt.size]

        return 1.07735 * s

    def _getAlphaB(self, direction):
        alphaD = self._getAlphaD(direction)
        fub = self._bolt.fub
        fu = self._bolt.plate.material.yieldStrength

        return min(alphaD, fub/fu, 1)

    def _getAlphaD(self, direction):
        if direction == "x":
            e1 = self._bolt.ex
            p1 = self._bolt.px
        elif direction == "y":
            e1 = self._bolt.ey
            p1 = self._bolt.py
        d0 = self._bolt.d0
        if self._bolt.checkIfEndBoltWidthDirection():
            return e1 / (3 * d0)
        return (p1 / (3 * d0)) - 1 / 4

    def _getK1(self, direction):
        if direction == "x":
            e2 = self._bolt.ey
        elif direction == "y":
            e2 = self._bolt.ex
        d0 = self._bolt.d0
        if self._bolt.checkIfEndBoltWidthDirection():
            return min(2.8*e2/d0 - 1.7, 2.5)
        return min(1.4*e2/d0 - 1.7, 2.5)

    def _getAlphaV(self):
        grade = self._bolt.grade
        if grade in ["4.6", "5.6", "8.8"]:
            return 0.6
        elif grade in ["4.8", "5.8", "6.8", "10.9"]:
            return 0.5

    def _getK2(self):
        if self._bolt.countersunk:
            return 0.63
        return 0.9

    def _getTensileStrengthBearing(self):
        fu = self._bolt.plate.material.tensileStrength
        if self._bolt.plate.material.stainless:
            fy = self._bolt.plate.material.yieldStrength
            return min(0.5*fy + 0.6*fu, fu)
        return fu
