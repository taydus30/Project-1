import pygame
from pygame.locals import *
from world import World


def init():
    global screen
    global world
    global font
    global x
    global y
    global move_x
    global move_y
    global zoom
    global world_surface

    zoom = 0

    move_x = 0
    move_y = 0

    x = 0
    y = 0

    (width, height) = (640, 360)

    world_surface = pygame.Surface((width, height))
    world = World(width // 8, height // 8)

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 16)

    screen = pygame.display.set_mode((width, height))

    pygame.display.flip()
    pygame.display.set_caption("project 3")
