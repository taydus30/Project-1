"""
Created By: Tucker, Dustyn,
Project 2
DNA calculations
"""


import pygame
from pygame.locals import *
import time
from project_2 import DNA

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 16)

project_dna = DNA().from_json("test.json")

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("DNA Sequence Visualization: " + project_dna.strand)
running = True

def draw_dna(string):
    red = (255, 50, 50)
    blue = (90, 90, 255)
    green = (50, 255, 50)
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
zoom = 20
while running:
    time.sleep(1/60)
    screen.fill((255,255,255))

    draw_dna(strands[index])
    test_strand = DNA(strands[index])

    colors = font.render("A = red, T = blue, G = green, C = yellow", True, (0,0,0))
    instructions = font.render("left/right: advance in time through mutations,    up/down: zoom in and out", True, (0,0,0))
    st = font.render("generation: " + str(index + 1) + " / " + str(len(strands)), True, (0,0,0))
    gc_comp = font.render("GC Comp: " + str(test_strand.gc_comp()), True, (0,0,0))
    base_freq = "Base Frequencies: " + "A: " + str(test_strand.base_frequencies("a")) + " T: " + str(test_strand.base_frequencies("t")) + " C: " + str(test_strand.base_frequencies("c")) + " G: " + str(test_strand.base_frequencies("g"))
    bases = font.render(base_freq, True, (0,0,0))
    mrna = font.render("mRNA: " + test_strand.mrna(), True, (0,0,0))

    if(zoom > 9):
        a = 0
        for c in test_strand.strand:
            i = font.render(c, True, (0,0,0))
            screen.blit(i, (a + 2 + zoom / 2 , zoom + 10))
            a += zoom + 1


    screen.blit(colors, (3,3))
    screen.blit(instructions, (3, zoom + 40))
    screen.blit(st, (3, zoom + 65))
    screen.blit(gc_comp, (3, zoom + 85))
    screen.blit(bases, (3, zoom + 110))
    screen.blit(mrna, (3, zoom + 135))
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
                if index == len(strands) - 1:
                    project_dna.strand = project_dna.mutation()
                    strands.append(project_dna.strand.lower())
                    print("new sequence: ", project_dna.strand)
                    index += 1
                else:
                    index += 1
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
