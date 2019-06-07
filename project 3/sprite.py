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
        self.age += 1
        if self.alive:
            main.world_surface.blit(self.surface, (self.x , self.y) )

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
        for x1 in range(0, x_mod):
            for y1 in range(0, y_mod):
                terr = self.terrAt(toWorldPoint(self.x + x1), toWorldPoint(self.y + y1))
                if terr != "water":
                    self.x = x1
                    self.y = y1
        # dont go out of bounds
        self.x = max(self.x, 0)
        self.x = min(self.x, main.width)
        self.y = max(self.x, 0)
        self.y = min(self.x, main.height)
