import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT

import parametros as pr

class Cara():
    def __init__(self, posicion, ancho, color=(0, 0, 0), fondo=(pr.COLOR_CARA)) -> None:
        self.ancho = ancho
        self.alto = ancho*1.75
        self.alto_boca = ancho*0.5

        self.posicion = posicion

        self.color = color
        self.color_fondo = fondo


    def move(self):
        punto = pygame.mouse.get_pos()
        x = (punto[0] - self.posicion[0])/30
        y = (punto[1] - self.posicion[1])/30

        self.ojo1 = [self.posicion[0] - (self.ancho * 3) + x,
                     self.posicion[1] - self.alto/2 + y]

        self.ojo2 = [self.posicion[0] + (self.ancho * 2) + x,
                     self.posicion[1] - self.alto/2 + y]

        self.boca = [self.posicion[0] - self.ancho/2 + x/3,
                     self.posicion[1] + self.alto/3 + y/3]


    def draw(self, screen):
        self.move()
        # --- OJOS ----
        pygame.draw.ellipse(screen, self.color,
                            pygame.Rect(self.ojo1[0], self.ojo1[1],
                                        self.ancho, self.alto))
        pygame.draw.ellipse(screen, self.color,
                            pygame.Rect(self.ojo2[0], self.ojo2[1],
                                        self.ancho, self.alto))
        # --- BOCA ----
        pygame.draw.ellipse(screen, self.color,
                            pygame.Rect(self.boca[0], self.boca[1],
                                        self.ancho, self.alto_boca))

        pygame.draw.ellipse(screen, self.color_fondo,
                            pygame.Rect(self.boca[0] + self.ancho/10,
                                        self.boca[1] + self.ancho/10,
                                        self.ancho - self.ancho/5,
                                        self.alto_boca - self.ancho/5))

        pygame.draw.rect(screen, self.color_fondo,
                            pygame.Rect(self.boca[0], self.boca[1],
                                        self.ancho, self.alto_boca/2))

        pygame.draw.ellipse(screen, self.color,
                            pygame.Rect(self.boca[0],
                                        self.boca[1] + self.alto_boca/2 - self.ancho/20,
                                        self.ancho/10, self.ancho/10))

        pygame.draw.ellipse(screen, self.color,
                            pygame.Rect(self.boca[0] + self.ancho - self.ancho/10,
                                        self.boca[1] + self.alto_boca/2 - self.ancho/20,
                                        self.ancho/10, self.ancho/10))



pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)


cara = Cara([pr.SCREEN_WIDTH/2, pr.SCREEN_HEIGHT*3/7], pr.SCREEN_WIDTH/9)
# cara = Cara([pr.SCREEN_WIDTH/4, pr.SCREEN_HEIGHT/5], pr.SCREEN_WIDTH/15)


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


    screen.fill(pr.COLOR_CARA)


    cara.draw(screen)


    # for n in range(12):
    #     pygame.draw.line(screen, (150, 150, 150), [pr.SCREEN_WIDTH/2 + n*100, 0], [pr.SCREEN_WIDTH/2 + n*100, pr.SCREEN_HEIGHT], width=5)
    #     pygame.draw.line(screen, (150, 150, 150), [pr.SCREEN_WIDTH/2 - n*100, 0], [pr.SCREEN_WIDTH/2 - n*100, pr.SCREEN_HEIGHT], width=5)
    #     pygame.draw.line(screen, (150, 150, 150), [0, pr.SCREEN_HEIGHT/2 + n*100], [pr.SCREEN_WIDTH, pr.SCREEN_HEIGHT/2 + n*100], width=5)
    #     pygame.draw.line(screen, (150, 150, 150), [0, pr.SCREEN_HEIGHT/2 - n*100], [pr.SCREEN_WIDTH, pr.SCREEN_HEIGHT/2 - n*100], width=5)


    pygame.display.flip()