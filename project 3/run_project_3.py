import pygame
from pygame.locals import *
import time
import main



def update():
    main.world_surface.fill((255,255,255))
    main.world_surface.blit(terrain_surface, (0,0))
    main.world.update()
    gameEvent()
    move()


def move():
    main.x += main.move_x
    main.y += main.move_y


def gameEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # stuff on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main.move_y += 1
            if event.key == pygame.K_DOWN:
                main.move_y -= 1
            if event.key == pygame.K_LEFT:
                main.move_x += 1
            if event.key == pygame.K_RIGHT:
                main.move_x -= 1
            if event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:
                main.zoom -= 1
                main.zoom = max(2, main.zoom)
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                main.zoom += 1
                main.zoom = min(20, main.zoom)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        # stuff on key lift
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                main.move_y = 0
            if event.key == pygame.K_DOWN:
                main.move_y = 0
            if event.key == pygame.K_LEFT:
                main.move_x = 0
            if event.key == pygame.K_RIGHT:
                main.move_x = 0


def drawTerrain():
    for x in range(len(main.world.terrain)):
        for y in range(len(main.world.terrain[0])):
            color = main.world.colorAt(x, y)
            rect = pygame.Rect(x*8 + main.x, y*8 + main.y, 8, 8)
            pygame.draw.rect(terrain_surface, color, rect)


main.init()
terrain_surface = pygame.Surface((main.width, main.height))
drawTerrain()
running = True
while running:
    time.sleep(1/60)
    main.screen.fill((255, 255, 255))
    update()
    scale_location = (main.x * main.zoom, main.y * main.zoom)
    new_size = (main.world.width * main.zoom, main.world.height * main.zoom)
    zoom_surface = pygame.Surface(new_size)
    pygame.transform.scale(main.world_surface, new_size, zoom_surface)
    main.screen.fill((255, 255, 255))
    main.screen.blit(zoom_surface, scale_location)
    pygame.display.flip()
