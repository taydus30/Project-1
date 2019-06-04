import perlin
import numpy as np
import random
import tree
import main
import berry_bush

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
        print("generated world")
        self.age = 0
        self.curr_year = 0

    def update(self):
        self.age += 1
        years = self.age // (60 / main.simulation_speed)
        if years > self.curr_year:
            self.curr_year += 1
            print("year ", years)
        for obj in self.objects:
            if obj.alive:
                obj.update()

    def heightAt(self, x, y):
        return(self.terrain[x][y])

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

    def objectAt(self, x, y):
        out = None
        for obj in self.objects:
            if(obj.world_x() == x and obj.world_y() == y):
                out = obj
        # we want to return the object if one is there
        # ie if an animal is looking at nearby objects for food it would set
        # alive to false to show its eaten
        return(out)

    def spawnObjectAt(self, object, world_x, world_y):
        # don't spawn if an object would overlap
        if self.objectAt(world_x, world_y) is not None:
            return
        # don't spawn objects out of bounds of the map
        if world_x >= self.width or world_y >= self.height or world_x < 0 or world_y < 0:
            return
        object.x = world_x * 8
        object.y = world_y * 8
        self.objects.append(object)
        return(object)

    def spawnWorldObjects(self):
        tree.spawnInWorld()
        berry_bush.spawnInWorld()
        print("generated world objects")
