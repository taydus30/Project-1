import pygame
from pygame.locals import *
import time
import numpy as np
import noise
from world import World

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 16)

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("project 3")
running = True

world = World()

def setup():
    print('setup')


def update():
    draw_terrain()

def draw_terrain():
    for x in range(len(world.terrain)):
        for y in range(len(world.terrain[0])):
            height = world.terrain[x][y]
            color = get_terrain_color(height)
            pygame.draw.rect(screen, color, pygame.Rect(x*5, y*5, 5, 5))

def get_terrain_color(height):
    if height < 0.47:
        return((0,0,255))
    if height < 0.488:
        return((220,190,150))
    elif height > 0.6:
        return((200 + height * 10,200 + height * 10,250))
    else:
        return((height * 159, height * 120 + 80, height * 120))

setup()
while running:
    time.sleep(1/60)
    screen.fill((255,255,255))
    update()
    pygame.display.flip()
