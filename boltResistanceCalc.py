class BoltResistanceCalc:
    def __init__(self, bolt, partialFactors):
        self._bolt = bolt
        self._partialFactors = partialFactors
        self._alphaV = self._getAlphaV()
        self._k2 = self._getK2()

    @property
    def FtRd(self):
        k2 = self._k2
        fub = self._bolt.fub
        A = self._bolt.As
        ym2 = self._partialFactors.ym2

        return round(k2 * fub * A / (ym2 * 10**3), 2)

    @property
    def FvRd(self):
        alphaV = self._alphaV
        fub = self._bolt.fub
        A = self._bolt.As
        ym2 = self._partialFactors.ym2

        return round(alphaV * fub * A / (ym2 * 10**3), 2)

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
