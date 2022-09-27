import pygame
from pygame.locals import *

import numpy as np

import parametros as pr
from parametros import *


pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)


pestañeo = 0
cont = 0

run = 1
while run:
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = 0

            elif event.type == QUIT:
                run = 0
    screen.fill(COLOR_CARA)


    cont += 1

    if cont > 1000:
        if cont < 1000 + 60:
            if cont%5 == 0:
                pestañeo += OJO_STEP
        elif cont < 1000 + 60 + 60:
            if cont%5 == 0:
                pestañeo -= OJO_STEP
    if cont > 1000 + 60 + 60:
        pestañeo = 0
        cont = 0




    punto = pygame.mouse.get_pos()
    x = (SCREEN_WIDTH - punto[0])/80
    y = (SCREEN_HEIGHT - punto[1])/80



    pygame.draw.ellipse(screen, (0, 0, 0),
                        Rect(SCREEN_WIDTH/2 - PASO_W*3 - x*3, SCREEN_HEIGHT/2 - PASO_H*2 + pestañeo - y*3,
                        OJO_ANCHO, OJO_ALTO - pestañeo*2))

    pygame.draw.ellipse(screen, (0, 0, 0),
                        Rect(SCREEN_WIDTH/2 + PASO_W*3 - OJO_ANCHO - x*3, SCREEN_HEIGHT/2 - PASO_H*2 + pestañeo - y*3,
                        OJO_ANCHO, OJO_ALTO - pestañeo*2))

    pygame.draw.ellipse(screen, (0, 0, 0),
                        Rect(SCREEN_WIDTH/2-90 - x, SCREEN_HEIGHT/2 - y,
                        180, 100))

    pygame.draw.ellipse(screen, COLOR_CARA,
                        Rect(SCREEN_WIDTH/2-70 - x, SCREEN_HEIGHT/2 - y,
                        140, 80))

    pygame.draw.rect(screen, COLOR_CARA,
                        Rect(SCREEN_WIDTH/2-90 - x, SCREEN_HEIGHT/2 - y,
                        180, 50))

    pygame.draw.ellipse(screen, (0, 0, 0),
                        Rect(SCREEN_WIDTH/2-90 - x, SCREEN_HEIGHT/2+40 - y,
                        22, 20))

    pygame.draw.ellipse(screen, (0, 0, 0),
                        Rect(SCREEN_WIDTH/2+90-22 - x, SCREEN_HEIGHT/2+40 - y,
                        22, 20))



    pygame.display.flip()