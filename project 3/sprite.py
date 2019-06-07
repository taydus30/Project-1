import pygame
import main


def toWorldPoint(p):
    return(int(p // 8))


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
        if(self.terrAt() == "out"):
            self.alive = False
        self.age += 1
        if self.alive:
            main.world_surface.blit(self.surface, (self.x, self.y))

    def world_x(self):
        return int(self.x // 8)

    def world_y(self):
        return int(self.y // 8)

    def years(self):
        return(self.age // (60 / main.simulation_speed))

    def terrAt(self, xx=None, yy=None):
        if xx is None:
            xx = self.world_x()
        if yy is None:
            yy = self.world_y()
        # simple func for shortening code
        return(main.world.terrainAt(xx, yy))

    def move(self, x_mod, y_mod):
        farthest_x = 0
        farthest_y = 0
        x1 = 0
        y1 = 0
        while x1 != x_mod and y1 != y_mod:
            new_x = toWorldPoint(self.x + x1)
            new_y = toWorldPoint(self.y + y1)
            terr = self.terrAt(new_x, new_y)
            if terr != "water" and terr != "out":
                farthest_x = x1
                farthest_y = y1
            if(x1 < x_mod):
                x1 += 1
            elif x1 > x_mod:
                x1 -= 1
            if(y1 < y_mod):
                y1 += 1
            elif y1 > y_mod:
                y1 -= 1
        self.x += farthest_x
        self.y += farthest_y

    def objectsInRange(self, ran):
        wx = self.world_x()
        wy = self.world_y()
        objs = []
        for r in range(1, ran + 1):
            xx = r
            for yy in range(0, r):
                0
                if(xx != 0):
                    0
                if(yy != 0):
                    0
                    if(xx != 0):
                        0
                xx -= 1
