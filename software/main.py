import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_1, K_2, K_3, K_4, QUIT

from threading import Thread
from time import sleep

from random import randint

import software.parametros as pr

import os


class Cara():
    def __init__(self, alto_screen, ancho_screen, screen) -> None:

        self.screen = screen

        self.height = alto_screen
        self.width = ancho_screen
        self.set_images()

        self.mode(3)

        self.thread()

    def scale(self, escala, position):
        escala[0] *= self.width
        escala[1] *= self.height

        self.ancho = escala[0]
        self.alto = escala[1]

        self.alto_ojos = escala[1]
        self.alto_boca = escala[1]*0.25

        self.alto_blush = escala[1]*0.2

        self.posicion = [self.width*position[0], self.height*position[1]]
        self.punto = self.posicion.copy()

    def move(self):
        punto = pygame.mouse.get_pos()
        x = (punto[0] - self.posicion[0])/3
        if x > self.ancho:
            x = self.ancho
        elif x < -self.ancho:
            x = -self.ancho
        y = (punto[1] - self.posicion[1])/3
        if y > self.alto/4:
            y = self.alto/4
        elif y < -self.alto:
            y = -self.alto

        self.ojo1 = [self.posicion[0] - (self.ancho * 3) + x,
                     self.posicion[1] - self.alto/2 + y + int((self.alto - self.alto_ojos)/2)]

        self.ojo2 = [self.posicion[0] + (self.ancho * 2) + x,
                     self.posicion[1] - self.alto/2 + y  + int((self.alto - self.alto_ojos)/2)]

        self.boca = [self.posicion[0] - self.ancho/2 + x/3,
                     self.posicion[1] + self.alto/3 + y/3]



    def draw(self):
        self.move()

        self.screen.fill(self.color_fondo)


        # --- OJOS ----
        pygame.draw.ellipse(self.screen, self.color,
                            pygame.Rect(self.ojo1[0], self.ojo1[1],
                                        self.ancho, self.alto_ojos))
        pygame.draw.ellipse(self.screen, self.color,
                            pygame.Rect(self.ojo2[0], self.ojo2[1],
                                        self.ancho, self.alto_ojos))
        # --- BOCA ----
        pygame.draw.ellipse(self.screen, self.color,
                            pygame.Rect(self.boca[0], self.boca[1],
                                        self.ancho, self.alto_boca))

        pygame.draw.ellipse(self.screen, self.color_fondo,
                            pygame.Rect(self.boca[0] + self.ancho/10,
                                        self.boca[1] + self.ancho/10,
                                        self.ancho - self.ancho/5,
                                        self.alto_boca - self.ancho/5))

        pygame.draw.rect(self.screen, self.color_fondo,
                            pygame.Rect(self.boca[0], self.boca[1],
                                        self.ancho, self.alto_boca/2))

        pygame.draw.ellipse(self.screen, self.color,
                            pygame.Rect(self.boca[0],
                                        self.boca[1] + self.alto_boca/2 - self.ancho/20,
                                        self.ancho/10, self.ancho/10))

        pygame.draw.ellipse(self.screen, self.color,
                            pygame.Rect(self.boca[0] + self.ancho - self.ancho/10,
                                        self.boca[1] + self.alto_boca/2 - self.ancho/20,
                                        self.ancho/10, self.ancho/10))

        if self.option == 1:
            self.screen.blit(self.show, (self.width/10, self.height*2/10))

        if self.option == 2:
            pass

        if self.option == 3:
            pygame.draw.ellipse(self.screen, pr.COLOR_BLUSH,
                    pygame.Rect(self.ojo1[0], self.alto*2,
                                self.ancho, self.alto_blush))
            pygame.draw.ellipse(self.screen, pr.COLOR_BLUSH,
                    pygame.Rect(self.ojo2[0], self.alto*2,
                                self.ancho, self.alto_blush))

    def set_images(self):
        self.images = []
        for n in os.listdir('source/'):
            self.images.append(pygame.transform.scale(pygame.image.load(f'source/{n}'), (self.width*8/10, self.height*7/10)))
        image = Thread(target=self.show_image, daemon=True)
        image.start()

    def thread(self):
        pestañeo = Thread(target=self.blink, daemon=True)
        pestañeo.start()

    def show_image(self):
        while True:
            self.show = self.images[randint(0, len(self.images)-1)]
            sleep(5.1)


    def blink(self):
        step = 30

        while True:
            if self.option == 1:
                time = 0.001
            else:
                time = 0.005
            sleep(3)
            for _ in range(step):
                self.alto_ojos -= self.alto/(step*1.1)
                sleep(time)

            for _ in range(step):
                self.alto_ojos += self.alto/(step*1.1)
                sleep(time)

    def mode(self, option):
        self.option = option
        if self.option == 0:
            self.scale([1/10, 3/9], [1/2, 3/7])
            self.color = (0, 0, 0)
            self.color_fondo = pr.COLOR_CARA
        elif self.option == 1:
            self.scale([1/30, 1/10], [1/2, 1/10])
            self.color = (0, 0, 0)
            self.color_fondo = pr.COLOR_CARA
        elif self.option == 2:
            self.scale([1/10, 3/9], [1/2, 3/7])
            self.color = (0, 0, 0)
            self.color_fondo = pr.COLOR_ANGRY
        elif self.option == 3:
            self.scale([1/10, 3/9], [1/2, 3/7])
            self.color = (0, 0, 0)
            self.color_fondo = pr.COLOR_CARA




pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

# cara = Cara([pr.SCREEN_WIDTH/2, pr.SCREEN_HEIGHT*3/7], pr.SCREEN_WIDTH/9, screen)
cara = Cara(pr.SCREEN_HEIGHT, pr.SCREEN_WIDTH, screen)

run = 1
while run:
    for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    run = 0

                if event.key == K_1:
                    cara.mode(0)

                if event.key == K_2:
                    cara.mode(1)

                if event.key == K_3:
                    cara.mode(2)

                if event.key == K_4:
                    cara.mode(3)


            elif event.type == QUIT:
                run = 0


    cara.draw()


    # --- LINEAS GUIA ---
    # for n in range(12):
    #     pygame.draw.line(screen, (150, 150, 150), [pr.SCREEN_WIDTH/2 + n*100, 0], [pr.SCREEN_WIDTH/2 + n*100, pr.SCREEN_HEIGHT], width=5)
    #     pygame.draw.line(screen, (150, 150, 150), [pr.SCREEN_WIDTH/2 - n*100, 0], [pr.SCREEN_WIDTH/2 - n*100, pr.SCREEN_HEIGHT], width=5)
    #     pygame.draw.line(screen, (150, 150, 150), [0, pr.SCREEN_HEIGHT/2 + n*100], [pr.SCREEN_WIDTH, pr.SCREEN_HEIGHT/2 + n*100], width=5)
    #     pygame.draw.line(screen, (150, 150, 150), [0, pr.SCREEN_HEIGHT/2 - n*100], [pr.SCREEN_WIDTH, pr.SCREEN_HEIGHT/2 - n*100], width=5)


    pygame.display.flip()
