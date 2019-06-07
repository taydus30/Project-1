import pygame
import main


class Sprite:

    x:     int = 0
    y:     int = 0
    age:   int = 0

    def __init__(self, filename, x=0, y=0):
        self.surface = pygame.image.load("img/" + filename)
        self.alive = True
        self.x = x
        self.y = y

    def update(self):
        self.age += 1
        if self.alive:
            main.world_surface.blit(self.surface, (self.x , self.y) )

    def world_x(self):
        return int(self.x // 8)

    def world_y(self):
        return int(self.y // 8)

    def years(self):
        return(self.age // (60 / main.simulation_speed))

    def terrAt(self):
        #simple func for shortening code
        return(main.world.terrainAt(self.world_x(), self.world_y()))

    def objectInRange(self, range):
        objects = []
        for i in range(range):
            obj = main.world.objectAt(self.world_x() + i, self.world_y())
            if obj != None:
                objects.append(obj)
            obj = main.world.objectAt(self.world_x(), self.world_y() + i)
            if obj != None:
                objects.append(obj)
            obj = main.world.objectAt(self.world_x() - i, self.world_y())
            if obj != None:
                objects.append(obj)
            obj = main.world.objectAt(self.world_x(), self.world_y() - i)
            if obj != None:
                objects.append(obj)

            if (i - 1) != 0:
                obj = main.world.objectAt(self.world_x() + (i - 1), self.world_y() + (i - 1))
                if obj != None:
                    objects.append(obj)
                obj = main.world.objectAt(self.world_x() + (i - 1), self.world_y() - (i - 1))
                if obj != None:
                    objects.append(obj)
                obj = main.world.objectAt(self.world_x() - (i - 1), self.world_y() - (i - 1))
                if obj != None:
                    objects.append(obj)
                obj = main.world.objectAt(self.world_x() - (i - 1), self.world_y() + (i - 1))
                if obj != None:
                    objects.append(obj)
        return(objects)
