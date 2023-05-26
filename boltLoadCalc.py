from math import sin, cos

class BoltLoadCalc:
    def __init__(self, bolt, load):
        self._bolt = bolt
        self._load = load

    def _getPxFx(self):
        Fx = self._load.Fx
        As = self._bolt.As
        sumA = self._bolt.areaForAllBolts

        return Fx * As / sumA

    def _getPyFy(self):
        Fy = self._load.Fy
        As = self._bolt.As
        sumA = self._bolt.areaForAllBolts

        return Fy * As / sumA

    def _getPxyMc(self):
        Mc = self._load.Mz * 10**3
        rc = self._bolt.rxy
        Ic = self._bolt.Icp
        As = self._bolt.As

        return Mc * rc * As / Ic

    def _getPxMz(self):
        PxyMc = self._getPxyMc()
        theta = self._bolt.theta

        return PxyMc * sin(theta)

    def _getPyMz(self):
        PxyMc = self._getPxyMc()
        theta = self._bolt.theta

        return PxyMc * cos(theta)

    def getPr(self):
        PxFx = self._getPxFx()
        PxMz = self._getPxMz()
        PyFy = self._getPyFy()
        PyMz = self._getPyMz()

        return ((PxFx + PxMz) ** 2 + (PyFy + PyMz) ** 2) ** 0.5

    def getPz(self):
        PzFz = self._getPzFz()
        PzMx = self._getPzMx()
        PzMy = self._getPzMy()

        return PzFz + PzMx + PzMy

    def _getPzFz(self):
        Fc = self._load.Fz
        As = self._bolt.As
        sumA = self._bolt.areaForAllBolts

        return Fc * As / sumA

    def _getPzMx(self):
        Mx = self._load.Mx * 10**3
        ry = self._bolt.ry
        Ix = self._bolt.Icx
        As = self._bolt.As

        return Mx * ry * As / Ix

    def _getPzMy(self):
        My = self._load.My * 10**3
        rx = self._bolt.rx
        Iy = self._bolt.Icy
        As = self._bolt.As

        return My * rx * As / Iy









