import perlin
import numpy as np
import random
import tree


class World:

    def __init__(self, width, height):
        self.objects = []
        self.width = width
        self.height = height
        r = random.randint(0, 999)
        self.terrain = np.zeros((width, height))
        noise = perlin.PerlinNoiseFactory(3, 24)
        print("starting terrain generation")
        for x in range(width):
            for y in range(height):
                self.terrain[x][y] = 0.5 + noise(x/width, y/height, r)
            p = x / width
            if (p * 100) % 10.0 < 0.3:
                print(int(p * 100), "% complete")
        self.spawnWorldObjects()
        print("generated world")

    def update(self):
        for obj in self.objects:
            if obj.alive:
                obj.update()

    def terrainAt(self, x, y):
        height = self.terrain[x][y]
        if height < 0.46:
            return("water")
        if height < 0.488:
            return("beach")
        elif height > 0.6:
            return("snow")
        else:
            return("grass")

    def colorAt(self, x, y):
        terrain_type = self.terrainAt(x, y)
        height = self.terrain[x][y]
        if terrain_type == "water":
            return((0, 0, 255))
        if terrain_type == "beach":
            return((220, 190, 150))
        elif terrain_type == "snow":
            return((200 + height * 10, 200 + height * 10, 250))
        else:
            # grass
            return((height * 159, height * 120 + 80, height * 120))

    def spawnObjectAt(self, object, world_x, world_y):
        # don't spawn objects out of bounds of the map
        if world_x > self.width or world_y > self.height or world_x < 0 or world_y < 0:
            return
        object.x = world_x * 8
        object.y = world_y * 8
        self.objects.append(object)

    def spawnWorldObjects(self):
        for x in range(self.width):
            for y in range(self.height):
                # tree generation
                if self.terrainAt(x, y) == "grass":
                    if random.randrange(0, 40) == 0:
                        print("spawn tree")
                        tr = tree.Tree()
                        tr.x = x * 8
                        tr.y = y * 8
                        self.objects.append(tr)
