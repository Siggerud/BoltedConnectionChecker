class Plate:
    def __init__(self, width, height, thickness, material):
        self._width = width
        self._height = height
        self._thickness = thickness
        self._material = material
        self._bolts = None

    def add_bolts(self, bolts):
        self._bolts = bolts

    @property
    def material(self):
        return self._material

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def t(self):
        return self._thickness

    @property
    def xc(self):
        xc = sum([bolt.x * bolt.As for bolt in self._bolts]) / sum([bolt.As for bolt in self._bolts])
        return xc

    @property
    def yc(self):
        yc = sum([bolt.y * bolt.As for bolt in self._bolts]) / sum([bolt.As for bolt in self._bolts])
        return yc











