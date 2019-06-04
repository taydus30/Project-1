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
            main.world_surface.blit(self.surface, (self.x + main.x, self.y + main.y) )

    def world_x(self):
        return int(self.x // 8)

    def world_y(self):
        return int(self.y // 8)

    def years(self):
        return(self.age // 60)

    def terrAt(self):
        #simple func for shortening code
        return(main.world.terrainAt(self.world_x(), self.world_y()))
