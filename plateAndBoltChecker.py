class loadCalc:
    def __init__(self, plate, beam, bolts):
        self._plate = plate
        self._bolts = bolts
        self._beam = beam
        self._boltCentroid = self._getBoltCentroid()

    def _getBoltCentroid(self):
        xc = sum([bolt.x * bolt.As for bolt in self._bolts]) / sum([bolt.As for bolt in self._bolts])
        yc = sum([bolt.y * bolt.As for bolt in self._bolts]) / sum([bolt.As for bolt in self._bolts])

        return (xc, yc)





    