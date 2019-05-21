import pygame
from pygame.locals import *
import time
from project_2 import DNA

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)

project_dna = DNA().from_json("test.json")

(width, height) = (640, 360)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("DNA Sequence Visualization: " + project_dna.strand)
running = True

def draw_dna(string):
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    x = 6
    y = 30
    for c in string:
        if c == "a":
            pygame.draw.rect(screen, red, pygame.Rect(x, y, zoom, zoom))
        if c == "t":
            pygame.draw.rect(screen, blue, pygame.Rect(x, y, zoom, zoom))
        if c == "g":
            pygame.draw.rect(screen, green, pygame.Rect(x, y, zoom, zoom))
        if c == "c":
            pygame.draw.rect(screen, yellow, pygame.Rect(x, y, zoom, zoom))
        x += zoom + 1

strands = [project_dna.strand]
index = 0
zoom = 5
while running:
    time.sleep(1/60)
    screen.fill((255,255,255))

    draw_dna(strands[index])

    colors = font.render("A = red, T = blue, G = green, C = yellow", False, (0,0,0))
    screen.blit(colors, (3,3))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zoom += 1
            if event.key == pygame.K_DOWN:
                zoom -= 1
                zoom = max(zoom, 5)
            if event.key == pygame.K_LEFT:
                index -= 1
                index = max(0, index)
            if event.key == pygame.K_RIGHT:
                project_dna.strand = project_dna.mutation()
                strands += project_dna.strand
                index += 1
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
