import pygame

pygame.init()


SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

proporcion = SCREEN_WIDTH/SCREEN_HEIGHT


PASO_H = SCREEN_HEIGHT/10
PASO_W = SCREEN_WIDTH/10


OJO_ANCHO = PASO_W
OJO_ALTO = OJO_ANCHO*1.75
OJO_STEP = OJO_ALTO/30


COLOR_CARA = (194,216,214)
