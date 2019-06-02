import noise
import numpy as np
import random

class World:

    def __init__(self, width=200, height=200):
        r = random.randint(0, 999)
        self.terrain = np.zeros((width, height))
        for x in range(width):
            for y in range(height):
                self.terrain[x][y] = 0.5 + noise.pnoise3(x/100.0,
                                                   y/100.0,
                                                   r,
                                                   octaves = 6,
                                                   persistence = 0.8,
                                                   lacunarity = 1.7,
                                                   base=0) * 0.5
        print(self.terrain)

    def terrainAt(x, y):
        height = self.terrain[x][y]
        if height < 0.47:
            return("water")
        if height < 0.488:
            return("beach")
        elif height > 0.6:
            return("snow")
        else:
            return("grass")
