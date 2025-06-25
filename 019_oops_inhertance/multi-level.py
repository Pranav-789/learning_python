class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips
        pass

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = PuneFactory("Cotton", 1, "red", 3)